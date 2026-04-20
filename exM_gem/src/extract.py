import os
from pypdf import PdfReader

def extract(pdf_path, txt_path):
    if not os.path.exists(pdf_path):
        return
    text = ""
    for p in PdfReader(pdf_path).pages:
        text += p.extract_text() + "\n"
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(text)

extract("Ex/SMCS_mock_test_1_2025-26.pdf", "mock_gem/src/mock.txt")
extract("argomenti_primo_parziale.pdf", "mock_gem/src/argomenti.txt")
