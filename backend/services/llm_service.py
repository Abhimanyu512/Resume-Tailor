import os
from langchain_community.llms import GPT4All
# from langchain.schema import RunnableSequence
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from backend.schemas.resume_output import TailoredResume
from backend.services.resume_prompt import resume_prompt
from pathlib import Path

# Setup output parser
parser = PydanticOutputParser(pydantic_object=TailoredResume)

# Init GPT4All
llm = GPT4All(
    model="/Users/zoro/Library/Application Support/nomic.ai/GPT4All/mistral-7b-instruct-v0.1.Q4_0.gguf",  # folder path
    allow_download=False  # optional, prevents auto-download
)

prompt = PromptTemplate(
    template=resume_prompt,
    input_variables=["resume", "jd", "tone", "focus"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = LLMChain(llm=llm, prompt=prompt)

import json

def generate_tailored_resume(resume_text, jd_text, tone, focus):
    try:
        raw_output = chain.invoke({
            "resume": resume_text,
            "jd": jd_text,
            "tone": tone,
            "focus": focus,
        })

        # raw_output is a dict, extract the 'text' key which contains the actual model response string
        model_response = raw_output.get("text", "")
        model_response = model_response.strip()

        # Now parse the JSON string using your Pydantic parser
        parsed_resume = parser.parse(model_response)

        return parsed_resume.dict()

    except Exception as e:
        return {
            "error": str(e),
            "raw_output": raw_output if 'raw_output' in locals() else None
        }

