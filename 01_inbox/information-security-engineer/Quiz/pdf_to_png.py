import fitz
import sys
import os

pdf_path = sys.argv[1]
start_page = int(sys.argv[2]) - 1
end_page = int(sys.argv[3]) - 1
out_dir = sys.argv[4]

os.makedirs(out_dir, exist_ok=True)
doc = fitz.open(pdf_path)
for i in range(start_page, end_page + 1):
    page = doc.load_page(i)
    pix = page.get_pixmap(dpi=150)
    pix.save(f"{out_dir}/page_{i+1}.png")
print("Done")
