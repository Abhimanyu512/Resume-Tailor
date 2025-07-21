import pdfplumber
import docx
from fastapi import UploadFile

def extract_text_from_pdf(file: UploadFile) -> str:
    with pdfplumber.open(file.file) as pdf:
        return "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

def extract_text_from_docx(file: UploadFile) -> str:
    doc = docx.Document(file.file)
    return "\n".join([para.text for para in doc.paragraphs])

def parse_resume_file(file: UploadFile) -> str:
    filename = file.filename.lower()
    if filename.endswith(".pdf"):
        return extract_text_from_pdf(file)
    elif filename.endswith(".docx"):
        return extract_text_from_docx(file)
    else:
        raise ValueError("Unsupported file type. Only PDF and DOCX are supported.")
