import requests
from bs4 import BeautifulSoup
import time
from pathlib import Path
import sys
from urllib.parse import urljoin, urlparse
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

class SmartGitDocsCrawler:
    def __init__(self, base_url="https://git-scm.com/docs", output_dir="git_docs_latest"):
        self.base_url = base_url
        self.output_dir = Path(__file__).parent / output_dir
        self.output_dir.mkdir(exist_ok=True)
        self.visited = set()
        
    def is_latest_english_doc(self, url):
        """只保留最新版本的英文文档"""
        parsed = urlparse(url)
        path = parsed.path
        
        # 排除带版本号的URL
        if re.search(r'/\d+\.\d+\.\d+', path):
            return False
        
        # 排除非英文版本
        if re.search(r'/(zh_|ja|fr|pt_|sv|ru|uk|vi)', path):
            return False
        
        # 只保留 /docs/ 下的文档
        if not path.startswith('/docs/'):
            return False
            
        return True
    
    def fetch_page(self, url):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=15)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"✗ 获取失败: {url} - {e}")
            return None
    
    def extract_doc_links(self, html, current_url):
        """提取页面中的文档链接"""
        soup = BeautifulSoup(html, 'html.parser')
        links = set()
        
        for link in soup.find_all('a', href=True):
            href = link['href']
            full_url = urljoin(current_url, href).split('#')[0]
            
            if self.is_latest_english_doc(full_url) and full_url not in self.visited:
                links.add(full_url)
                
        return links
    
    def save_doc(self, url, html):
        soup = BeautifulSoup(html, 'html.parser')
        
        # 提取文档名称
        doc_name = urlparse(url).path.strip('/').replace('docs/', '').replace('/', '_')
        if not doc_name:
            doc_name = "index"
        
        # 提取标题
        title = soup.find('title')
        title_text = title.text if title else doc_name
        
        # 提取主要内容
        main_content = soup.find('div', {'id': 'main'}) or soup.find('body')
        
        # 保存为文本
        output_file = self.output_dir / f"{doc_name}.txt"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"URL: {url}\n")
            f.write(f"Title: {title_text}\n")
            f.write("=" * 80 + "\n\n")
            
            if main_content:
                text = main_content.get_text(separator='\n', strip=True)
                f.write(text[:100000])  # 限制长度
        
        return doc_name
    
    def crawl(self):
        print(f"开始爬取 Git 官方文档 (仅最新英文版): {self.base_url}\n")
        
        # 首先获取主页
        html = self.fetch_page(self.base_url)
        if not html:
            return
        
        # 提取所有文档链接
        to_visit = self.extract_doc_links(html, self.base_url)
        print(f"发现 {len(to_visit)} 个文档链接\n")
        
        crawled = 0
        
        while to_visit:
            url = to_visit.pop()
            
            if url in self.visited:
                continue
            
            crawled += 1
            print(f"[{crawled}] 爬取: {url}")
            
            html = self.fetch_page(url)
            if not html:
                continue
            
            # 保存文档
            doc_name = self.save_doc(url, html)
            self.visited.add(url)
            print(f"  ✓ 已保存: {doc_name}.txt")
            
            # 提取新链接
            new_links = self.extract_doc_links(html, url)
            for link in new_links:
                if link not in self.visited:
                    to_visit.add(link)
            
            time.sleep(0.3)
        
        # 保存URL列表
        urls_file = self.output_dir / "doc_list.json"
        with open(urls_file, 'w', encoding='utf-8') as f:
            json.dump(sorted(list(self.visited)), f, indent=2)
        
        print(f"\n完成! 共爬取 {crawled} 个文档")
        print(f"保存位置: {self.output_dir}")
        
        # 列出所有文档
        print("\n爬取的文档:")
        docs = sorted([f.stem for f in self.output_dir.glob("*.txt")])
        for doc in docs:
            print(f"  • {doc}")
        
        return crawled

if __name__ == "__main__":
    crawler = SmartGitDocsCrawler()
    crawler.crawl()
