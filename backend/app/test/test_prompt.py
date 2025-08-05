import os
from langchain_community.llms import GPT4All
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from backend.schemas.resume_output import TailoredResume
from backend.services.resume_prompt import resume_prompt


# prompt = PromptTemplate(
#     template=resume_prompt,
#     input_variables=["resume", "jd", "tone", "focus"],
# )


# def generate_tailored_resume(resume_text, jd_text, tone, focus):
#     # Setup parser and model
#     parser = PydanticOutputParser(pydantic_object=TailoredResume)

#     llm = GPT4All(
#         model="/Users/zoro/Library/Application Support/nomic.ai/GPT4All/mistral-7b-instruct-v0.1.Q4_0.gguf",
#         allow_download=False
#     )
#     chain = prompt | llm

#     try:
#         # 1. Print formatted prompt to check variable interpolation
#         formatted_prompt = prompt.format(
#             resume=resume_text,
#             jd=jd_text,
#             tone=tone,
#             focus=focus
#         )
#         print("\n=== FORMATTED PROMPT ===\n")
#         print(formatted_prompt)
#         print("\n=== END OF PROMPT ===\n")

#         # 2. Invoke the chain with inputs
#         raw_output = llm.invoke(formatted_prompt)

#         print("=== RAW MODEL OUTPUT ===")
#         print(raw_output)
#         print("=== END RAW OUTPUT ===\n")

#         # 3. Extract model response text and print it
#         model_response = raw_output.strip()
#         print("=== MODEL RESPONSE TEXT ===")
#         print(model_response)
#         print("=== END MODEL RESPONSE ===\n")

#         # 4. Try parsing the JSON output using Pydantic
#         parsed_resume = parser.parse(model_response)
#         print("=== PARSED RESUME OBJECT ===")
#         print(parsed_resume)
#         print("=== END PARSED RESUME ===\n")

#         return parsed_resume.dict()

#     except Exception as e:
#         print("Exception during generation or parsing:", e)
#         return {
#             "error": str(e),
#             "raw_output": raw_output if 'raw_output' in locals() else None
#         }

# # Example test calls with different resumes

# resume1 = """
# John Doe
# Backend Engineer with 4+ years experience in Java, Spring Boot, and database tuning.
# Worked at ABC Corp on core banking and ETL pipelines.
# """

# resume2 = """
# Jane Smith
# Data Scientist with expertise in Python, ML, and data analysis.
# Experience in predictive modeling and customer analytics.
# """

# jd = """
# Looking for a Backend Engineer experienced with Java, Spring Boot, and team leadership.
# """

# print("### TEST with resume 1 ###")
# output1 = generate_tailored_resume(resume1, jd, tone="professional", focus="leadership")

# print("### TEST with resume 2 ###")
# output2 = generate_tailored_resume(resume2, jd, tone="professional", focus="leadership")


# from langchain_community.llms import GPT4All
# from langchain.prompts import PromptTemplate
# from langchain.output_parsers import PydanticOutputParser
# from backend.schemas.resume_output import TailoredResume  # your Pydantic model

# Initialize model
llm = GPT4All(
    model="/Users/zoro/Library/Application Support/nomic.ai/GPT4All/mistral-7b-instruct-v0.1.Q4_0.gguf",
    allow_download=False
    # temperature=0.0,
)

# Setup parser
parser = PydanticOutputParser(pydantic_object=TailoredResume)

prompt = PromptTemplate(
    template=resume_prompt,
    input_variables=["resume", "jd", "tone", "focus"]
)

chain = prompt | llm

def generate_tailored_resume(resume_text, jd_text, tone, focus):
    formatted_prompt = prompt.format(
        resume=resume_text,
        jd=jd_text,
        tone=tone,
        focus=focus
    )
    print("=== FORMATTED PROMPT ===")
    print(formatted_prompt)

    raw_output = chain.invoke({
        "resume": resume_text,
        "jd": jd_text,
        "tone": tone,
        "focus": focus,
    })
    print("=== RAW MODEL OUTPUT ===")
    print(raw_output)

    parsed = parser.parse(raw_output.strip())
    print("=== PARSED RESUME ===")
    print(parsed)
    return parsed.dict()

# Example usage
resume_text1 = """
Jane Smith
Data Scientist with expertise in Python, ML, and data analysis.
Experience in predictive modeling and customer analytics.
"""

resume_text2 = """
John Doe
Backend Engineer with 4+ years experience in Java, Spring Boot, and database tuning.
Worked at ABC Corp on core banking and ETL pipelines.
"""

resume_text3 = """
Johdfaksjn Doeodlafskjcxm
Backend Engineer with 1 years experience in Scala, and oracle.
Worked at alkdm comp on modeling pipelines.
"""

jd_text = """
Looking for a Backend Engineer experienced with Java, Spring Boot, and team leadership.
"""

print("### TEST with resume 1 ###")
output1 = generate_tailored_resume(resume_text1, jd_text, tone="professional", focus="leadership")

print("### TEST with resume 2 ###")
output2 = generate_tailored_resume(resume_text2, jd_text, tone="professional", focus="leadership")


print("### TEST with resume 2 ###")
output3 = generate_tailored_resume(resume_text3, jd_text, tone="professional", focus="leadership")

# generate_tailored_resume(resume_text, jd_text, tone="professional", focus="leadership")
