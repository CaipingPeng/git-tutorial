# 03. 日常工作流 ⭐

> 15 分钟掌握 Git 的核心操作,覆盖 80% 日常场景

这是整个基础教程最重要的一章。掌握这章,你就能独立使用 Git 了。

## Git 的工作循环

日常使用 Git 就是不断重复这个循环:

```
┌─────────────────────────────────────┐
│                                     │
│  1. 修改代码                         │
│  2. git status   (看看改了什么)      │
│  3. git add      (选择要提交的)      │
│  4. git commit   (提交)             │
│  5. git push     (推送到远程)        │
│                                     │
└─────────────────────────────────────┘
```

## 核心命令:status → add → commit → push

### git status: 随时查看状态

这是你用得最多的命令。

```bash
git status
```

**输出示例**:
```
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   index.html

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        style.css

no changes added to commit (use "git add" and/or "git commit -a")
```

**怎么看这个输出?**
- `modified: index.html`: 已跟踪的文件被修改了
- `Untracked files: style.css`: 新文件,还没被 Git 跟踪
- 括号里的提示告诉你下一步该做什么

**记住**: 不确定时就 `git status`,它会告诉你当前状态和下一步怎么做。

### git add: 选择要提交的改动

```bash
git add 文件名
```

**常用方式**:

```bash
# 添加单个文件
git add index.html

# 添加多个文件
git add index.html style.css

# 添加当前目录所有改动
git add .

# 添加所有改动 (包括删除)
git add -A
```

**为什么要 add?**

Git 不会自动提交所有改动,你需要明确告诉它"我要提交这些"。

这样的好处:
- 可以只提交一部分改动
- 可以分多次提交,每次提交一个功能
- 提交历史更清晰

### git commit: 提交改动

```bash
git commit -m "提交信息"
```

**示例**:
```bash
git commit -m "Add homepage header"
git commit -m "Fix login button style"
git commit -m "Update README"
```

**提交信息怎么写?**

✅ 好的提交信息:
- `Add user login feature`
- `Fix null pointer exception in UserService`
- `Update documentation for API v2`

❌ 差的提交信息:
- `update` (太模糊)
- `fix bug` (哪个bug?)
- `work in progress` (还没完成就不要提交)

**原则**: 用一句话说清楚这次改了什么。

### git commit -a: 快捷提交

如果只是修改已跟踪的文件(没有新文件),可以跳过 `add`:

```bash
git commit -a -m "提交信息"
```

等价于:
```bash
git add 所有已跟踪的修改文件
git commit -m "提交信息"
```

**注意**: `-a` 不会添加新文件,只处理修改和删除。

### git push: 推送到远程

```bash
git push
```

如果是第一次推送,需要:
```bash
git push -u origin main
```

**发生了什么?**
- 把本地提交推送到远程仓库(如 GitHub)
- 其他人可以看到你的改动
- `-u` 设置上游分支,以后就不用每次都写 `origin main` 了

## 完整示例:从修改到推送

**场景**: 你修改了首页,想提交并推送。

```bash
# 1. 先看看状态
git status
# 输出: modified: index.html

# 2. 添加到暂存区
git add index.html

# 3. 再看看状态 (确认一下)
git status
# 输出: Changes to be committed: modified: index.html

# 4. 提交
git commit -m "Update homepage title"
# 输出: [main a1b2c3d] Update homepage title
#  1 file changed, 2 insertions(+), 1 deletion(-)

# 5. 推送到远程
git push
# 输出: To github.com:user/repo.git
#    a1b2c3d..e4f5g6h  main -> main
```

完成!

## 查看历史

### git log: 查看提交历史

```bash
git log
```

**输出示例**:
```
commit e4f5g6h7i8j9k0l1m2n3o4p5q6r7s8t9u0v1w2x3
Author: Alice <alice@example.com>
Date:   Mon Jan 15 10:30:00 2024 +0800

    Update homepage title

commit a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0
Author: Alice <alice@example.com>
Date:   Mon Jan 15 09:00:00 2024 +0800

    Initial commit
```

**更简洁的方式**:
```bash
git log --oneline
```

输出:
```
e4f5g6h Update homepage title
a1b2c3d Initial commit
```

**图形化显示**:
```bash
git log --oneline --graph --all
```

### git show: 查看具体改动

```bash
# 查看最近一次提交的详细改动
git show

# 查看特定提交
git show a1b2c3d
```

输出包括:
- 提交信息
- 作者和时间
- 具体改了哪些行

### git diff: 查看未提交的改动

```bash
# 查看工作目录的改动
git diff

# 查看暂存区的改动
git diff --staged
```

**实战用法**:
```bash
# 修改了几个文件
vim index.html style.css

# 想看看改了什么
git diff

# 觉得ok,提交
git add .
git commit -m "Update styles"
```

## 常见场景速查

### 场景1: 修改一个文件并提交

```bash
vim file.txt
git add file.txt
git commit -m "Update file"
git push
```

### 场景2: 修改多个文件,分别提交

```bash
# 修改了 A.txt 和 B.txt
vim A.txt B.txt

# 先提交 A
git add A.txt
git commit -m "Update A"

# 再提交 B
git add B.txt
git commit -m "Update B"

# 一起推送
git push
```

### 场景3: 快速提交所有改动

```bash
# 修改了很多已跟踪的文件
git commit -a -m "Batch update"
git push
```

### 场景4: 提交信息写错了

```bash
# 刚提交完,发现信息写错了
git commit --amend -m "正确的提交信息"
```

**注意**: 只能改最后一次提交,且只在还没 push 前用。

### 场景5: 忘记添加某个文件

```bash
# 提交了,发现忘了添加某个文件
git add 忘记的文件.txt
git commit --amend --no-edit

# --no-edit 表示不修改提交信息
```

## 工作流程图

```
工作目录              暂存区              本地仓库            远程仓库
  (编辑)              (准备)              (提交)              (GitHub)
                    
  修改文件
     │
     │ git add
     ├──────────→   暂存改动
     │                  │
     │                  │ git commit
     │                  ├──────────→   提交保存
     │                  │                  │
     │                  │                  │ git push
     │                  │                  ├──────────→   推送到远程
     │                  │                  │
     │ git restore      │                  │
     │←──────────       │                  │
     │                  │                  │
     │                  │ git restore --staged
     │                  │←──────────       │
```

## 你只需要记住这 3 点

1. **核心循环**: status → add → commit → push
2. **status 是导航**: 不确定时就运行 `git status`
3. **提交要明确**: 用清晰的信息描述这次改了什么

## 练习

1. 创建一个新仓库,添加几个文件
2. 修改文件,用 `git status` 查看状态
3. 用 `git add` 和 `git commit` 提交
4. 用 `git log` 查看历史
5. 再修改文件,重复以上流程

## 下一步

掌握了基本工作流,接下来学习分支:

→ [分支基础](04-branching.md) - 15分钟学会并行开发

---

**小贴士**:
- `git status` 永远是你的朋友,有疑问先运行它
- 提交要频繁,一个小功能就提交一次
- 提交信息要清楚,方便以后查找
- push 前先确保代码可以运行
