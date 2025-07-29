from backend.services.llm_service import generate_tailored_resume

resume_text = """
John Doe
Backend Engineer with 4+ years of experience building REST APIs using Java and Spring Boot.
Worked on banking domain, database tuning, and API design.

Experience:
- Company: ABC Tech
- Title: Software Engineer
- Duration: 2019–2023
- Projects: Core banking, Limits Management, ETL pipelines

Skills: Java, Spring Boot, SQL, REST, Informatica

Education: B.Tech in Computer Science, XYZ University
"""

jd_text = """
We’re looking for a Backend Engineer with strong Java + Spring Boot experience. 
Bonus if you've worked with LLM APIs, database optimization, and clean API design.
"""

# output = generate_tailored_resume(resume_text, jd_text, tone="formal", focus="impact")
# print(output)

result = generate_tailored_resume(
    resume_text=resume_text,
    jd_text=jd_text,
    tone="professional",
    focus="leadership"
)
print(result)
