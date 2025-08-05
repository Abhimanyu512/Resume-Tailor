from fastapi import APIRouter, Form
from backend.services.llm_service import generate_tailored_resume
from backend.schemas.resume_output import TailoredResume

router = APIRouter()

@router.post("/generate-tailored-resume")
async def generate_tailored(data: TailoredResume):
    try:
        response = generate_tailored_resume(
            resume_text=data.resume,
            jd_text=data.job_description,
            tone=data.tone,
            focus=data.focus
        )
        return {"tailored_resume": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))