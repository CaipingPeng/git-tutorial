import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

def fix_whitespace():
    repo_root = Path(__file__).parent.parent
    md_files = list(repo_root.glob("*.md"))
    
    for md_file in md_files:
        with open(md_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        # Remove trailing whitespace
        lines = [line.rstrip() + '\n' for line in lines]
        
        # Remove trailing blank lines at EOF
        while lines and lines[-1].strip() == '':
            lines.pop()
        
        # Ensure single newline at EOF
        if lines and not lines[-1].endswith('\n'):
            lines[-1] += '\n'
        
        with open(md_file, "w", encoding="utf-8", newline='\n') as f:
            f.writelines(lines)
        
        print(f"[OK] {md_file.name}")

if __name__ == "__main__":
    fix_whitespace()
