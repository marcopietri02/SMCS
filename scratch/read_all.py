import os
from pypdf import PdfReader

pdfs = [
    r"Ex\Descriptive Stats-20260317\Exercises-2_DesciptiveStats.pdf",
    r"Ex\Probability-20260317\Exercises-3_Probability.pdf",
    r"Ex\Discrete Random Variables-20260327\Exercises-4_DiscreteRV.pdf",
    r"Ex\Continuous Random Variables-20260327\Exercises-5_ContinuousRV.pdf"
]

out_txt = ""

for pdf in pdfs:
    out_txt += f"--- {os.path.basename(pdf)} ---\n"
    try:
        reader = PdfReader(pdf)
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                out_txt += text + "\n"
    except Exception as e:
        out_txt += f"Error reading: {e}\n"
    out_txt += "\n"

os.makedirs("scratch", exist_ok=True)
with open("scratch/all_ex.txt", "w", encoding="utf-8") as f:
    f.write(out_txt)
