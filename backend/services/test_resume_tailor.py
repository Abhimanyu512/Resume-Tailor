from backend.services.llm_service import generate_tailored_resume
import json
resume_text = json.loads("""
{
  "name": "Sudhanshu Iyer",
  "summary": "Product Engineer with 4+ years of experience in Java, Spring Boot, and SQL. Experienced in building scalable backend systems and working closely with stakeholders to deliver impactful solutions.",
  "skills": ["Java", "Spring Boot", "SQL", "REST APIs", "Informatica", "Oracle", "Microservices", "Docker"],
  "experience": [
    {
      "job_title": "Senior Product Engineer",
      "company": "MBBLabs Pvt. Ltd.",
      "duration": "03/2023 - Present",
      "description": "Led development of a Limits Management Application that improved core banking operations for over 1M accounts. Worked with stakeholders to define product roadmaps and implemented features using Java and Spring Boot."
    },
    {
      "job_title": "Product Engineer",
      "company": "MBBLabs Pvt. Ltd.",
      "duration": "07/2020 - 03/2023",
      "description": "Built RESTful APIs for risk profiling and exposure tracking. Improved ETL pipelines using Informatica and tuned SQL queries for optimal database performance."
    }
  ],
  "projects": [
    {
      "title": "Smart Scheduler",
      "description": "Built an AI-powered task manager that reorders tasks based on priority and estimated completion time using a local ML model and FastAPI backend.",
      "tech_stack": ["Python", "FastAPI", "scikit-learn", "PostgreSQL"]
    },
    {
      "title": "Resume Tailor",
      "description": "Developed a system that customizes resumes and generates cover letters using LLMs like GPT-4 and LangChain.",
      "tech_stack": ["Python", "LangChain", "OpenAI", "Java Spring Boot"]
    }
  ],
  "education": [
    {
      "degree": "MS in Computer Science",
      "institution": "XYZ University, USA",
      "duration": "2024 - 2026"
    },
    {
      "degree": "B.Tech in Computer Engineering",
      "institution": "ABC Institute of Technology, India",
      "duration": "2016 - 2020"
    }
  ]
}
""")

jd_text = """
We’re looking for a Backend Engineer with strong Java + Spring Boot experience. 
Bonus if you've worked with LLM APIs, database optimization, and clean API design.
"""

# output = generate_tailored_resume(resume_text, jd_text, tone="formal", focus="impact")
# print(output)
import re

# def preprocess_resume_text(text):
#     # Add space after periods, commas, colons if not followed by space
#     text = re.sub(r'([.,:;!?])(?=[^\s])', r'\1 ', text)
    
#     # Replace multiple newlines or missing spaces between words with a single space
#     text = re.sub(r'\s+', ' ', text)

#     # Optional: add newline before sections like EDUCATION, WORK EXPERIENCE for clarity
#     for section in ["EDUCATION", "WORK EXPERIENCE", "PROJECTS", "SKILLS", "AWARDS", "RELEVANT PROJECTS"]:
#         text = re.sub(rf'(?i){section}', f'\n{section}', text)
    
#     return text.strip()

# cleaned_resume = preprocess_resume_text(resume_text)
# print(cleaned_resume)
result = generate_tailored_resume(
    resume_text=resume_text,
    jd_text=jd_text,
    tone="professional",
    focus="leadership"
)
print(result)
