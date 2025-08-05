from pydantic import BaseModel
from typing import List, Optional

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