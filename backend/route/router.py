from fastapi import APIRouter, UploadFile, File, Form
from app.services.resume_utils import extract_text_from_resume
from app.services.jd_analyzer import extract_keywords_from_jd

router = APIRouter()

@router.post("/parse_resume")
async def parse_resume(file: UploadFile = File(...)):
    content = await file.read()
    text = extract_text_from_resume(file.filename, content)
    return {"extracted_text": text}

@router.post("/analyze_jd")
async def analyze_jd(jd_text: str = Form(...)):
    keywords = extract_keywords_from_jd(jd_text)
    return {"keywords": keywords}