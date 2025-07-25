from fastapi import APIRouter, UploadFile, File, HTTPException
from app.utils.parser import parse_resume_file

router = APIRouter()

@router.post("/parse-resume")
async def parse_resume(file: UploadFile = File(...)):
    try:
        resume_text = parse_resume_file(file)
        return {"resume_text": resume_text}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/api/tailor-full")
def tailor_full_resume(
    resume_text: str = Form(...),
    jd_text: str = Form(...),
    tone: str = Form("formal"),
    focus: str = Form("impact")
):
    tailored_resume = generate_tailored_resume(resume_text, jd_text, tone, focus)
    return tailored_resume