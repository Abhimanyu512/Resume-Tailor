from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
from app.utils.parser import parse_resume_file  # your existing resume parser

router = APIRouter()

# Resume Upload Endpoint
@router.post("/parse-resume")
async def parse_resume(file: UploadFile = File(...)):
    try:
        resume_text = parse_resume_file(file)
        return {"resume_text": resume_text}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Job Description Plain Text Endpoint
class JobDescriptionRequest(BaseModel):
    job_description: str

@router.post("/parse-job-description")
async def parse_job_description(data: JobDescriptionRequest):
    try:
        jd_text = data.job_description.strip()
        if not jd_text:
            raise ValueError("Job description is empty.")
        return {"job_description_text": jd_text}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
