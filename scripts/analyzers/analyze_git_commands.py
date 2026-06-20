import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

def analyze_git_commands():
    file_path = Path(r"C:\Users\Administrator\Desktop\git学习\git-tutorial\referencesBook\Complete list of all commands.md")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract commands with descriptions
    pattern = r'\[git-(\w+(?:-\w+)*)\[1\]\].*?\n\s*>\s*(.+?)(?=\n\s*\[|$)'
    matches = re.findall(pattern, content, re.DOTALL)
    
    commands = {}
    for cmd, desc in matches:
        desc_clean = desc.strip().replace('\n', ' ')[:100]
        commands[cmd] = desc_clean
    
    print(f"提取到 {len(commands)} 个 Git 命令\n")
    
    # Define categories based on actual Git documentation
    categories = {
        '核心日常命令': [
            'add', 'status', 'commit', 'diff', 'log', 'show',
            'branch', 'checkout', 'switch', 'merge', 'tag',
            'fetch', 'pull', 'push', 'clone', 'remote',
            'rm', 'mv', 'grep', 'init'
        ],
        '撤销与恢复': [
            'restore', 'reset', 'revert', 'reflog', 'checkout'
        ],
        '暂存与保存': [
            'stash', 'cherry-pick'
        ],
        '历史查询': [
            'log', 'show', 'diff', 'bisect', 'blame', 'grep',
            'describe', 'shortlog', 'show-branch'
        ],
        '分支与合并': [
            'branch', 'checkout', 'switch', 'merge', 'mergetool',
            'rebase', 'difftool'
        ],
        '远程协作': [
            'clone', 'fetch', 'pull', 'push', 'remote',
            'ls-remote', 'show-ref'
        ],
        '补丁与邮件': [
            'format-patch', 'send-email', 'request-pull', 'am', 'apply'
        ],
        '高级操作': [
            'rebase', 'filter-branch', 'submodule', 'worktree',
            'notes', 'range-diff'
        ],
        '仓库维护': [
            'gc', 'fsck', 'prune', 'reflog', 'clean',
            'archive', 'bundle'
        ],
        '配置与帮助': [
            'config', 'help', 'version'
        ],
        '底层命令 (Plumbing)': [
            'cat-file', 'hash-object', 'ls-files', 'ls-tree',
            'show-ref', 'update-ref', 'read-tree', 'write-tree',
            'commit-tree', 'merge-base', 'rev-parse', 'rev-list'
        ]
    }
    
    # Check what's in official list
    print("=== 官方命令分类检查 ===\n")
    
    for category, cmd_list in categories.items():
        print(f"\n{category} ({len(cmd_list)} 个):")
        found = 0
        for cmd in cmd_list:
            if cmd in commands:
                found += 1
                print(f"  ✓ git {cmd:20} - {commands[cmd][:60]}")
            else:
                print(f"  ✗ git {cmd:20} - (未在官方列表找到)")
        print(f"  覆盖率: {found}/{len(cmd_list)}")
    
    # Find useful commands not in common categories
    print("\n\n=== 可能被忽略的实用命令 ===\n")
    
    common_set = set()
    for cmd_list in categories.values():
        common_set.update(cmd_list)
    
    interesting = []
    keywords = ['merge', 'diff', 'show', 'log', 'commit', 'branch', 'remote', 'tag']
    
    for cmd, desc in commands.items():
        if cmd not in common_set:
            for keyword in keywords:
                if keyword in cmd or keyword in desc.lower():
                    interesting.append((cmd, desc))
                    break
    
    for cmd, desc in sorted(interesting)[:15]:
        print(f"• git {cmd:25} - {desc[:70]}")
    
    print("\n\n=== 教程优化建议 ===\n")
    
    recommendations = {
        '第03章 (基础操作)': {
            '新增': ['git notes (给提交添加注释)', 'git show (查看对象详情)'],
            '说明': '这两个命令能丰富日常工作流'
        },
        '第05章 (合并与冲突)': {
            '新增': ['git difftool (外部差异工具)', 'git mergetool (外部合并工具)'],
            '说明': '很多人更喜欢用 GUI 工具解决冲突'
        },
        '第06章 (远程协作)': {
            '新增': ['git ls-remote (查看远程引用)', 'git show-ref (查看本地引用)'],
            '说明': '调试远程分支问题时很有用'
        },
        '第11章 (历史查询)': {
            '新增': ['git describe (用标签描述提交)', 'git shortlog (汇总日志)', 'git show-branch (分支树)'],
            '说明': '这些是官方推荐的查询命令'
        },
        '第15章 (配置与工具)': {
            '新增': ['difftool/mergetool 配置', 'GPG 签名 (commit -S, tag -s)', 'verify-commit/verify-tag'],
            '说明': '安全和工具集成'
        },
        '新增章节建议': {
            '新增': ['git range-diff (对比补丁系列)', 'git worktree (多工作目录)', 'git notes 的团队使用'],
            '说明': '这些是高级但实用的功能'
        }
    }
    
    for chapter, info in recommendations.items():
        print(f"\n{chapter}:")
        print(f"  建议: {info['说明']}")
        for item in info['新增']:
            print(f"    • {item}")

if __name__ == "__main__":
    analyze_git_commands()
