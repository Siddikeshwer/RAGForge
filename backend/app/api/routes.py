from pathlib import Path

from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel

from app.rag.ingest import DocumentIngestor
from app.rag.rag_pipeline import RAGPipeline


router = APIRouter()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

ingestor = DocumentIngestor()
rag = RAGPipeline()


class QuestionRequest(BaseModel):
    question: str


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    allowed_types = {
        ".pdf",
        ".docx",
        ".txt"
    }

    extension = Path(file.filename).suffix.lower()

    if extension not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail="Only PDF, DOCX and TXT files are supported."
        )

    file_path = UPLOAD_DIR / file.filename

    contents = await file.read()

    file_path.write_bytes(contents)

    try:
        result = ingestor.ingest(str(file_path))

        return {
            "message": "Document uploaded successfully",
            "file": result["file"],
            "chunks": result["chunks"]
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.post("/ask")
async def ask_question(request: QuestionRequest):

    if not request.question.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    try:
        result = rag.ask(request.question)

        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )