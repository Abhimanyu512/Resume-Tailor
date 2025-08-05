from fastapi import APIRouter, UploadFile, File, HTTPException, Form
from pydantic import BaseModel
from app.utils.parser import parse_resume_file  # your existing resume parser

router = APIRouter()

# Resume Upload Endpoint
@router.post("/parse-resume")
async def parse_resume(file: UploadFile = File(...)):
    try:
        resume_text = parse_resume_file(file)
        print(resume_text)
        return {"resume_text": resume_text}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# @router.post("/api/tailor-full")
# def tailor_full_resume(
#     resume_text: str = Form(...),
#     jd_text: str = Form(...),
#     tone: str = Form("formal"),
#     focus: str = Form("impact")
# ):
#     tailored_resume = generate_tailored_resume(resume_text, jd_text, tone, focus)
#     return tailored_resume

# Job Description Plain Text Endpoint
class JobDescriptionRequest(BaseModel):
    job_description: str

@router.post("/parse-job-description")
async def parse_job_description(data: JobDescriptionRequest):
    try:
        jd_text = data.job_description.strip()
        if not jd_text:
            raise ValueError("Job description is empty.")
        print(jd_text)
        return {"job_description_text": jd_text}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
