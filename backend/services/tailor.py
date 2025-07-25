from fastapi import APIRouter, Form
from app.services.llm_service import generate_tailored_resume

router = APIRouter()

@router.post("/tailor")
async def tailor_resume(
    resume_text: str = Form(...),
    jd_text: str = Form(...),
    tone: str = Form("formal"),
    focus: str = Form("project impact")
):
    tailored_result = generate_tailored_resume(resume_text, jd_text, tone, focus)
    return tailored_result