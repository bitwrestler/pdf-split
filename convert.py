import argparse
import sys
import pymupdf
from pathlib import Path

# Parse command-line arguments
parser = argparse.ArgumentParser(
    description="Convert each page of a PDF to a PNG image.",
    usage="%(prog)s input_pdf",
)
parser.add_argument("input_pdf", type=Path, help="Path to the input PDF file")

if len(sys.argv) == 1:
    parser.print_usage()
    sys.exit(1)

args = parser.parse_args()

# Load the PDF
input_path = args.input_pdf
doc = pymupdf.open(input_path)

output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

# Loop through every page and save as an image
for i, page in enumerate(doc):
  pix = page.get_pixmap(dpi=300)  # High resolution 300 DPI
  pix.save(output_dir / f"{input_path.stem}_page_{i+1:02d}.png")

doc.close()

