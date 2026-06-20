import fitz  # PyMuPDF
import sys
from pathlib import Path

# Fix console encoding
sys.stdout.reconfigure(encoding='utf-8')

def analyze_progit():
    script_dir = Path(__file__).parent
    pdf_path = script_dir.parent / "referencesBook" / "progit.pdf"
    
    if not pdf_path.exists():
        print(f"PDF not found: {pdf_path}")
        return
    
    doc = fitz.open(pdf_path)
    
    print("=== Pro Git PDF 完整分析 ===\n")
    print(f"总页数: {len(doc)}")
    print(f"作者: {doc.metadata.get('author', 'N/A')}")
    print(f"版本: {doc.metadata.get('title', 'N/A')}")
    print(f"创建日期: {doc.metadata.get('creationDate', 'N/A')}\n")
    
    # Extract full TOC
    toc = doc.get_toc()
    print("=== 完整目录结构 ===")
    for level, title, page in toc:
        indent = "  " * (level - 1)
        print(f"{indent}{title} (第{page}页)")
    
    # Count images per chapter
    print(f"\n=== 图片分布统计 ===")
    image_count = 0
    pages_with_images = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        images = page.get_images()
        if images:
            image_count += len(images)
            pages_with_images.append((page_num + 1, len(images)))
    
    print(f"总图片数: {image_count}")
    print(f"含图片页数: {len(pages_with_images)}")
    
    # Save detailed chapter text samples
    output_dir = script_dir / "progit_analysis"
    output_dir.mkdir(exist_ok=True)
    
    # Extract key chapters for analysis
    key_chapters = [
        (16, 31, "Chapter 1: Getting Started"),
        (32, 68, "Chapter 2: Git Basics"),
        (69, 110, "Chapter 3: Git Branching"),
        (132, 171, "Chapter 5: Distributed Git"),
        (172, 236, "Chapter 6: GitHub"),
        (237, 300, "Chapter 7: Git Tools"),
        (301, 360, "Chapter 8: Customizing Git"),
        (361, 412, "Chapter 9: Git and Other Systems"),
        (413, 458, "Chapter 10: Git Internals"),
    ]
    
    for start_page, end_page, chapter_name in key_chapters:
        chapter_text = ""
        for page_num in range(start_page - 1, min(end_page, len(doc))):
            page = doc[page_num]
            chapter_text += page.get_text()
        
        # Save chapter text
        safe_name = chapter_name.replace(":", "").replace(" ", "_")
        output_file = output_dir / f"{safe_name}.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(chapter_text)
        
        print(f"已提取: {chapter_name} ({end_page - start_page + 1}页, {len(chapter_text)}字符)")
    
    doc.close()
    print(f"\n分析完成。章节文本已保存到: {output_dir}")

if __name__ == "__main__":
    analyze_progit()
