import fitz  # PyMuPDF
from pathlib import Path
from PIL import Image
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')

def extract_images_from_progit():
    script_dir = Path(__file__).parent
    pdf_path = script_dir.parent / "referencesBook" / "progit.pdf"
    output_dir = script_dir.parent / "assets" / "progit"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    doc = fitz.open(pdf_path)
    
    # Key pages with valuable diagrams
    target_pages = [
        (17, "local-vcs"),
        (18, "centralized-vcs"),
        (19, "distributed-vcs"),
        (21, "deltas"),
        (23, "snapshots"),
        (25, "file-status-lifecycle"),
        (70, "commit-and-tree"),
        (71, "commits-and-parents"),
        (72, "branch-and-history"),
        (73, "two-branches"),
        (74, "head-to-branch"),
        (75, "advance-master"),
        (76, "checkout-testing"),
        (77, "divergent-history"),
        (78, "basic-branching-1"),
        (79, "basic-branching-2"),
        (80, "basic-branching-3"),
        (81, "basic-branching-4"),
        (82, "basic-branching-5"),
        (83, "basic-branching-6"),
        (92, "remote-branches-1"),
        (93, "remote-branches-2"),
        (94, "remote-branches-3"),
        (95, "remote-branches-4"),
        (96, "remote-branches-5"),
        (102, "simple-rebase-1"),
        (103, "simple-rebase-2"),
        (104, "simple-rebase-3"),
        (105, "interesting-rebase-1"),
        (106, "interesting-rebase-2"),
        (258, "reset-workflow"),
        (259, "reset-soft"),
        (260, "reset-mixed"),
        (261, "reset-hard"),
        (422, "data-model-1"),
        (423, "data-model-2"),
        (424, "data-model-3"),
    ]
    
    extracted = []
    
    for page_num, img_name in target_pages:
        if page_num > len(doc):
            continue
            
        page = doc[page_num - 1]
        images = page.get_images()
        
        if not images:
            continue
        
        xref = images[0][0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        
        img = Image.open(io.BytesIO(image_bytes))
        width, height = img.size
        
        if width < 100 or height < 100:
            continue
        
        aspect = width / height
        if aspect > 5 or aspect < 0.2:
            continue
        
        output_path = output_dir / f"{img_name}.{image_ext}"
        with open(output_path, "wb") as f:
            f.write(image_bytes)
        
        extracted.append((page_num, img_name, width, height))
        print(f"[OK] Page {page_num}: {img_name}.{image_ext} ({width}x{height})")
    
    doc.close()
    
    print(f"\n提取完成: {len(extracted)} 张图片")
    print(f"输出目录: {output_dir}")
    
    manifest_path = output_dir / "manifest.txt"
    with open(manifest_path, "w", encoding="utf-8") as f:
        f.write("Pro Git 图片清单\n")
        f.write("=" * 50 + "\n\n")
        for page_num, img_name, width, height in extracted:
            f.write(f"Page {page_num}: {img_name} ({width}x{height})\n")
    
    print(f"清单已保存: {manifest_path}")

if __name__ == "__main__":
    extract_images_from_progit()
