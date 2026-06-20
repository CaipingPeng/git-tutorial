import sys
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

def fetch_gittutorial():
    urls = [
        'https://git-scm.com/docs/gittutorial',
        'https://git-scm.com/docs/gittutorial-2',
    ]
    
    output_dir = Path(__file__).parent / "gittutorial_content"
    output_dir.mkdir(exist_ok=True)
    
    for url in urls:
        try:
            print(f"正在获取: {url}")
            headers = {'User-Agent': 'Mozilla/5.0'}
            req = urllib.request.Request(url, headers=headers)
            response = urllib.request.urlopen(req, timeout=10)
            content = response.read().decode('utf-8')
            
            filename = url.split('/')[-1] + '.html'
            output_path = output_dir / filename
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✓ 已保存: {filename} ({len(content)} 字符)")
        except Exception as e:
            print(f"✗ 获取失败: {url} - {e}")
    
    print(f"\n内容已保存到: {output_dir}")

if __name__ == "__main__":
    fetch_gittutorial()
