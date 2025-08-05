from groq import Groq
from langchain.llms.base import LLM
from typing import Optional, List, Mapping, Any
from pydantic import PrivateAttr, Field
from langchain.output_parsers import PydanticOutputParser, OutputFixingParser
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from backend.schemas.resume_output import TailoredResume
from backend.services.resume_prompt import resume_prompt
import re
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise ValueError("GROQ_API_KEY environment variable not set. Please check your .env file.")


class GroqLLM(LLM):
    _client: Groq = PrivateAttr()

    model: str = Field(default="llama-3.3-70b-versatile")
    temperature: float = Field(default=0.7)
    max_tokens: int = Field(default=512)

    def __init__(
        self,
        api_key: str,
        model: Optional[str] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        **kwargs,
    ):
        super().__init__(
            model=model or "llama-3.3-70b-versatile",
            temperature=temperature or 0.7,
            max_tokens=max_tokens or 512,
            **kwargs,
        )
        self._client = Groq(api_key=api_key)

    @property
    def _llm_type(self) -> str:
        return "groq"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        response = self._client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            stop=stop,
        )
        return response.choices[0].message.content

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        return {
            "model": self.model,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
        }


# Initialize Groq LLM
llm = GroqLLM(api_key=API_KEY)

# Setup parsers
base_parser = PydanticOutputParser(pydantic_object=TailoredResume)
parser = OutputFixingParser.from_llm(parser=base_parser, llm=llm)

# Setup prompt
prompt = PromptTemplate(
    template=resume_prompt,
    input_variables=["resume", "jd", "tone", "focus"],
    partial_variables={"format_instructions": base_parser.get_format_instructions()},
)

# Setup chain
chain = LLMChain(llm=llm, prompt=prompt)


def generate_tailored_resume(resume_text, jd_text, tone, focus):
    raw_output_dict = chain.invoke(
        {
            "resume": resume_text,
            "jd": jd_text,
            "tone": tone,
            "focus": focus,
        }
    )

    print("=== Raw Chain Output ===")
    print(raw_output_dict)

    llm_text = raw_output_dict.get("text")
    if not llm_text or not llm_text.strip():
        raise RuntimeError("LLM returned empty output, cannot parse.")

    # Find JSON in output and parse
    json_start = re.search(r"\{", llm_text)
    if json_start:
        llm_text = llm_text[json_start.start() :].strip()
    else:
        raise RuntimeError("No JSON found in LLM output")

    parsed = parser.parse(llm_text)
    return parsed.dict()
