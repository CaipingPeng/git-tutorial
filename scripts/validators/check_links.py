import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

def check_markdown_links():
    repo_root = Path(__file__).parent.parent
    md_files = list(repo_root.glob("*.md"))
    
    issues = []
    
    for md_file in md_files:
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Check image links
        img_pattern = r'!\[.*?\]\((.*?)\)'
        for match in re.finditer(img_pattern, content):
            img_path = match.group(1)
            if not img_path.startswith('http'):
                full_path = repo_root / img_path.lstrip('./')
                if not full_path.exists():
                    issues.append(f"{md_file.name}: 图片不存在 {img_path}")
        
        # Check markdown links
        link_pattern = r'\[.*?\]\((\.\/.*?\.md.*?)\)'
        for match in re.finditer(link_pattern, content):
            link_path = match.group(1).split('#')[0].split('?')[0]
            full_path = repo_root / link_path.lstrip('./')
            if not full_path.exists():
                issues.append(f"{md_file.name}: 链接不存在 {link_path}")
    
    if issues:
        print("发现问题:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("[OK] 所有链接和图片路径检查通过")
    
    return len(issues) == 0

if __name__ == "__main__":
    check_markdown_links()
