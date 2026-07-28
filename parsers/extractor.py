import os

from parsers.pdf_parser import extract_pdf_text
from parsers.docx_parser import extract_docx_text


def extract_text(file_path):

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        return extract_pdf_text(file_path)

    elif extension == ".docx":
        return extract_docx_text(file_path)

    else:
        raise ValueError("Unsupported File")