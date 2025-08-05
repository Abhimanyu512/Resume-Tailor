from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from ..services.llm_service import generate_tailored_resume
from ..schemas.resume_output import TailorRequest
from ..utils.pdf_generator import generate_resume_pdf
import io

router = APIRouter()

@router.post("/generate-tailored-resume")
async def generate_tailored(data: TailorRequest):
    try:
        response = generate_tailored_resume(
            resume_text=data.resume_text,
            jd_text=data.job_description,
            tone=data.tone,
            focus=data.focus
        )
        return {"tailored_resume": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/generate-tailored-resume-pdf")
async def generate_tailored_pdf(data: TailorRequest):
    try:
        # Generate the tailored resume
        resume_data = generate_tailored_resume(
            resume_text=data.resume_text,
            jd_text=data.job_description,
            tone=data.tone,
            focus=data.focus
        )
        
        # Generate PDF
        pdf_buffer = generate_resume_pdf(resume_data)
        
        # Create filename based on the person's name
        filename = f"{resume_data.get('name', 'resume').replace(' ', '_')}_tailored_resume.pdf"
        
        # Return PDF as streaming response
        return StreamingResponse(
            io.BytesIO(pdf_buffer.getvalue()),
            media_type="application/pdf",
            headers={"Content-Disposition": f"attachment; filename={filename}"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))