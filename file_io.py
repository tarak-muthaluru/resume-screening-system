# file_io.py
from pathlib import Path
import pdfplumber
from pdf2image import convert_from_path
import pytesseract

from cleaning import clean_text


def extract_pdf_text(path):
    """
    Extract text from PDF.
    Uses OCR fallback if text is not selectable.
    """
    path = Path(path)

    text = ""

    # 1) Try normal PDF text extraction
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += (page.extract_text() or "") + "\n"

    # 2) If very little text, assume scanned PDF → OCR
    if len(text.strip()) < 50:
        images = convert_from_path(str(path), dpi=200)
        ocr_text = []
        for img in images:
            ocr_text.append(pytesseract.image_to_string(img))
        text = "\n".join(ocr_text)

    # 3) Clean text
    return clean_text(text)

