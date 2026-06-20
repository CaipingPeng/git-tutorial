import sys
import re
from pathlib import Path
from html.parser import HTMLParser

sys.stdout.reconfigure(encoding='utf-8')

class GitTutorialParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_content = False
        self.current_tag = None
        self.text_parts = []
        self.section_title = None
        
    def handle_starttag(self, tag, attrs):
        if tag in ['h2', 'h3', 'p', 'pre', 'code', 'li', 'strong']:
            self.current_tag = tag
            self.in_content = True
    
    def handle_endtag(self, tag):
        if tag == self.current_tag:
            self.in_content = False
            if self.current_tag in ['h2', 'h3']:
                if self.text_parts:
                    self.text_parts.append('\n')
            elif self.current_tag == 'p':
                self.text_parts.append('\n\n')
    
    def handle_data(self, data):
        if self.in_content and data.strip():
            self.text_parts.append(data.strip())
    
    def get_text(self):
        return ' '.join(self.text_parts)

def extract_gittutorial():
    script_dir = Path(__file__).parent
    content_dir = script_dir / "gittutorial_content"
    
    for html_file in content_dir.glob("*.html"):
        print(f"\n=== 分析 {html_file.name} ===\n")
        
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        parser = GitTutorialParser()
        parser.feed(html_content)
        text = parser.get_text()
        
        # Extract key sections
        sections = {
            'NAME': r'NAME\s+(.*?)(?=SYNOPSIS|$)',
            'DESCRIPTION': r'DESCRIPTION\s+(.*?)(?=IMPORTING|MANAGING|SEE ALSO|$)',
            'KEY_CONCEPTS': r'(object database|commit|branch|index|working tree|HEAD)',
        }
        
        for section_name, pattern in sections.items():
            match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
            if match:
                content = match.group(1) if match.lastindex else match.group(0)
                print(f"## {section_name}")
                print(content[:500] + '...\n' if len(content) > 500 else content + '\n')
        
        # Save full text
        output_file = content_dir / f"{html_file.stem}_extracted.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)
        
        print(f"完整文本已保存: {output_file.name} ({len(text)} 字符)")

if __name__ == "__main__":
    extract_gittutorial()
