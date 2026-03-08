# backend/app/routes/analyzer.py

from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.services.pdf_parser import extract_text_from_pdf
from app.services.resume_analyzer import analyze_resume
from app.schemas.response_schema import AnalysisResponse

router = APIRouter()

@router.post("/analyze", response_model=AnalysisResponse)
async def analyze_resume_route(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    if not resume.filename or not resume.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF resumes are allowed.")

    try:
        resume_text = extract_text_from_pdf(resume.file)

        if not resume_text.strip():
            raise HTTPException(status_code=400, detail="Could not extract text from the uploaded PDF.")

        result = analyze_resume(resume_text, job_description)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error analyzing resume: {str(e)}")