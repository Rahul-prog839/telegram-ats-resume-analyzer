from docx import Document


def extract_docx_text(path):

    doc = Document(path)

    text = []

    for p in doc.paragraphs:
        text.append(p.text)

    return "\n".join(text)