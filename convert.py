import sys
import fitz  # PyMuPDF
from pathlib import Path

# Load the PDF
input_path = Path(sys.argv[1])
doc = fitz.open(input_path)

# Loop through every page and save as an image
for i, page in enumerate(doc):
  pix = page.get_pixmap(dpi=300)  # High resolution 300 DPI
  pix.save(f"{input_path.stem}_page_{i+1}.png")

doc.close()

