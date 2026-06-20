import requests
from bs4 import BeautifulSoup
import time
from pathlib import Path
import sys
from urllib.parse import urljoin, urlparse
import json

sys.stdout.reconfigure(encoding='utf-8')

class GitDocsCrawler:
    def __init__(self, base_url="https://git-scm.com/docs", output_dir="git_official_docs"):
        self.base_url = base_url
        self.output_dir = Path(__file__).parent / output_dir
        self.output_dir.mkdir(exist_ok=True)
        self.visited = set()
        self.doc_links = []
        
    def fetch_page(self, url):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"✗ 获取失败: {url} - {e}")
            return None
    
    def extract_doc_links(self, html, base_url):
        soup = BeautifulSoup(html, 'html.parser')
        links = []
        
        # 查找所有文档链接
        for link in soup.find_all('a', href=True):
            href = link['href']
            
            # Git 命令文档链接通常是 /docs/git-xxx 格式
            if href.startswith('/docs/git-'):
                full_url = urljoin(base_url, href)
                if full_url not in self.visited:
                    links.append(full_url)
                    
        return links
    
    def save_doc(self, url, html):
        soup = BeautifulSoup(html, 'html.parser')
        
        # 提取文档名称
        doc_name = urlparse(url).path.split('/')[-1]
        if not doc_name:
            doc_name = "index"
        
        # 提取主要内容
        content = {
            'url': url,
            'title': soup.find('title').text if soup.find('title') else doc_name,
            'content': []
        }
        
        # 提取文本内容
        main_content = soup.find('div', {'id': 'main'}) or soup.find('body')
        if main_content:
            # 提取段落
            for elem in main_content.find_all(['h1', 'h2', 'h3', 'h4', 'p', 'pre', 'code', 'li']):
                text = elem.get_text(strip=True)
                if text and len(text) > 10:
                    content['content'].append({
                        'tag': elem.name,
                        'text': text[:500]  # 限制长度
                    })
        
        # 保存为文本文件
        output_file = self.output_dir / f"{doc_name}.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"URL: {url}\n")
            f.write(f"Title: {content['title']}\n")
            f.write("=" * 80 + "\n\n")
            
            for item in content['content'][:50]:  # 限制条目数
                f.write(f"[{item['tag']}] {item['text']}\n\n")
        
        return doc_name
    
    def crawl(self, max_pages=50):
        print(f"开始爬取 Git 官方文档: {self.base_url}\n")
        
        # 获取主页
        html = self.fetch_page(self.base_url)
        if not html:
            print("无法获取主页")
            return
        
        # 提取所有文档链接
        self.doc_links = self.extract_doc_links(html, self.base_url)
        print(f"发现 {len(self.doc_links)} 个文档链接\n")
        
        # 保存链接列表
        links_file = self.output_dir / "doc_links.json"
        with open(links_file, 'w', encoding='utf-8') as f:
            json.dump(self.doc_links, f, indent=2)
        
        # 爬取文档 (限制数量)
        crawled = 0
        for url in self.doc_links[:max_pages]:
            if url in self.visited:
                continue
                
            print(f"[{crawled+1}/{min(max_pages, len(self.doc_links))}] 爬取: {url}")
            html = self.fetch_page(url)
            
            if html:
                doc_name = self.save_doc(url, html)
                self.visited.add(url)
                crawled += 1
                print(f"  ✓ 已保存: {doc_name}.txt")
            
            time.sleep(0.5)  # 避免请求过快
        
        print(f"\n完成! 共爬取 {crawled} 个文档")
        print(f"保存位置: {self.output_dir}")
        
        return crawled

if __name__ == "__main__":
    crawler = GitDocsCrawler()
    crawler.crawl(max_pages=50)  # 限制爬取50个页面
