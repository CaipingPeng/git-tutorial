import sys, os, io
sys.stdout.reconfigure(encoding="utf-8")
import pdfplumber
from PIL import Image

pdf_path = os.path.join("referencesBook",
    "Git in Practice (Includes 66 Techniques) (Mike McQuaid) (z-library.sk, 1lib.sk, z-lib.sk).pdf")
out_dir = "assets"
os.makedirs(out_dir, exist_ok=True)

image_pages = {
    204: "merge_rebase_compare"
}

with pdfplumber.open(pdf_path) as pdf:
    for pg, name in image_pages.items():
        page = pdf.pages[pg - 1]
        for i, img in enumerate(page.images):
            try:
                x0, top, x1, bottom = img["x0"], img["top"], img["x1"], img["bottom"]
                w, h = x1 - x0, bottom - top
                if w < 100 or h < 100:
                    continue
                stream = img["stream"]
                img_data = stream.get_data()
                pil_img = Image.open(io.BytesIO(img_data))
                ext = pil_img.format.lower() if pil_img.format else "png"
                fname = f"git-in-practice-{name}.{ext}"
                fpath = os.path.join(out_dir, fname)
                pil_img.save(fpath)
                print(f"Saved: {fpath} ({pil_img.size})")
            except Exception as e:
                print(f"Error page {pg}: {e}")
print("Done")
