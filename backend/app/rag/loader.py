from pathlib import Path
from pypdf import PdfReader
from docx import Document


def load_document(file_path: str):
    path = Path(file_path)

    if path.suffix.lower() == ".pdf":
        return load_pdf(path)

    if path.suffix.lower() == ".docx":
        return load_docx(path)

    if path.suffix.lower() == ".txt":
        text = path.read_text(encoding="utf-8")

        return [{
            "text": text,
            "source": path.name,
            "page": None
        }]

    raise ValueError(f"Unsupported file type: {path.suffix}")


def load_pdf(path: Path):
    reader = PdfReader(str(path))

    pages = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()

        if text and text.strip():
            pages.append({
                "text": text,
                "source": path.name,
                "page": page_number
            })

    return pages


def load_docx(path: Path):
    document = Document(str(path))

    text = "\n\n".join(
        paragraph.text
        for paragraph in document.paragraphs
        if paragraph.text.strip()
    )

    return [{
        "text": text,
        "source": path.name,
        "page": None
    }]