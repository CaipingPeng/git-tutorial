import requests
from bs4 import BeautifulSoup
import time
from pathlib import Path
import sys
from urllib.parse import urljoin, urlparse
import json

sys.stdout.reconfigure(encoding='utf-8')

class GitDocsRecursiveCrawler:
    def __init__(self, base_url="https://git-scm.com/docs", output_dir="git_official_docs_full"):
        self.base_url = base_url
        self.domain = "git-scm.com"
        self.output_dir = Path(__file__).parent / output_dir
        self.output_dir.mkdir(exist_ok=True)
        self.visited = set()
        self.to_visit = set([base_url])
        
    def is_valid_url(self, url):
        """检查URL是否属于文档页面"""
        parsed = urlparse(url)
        return (
            parsed.netloc == self.domain and
            parsed.path.startswith('/docs/') and
            not parsed.path.endswith('.pdf') and
            not parsed.path.endswith('.zip')
        )
    
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
    
    def extract_links(self, html, current_url):
        """提取页面中的所有文档链接"""
        soup = BeautifulSoup(html, 'html.parser')
        links = set()
        
        for link in soup.find_all('a', href=True):
            href = link['href']
            full_url = urljoin(current_url, href)
            
            # 去除fragment
            full_url = full_url.split('#')[0]
            
            if self.is_valid_url(full_url) and full_url not in self.visited:
                links.add(full_url)
                
        return links
    
    def save_doc(self, url, html):
        soup = BeautifulSoup(html, 'html.parser')
        
        # 提取文档名称
        doc_name = urlparse(url).path.strip('/').replace('/', '_')
        if not doc_name or doc_name == 'docs':
            doc_name = "index"
        
        # 提取标题
        title = soup.find('title')
        title_text = title.text if title else doc_name
        
        # 提取主要内容
        main_content = soup.find('div', {'id': 'main'}) or soup.find('article') or soup.find('body')
        
        # 保存为文本文件
        output_file = self.output_dir / f"{doc_name}.txt"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"URL: {url}\n")
            f.write(f"Title: {title_text}\n")
            f.write("=" * 80 + "\n\n")
            
            if main_content:
                # 提取所有文本内容
                text = main_content.get_text(separator='\n', strip=True)
                # 限制长度避免文件过大
                f.write(text[:50000])
        
        return doc_name
    
    def crawl(self, max_pages=200):
        print(f"开始递归爬取 Git 官方文档: {self.base_url}\n")
        print(f"最大页面数: {max_pages}\n")
        
        crawled = 0
        
        while self.to_visit and crawled < max_pages:
            url = self.to_visit.pop()
            
            if url in self.visited:
                continue
            
            print(f"[{crawled+1}/{max_pages}] 爬取: {url}")
            
            html = self.fetch_page(url)
            if not html:
                continue
            
            # 保存文档
            doc_name = self.save_doc(url, html)
            self.visited.add(url)
            crawled += 1
            print(f"  ✓ 已保存: {doc_name}.txt")
            
            # 提取新链接
            new_links = self.extract_links(html, url)
            self.to_visit.update(new_links)
            
            if new_links:
                print(f"  → 发现 {len(new_links)} 个新链接")
            
            time.sleep(0.5)  # 避免请求过快
        
        # 保存已访问URL列表
        urls_file = self.output_dir / "all_urls.json"
        with open(urls_file, 'w', encoding='utf-8') as f:
            json.dump(sorted(list(self.visited)), f, indent=2)
        
        print(f"\n完成! 共爬取 {crawled} 个文档")
        print(f"保存位置: {self.output_dir}")
        print(f"URL列表: {urls_file}")
        
        return crawled

if __name__ == "__main__":
    crawler = GitDocsRecursiveCrawler()
    crawler.crawl(max_pages=200)
