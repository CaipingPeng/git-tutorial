import json
import sys
from pathlib import Path
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

def analyze_official_docs():
    docs_dir = Path(__file__).parent / "git_official_docs"
    
    # 读取文档列表
    with open(docs_dir / "doc_links.json", 'r') as f:
        doc_links = json.load(f)
    
    print(f"分析 {len(doc_links)} 个 Git 官方文档\n")
    print("=" * 80)
    
    # 统计已爬取的文档
    doc_files = list(docs_dir.glob("git-*.txt"))
    print(f"\n已爬取文档: {len(doc_files)} 个\n")
    
    # 分类分析
    categories = {
        '核心日常命令': [
            'git-init', 'git-clone', 'git-add', 'git-status', 'git-commit',
            'git-diff', 'git-log', 'git-show', 'git-rm', 'git-mv'
        ],
        '分支与合并': [
            'git-branch', 'git-checkout', 'git-switch', 'git-merge',
            'git-mergetool', 'git-rebase', 'git-difftool'
        ],
        '远程协作': [
            'git-fetch', 'git-pull', 'git-push', 'git-remote', 'git-clone'
        ],
        '撤销与恢复': [
            'git-restore', 'git-reset', 'git-revert', 'git-checkout'
        ],
        '历史查询': [
            'git-log', 'git-show', 'git-diff', 'git-bisect', 'git-blame',
            'git-grep', 'git-describe', 'git-shortlog'
        ],
        '暂存与保存': [
            'git-stash', 'git-cherry-pick', 'git-notes'
        ],
        '标签与版本': [
            'git-tag', 'git-describe'
        ],
        '补丁与邮件': [
            'git-format-patch', 'git-send-email', 'git-am', 'git-apply',
            'git-request-pull', 'git-imap-send'
        ],
        '高级功能': [
            'git-worktree', 'git-submodule', 'git-range-diff'
        ],
    }
    
    # 检查覆盖度
    print("各类别命令覆盖度:\n")
    
    available_docs = {f.stem for f in doc_files}
    
    for category, commands in categories.items():
        found = [cmd for cmd in commands if cmd in available_docs]
        print(f"{category} ({len(found)}/{len(commands)} 已爬取):")
        for cmd in commands:
            status = "✓" if cmd in available_docs else "✗"
            print(f"  {status} {cmd}")
        print()
    
    # 生成优化建议
    print("\n" + "=" * 80)
    print("基于官方文档的优化建议\n")
    
    recommendations = {
        '第03章 - 基础操作': [
            ('git-add', '完善 git add 的高级用法: 交互式暂存 (-i, -p)'),
            ('git-commit', '补充 commit 的高级选项: --amend, --fixup, --squash'),
            ('git-notes', '已添加,可进一步完善使用场景'),
            ('git-diff', '补充 diff 的输出格式和过滤选项'),
        ],
        '第04章 - 分支管理': [
            ('git-branch', '补充远程分支跟踪 (-u, --set-upstream-to)'),
            ('git-switch', '强调 switch vs checkout 的使用场景'),
            ('git-checkout', '区分 checkout 的三种用途: 切换分支/恢复文件/detached HEAD'),
        ],
        '第05章 - 合并与冲突': [
            ('git-merge', '补充合并策略: ours, theirs, octopus'),
            ('git-mergetool', '已添加,可补充更多工具配置'),
            ('git-difftool', '已添加,可补充 --dir-diff 用法'),
        ],
        '第06章 - 远程协作': [
            ('git-remote', '补充 remote 的重命名和 URL 修改'),
            ('git-fetch', '补充 --prune, --tags, --force 用法'),
            ('git-push', '补充 --force-with-lease, --set-upstream'),
        ],
        '第09章 - 撤销与恢复': [
            ('git-restore', '补充 --staged, --worktree, --source 用法'),
            ('git-reset', '已有详细讲解,可补充 --keep 模式'),
            ('git-revert', '补充 revert 合并提交 (-m 选项)'),
        ],
        '第10章 - 暂存与保存': [
            ('git-stash', '补充 stash 的高级用法: push, apply, pop, branch'),
            ('git-cherry-pick', '补充多提交 cherry-pick 和冲突处理'),
        ],
        '第11章 - 历史查询': [
            ('git-log', '补充 log 的格式化: --pretty, --format, --graph'),
            ('git-blame', '补充 -L 选项和忽略提交'),
            ('git-describe', '已添加,可补充 --dirty, --broken 用法'),
            ('git-shortlog', '已添加,完善'),
        ],
        '新增章节建议': [
            ('git-worktree', '独立章节: Git Worktree 多工作目录实战'),
            ('git-submodule', '独立章节或扩充第14章'),
            ('git-format-patch', '新增: 邮件工作流完整指南'),
            ('git-range-diff', '第11章: 对比补丁系列'),
        ]
    }
    
    for chapter, items in recommendations.items():
        print(f"\n{chapter}:")
        for cmd, desc in items:
            status = "✓" if f'git-{cmd.replace("git-", "")}' in available_docs else "✗"
            print(f"  {status} {cmd:20} - {desc}")
    
    # 输出统计摘要
    print("\n" + "=" * 80)
    print("\n统计摘要:")
    print(f"  • 发现官方文档链接: {len(doc_links)} 个")
    print(f"  • 成功爬取文档: {len(doc_files)} 个")
    print(f"  • 核心命令覆盖: {len(available_docs)} 个")
    print(f"  • 建议优化章节: {len(recommendations)} 个")

if __name__ == "__main__":
    analyze_official_docs()
