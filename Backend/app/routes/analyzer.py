from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import StreamingResponse
import traceback

from app.services.pdf_parser import extract_text_from_pdf
from app.services.resume_analyzer import analyze_resume
from app.services.docx_exporter import build_resume_docx
from app.schemas.response_schema import AnalysisResponse

router = APIRouter()


@router.post("/analyze", response_model=AnalysisResponse)
async def analyze_resume_route(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    if not resume.filename or not resume.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF resumes are allowed.")

    try:
        resume_text = extract_text_from_pdf(resume.file)

        if not resume_text.strip():
            raise HTTPException(
                status_code=400,
                detail="Could not extract text from the uploaded PDF."
            )

        result = analyze_resume(resume_text, job_description)
        return result

    except HTTPException:
        raise
    except Exception as e:
        print("ANALYZE ROUTE ERROR:")
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail=f"Error analyzing resume: {str(e)}"
        )


@router.post("/export-docx")
async def export_resume_docx(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    if not resume.filename or not resume.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF resumes are allowed.")

    try:
        resume_text = extract_text_from_pdf(resume.file)

        if not resume_text.strip():
            raise HTTPException(
                status_code=400,
                detail="Could not extract text from the uploaded PDF."
            )

        analysis_result = analyze_resume(resume_text, job_description)
        optimized_resume_draft = analysis_result.get("optimized_resume_draft", {})

        file_stream = build_resume_docx(optimized_resume_draft)

        return StreamingResponse(
            file_stream,
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            headers={
                "Content-Disposition": "attachment; filename=optimized_resume.docx"
            }
        )

    except HTTPException:
        raise
    except Exception as e:
        print("EXPORT DOCX ERROR:")
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail=f"Error exporting resume: {str(e)}"
        )