from pydantic import BaseModel, validator
from typing import List, Optional

class TailorRequest(BaseModel):
    resume_text: str
    job_description: str
    tone: str = "formal"
    focus: str = "impact"

class Experience(BaseModel):
    job_title: str
    company: str
    duration: str
    description: str

class Project(BaseModel):
    title: str
    description: str
    tech_stack: Optional[List[str]] = []

class Education(BaseModel):
    degree: str
    institution: str
    duration: str

class TailoredResume(BaseModel):
    name: str
    summary: str
    skills: List[str]
    experience: List[Experience]
    projects: Optional[List[Project]] = []
    education: Optional[List[Education]] = []
    
    @validator('projects', pre=True)
    def filter_empty_projects(cls, v):
        if isinstance(v, list):
            # Filter out empty dictionaries or objects with missing required fields
            filtered = []
            for project in v:
                if isinstance(project, dict) and project.get('title') and project.get('description'):
                    filtered.append(project)
            return filtered
        return v
    
    @validator('education', pre=True)
    def filter_empty_education(cls, v):
        if isinstance(v, list):
            # Filter out empty dictionaries or objects with missing required fields
            filtered = []
            for edu in v:
                if isinstance(edu, dict) and edu.get('degree') and edu.get('institution'):
                    filtered.append(edu)
            return filtered
        return v