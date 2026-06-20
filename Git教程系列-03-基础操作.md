# Git 基础操作

上一章你已经创建了一个 Git 仓库。现在仓库还只是一个"空档案柜"，里面没有任何正式版本。

这一章要学习 Git 最常用的一条工作流：

```text
改文件 → 看状态 → 加入暂存区 → 提交成版本 → 查看历史
```

对应命令是：

```bash
git status
git add 文件名
git commit -m "说明"
git log --oneline
```

先记住一句话：

> Git 不会自动把你所有修改都保存成版本。你要先选择哪些改动进入暂存区，再提交成正式版本。

---

## 学习建议

本章内容分为三个部分：

| 部分 | 内容 | 建议 |
|---|---|---|
| **第一部分：核心流程** ⭐ | status、add、commit、log、diff | **新手必读**，先跑通这部分 |
| **第二部分：日常必备** | restore、.gitignore、好提交习惯 | 掌握核心流程后再读 |
| **第三部分：进阶技巧** | add -p、commit --amend、diff --check | 可以先跳过，需要时再回来查 |

**新手优先级**：先把第一部分的命令跑通，能完成"改文件 → add → commit → 查看历史"这个循环，再回头看第二、三部分。

---

# 第一部分：核心流程 ⭐ 新手必读

## 1. 先确认你在 Git 仓库里

本章命令都应该在 Git 仓库的项目目录里运行。

先运行：

```bash
git status
```

如果看到类似：

```text
On branch main
No commits yet
nothing to commit
```

说明你在一个 Git 仓库里。

如果看到：

```text
fatal: not a git repository
```

说明你当前不在 Git 仓库里。你需要 `cd` 到有 `.git` 的项目目录，或者先运行 `git init` 初始化仓库。

---

## 2. 最小可用流程（4个命令就够）

如果你是第一次学，先只记住这4个命令：

```bash
git status              # 看当前状态
git add 文件名           # 选择要提交的改动
git commit -m "说明"     # 提交
git log --oneline       # 看历史
```

**这4个命令就能让你开始用 Git 管理版本。**

**快捷方式**（适用于已跟踪的文件）：

```bash
git commit -a -m "说明"  # 自动 add 所有已跟踪且修改的文件
```

`-a` 的意思是 "all tracked files"。它有两个重要限制：

1. **不会 add 新文件**（untracked files）
2. **不会 add 被 .gitignore 忽略的文件**

这意味着如果你：
- 创建了新文件 → 必须先 `git add 新文件`
- 想精确控制暂存哪些改动 → 不能用 `-a`

**什么时候用 `-a`**：

| 场景 | 用不用 `-a` |
|---|---|
| 只改了已有文件，想全部提交 | ✅ 可以用 `git commit -a` |
| 有新文件要提交 | ❌ 必须先 `git add 新文件` |
| 想只提交部分改动 | ❌ 不能用 `-a`，要手动 `git add` 选择 |

**推荐习惯**：新手阶段建议总是先 `git add`，再 `git commit`，这样更容易理解暂存区的作用。熟练后再根据情况使用 `-a` 快捷方式。

---

## 3. 创建第一个文件并提交

### 步骤1：创建文件

假设你在项目里新建一个文件 `hello.txt`，内容是：

```text
Hello Git
```

保存后运行：

```bash
git status
```

你可能看到：

```bash
On branch main

No commits yet

Untracked files:
  (use \"git add <file>...\" to include in what will be committed)
        hello.txt

nothing added to commit but untracked files present (use \"git add\" to track)
```

`Untracked files` 的意思是：

> 这个文件在文件夹里，但 Git 还没有把它纳入版本管理。

新文件默认不会自动进入 Git 历史。你要明确告诉 Git：这个文件我要管理。

### 步骤2：加入暂存区

运行：

```bash
git add hello.txt
```

这一步的意思不是"提交"，而是：

> 我准备把 `hello.txt` 放进下一次提交。

再看状态：

```bash
git status
```

你可能看到：

```text
On branch main

No commits yet

Changes to be committed:
  (use \"git rm --cached <file>...\" to unstage)
        new file:   hello.txt
```

这表示 `hello.txt` 已经进入暂存区，准备提交。

### 步骤3：提交

运行：

```bash
git commit -m \"first: 添加 hello.txt\"
```

`-m` 后面跟的是**提交说明**。这段话会和这次提交一起保存在历史里，以后你可以通过它快速了解这次改了什么。

提交成功后，你可能看到类似：

```text
[main (root-commit) a1b2c3d] first: 添加 hello.txt
 1 file changed, 1 insertion(+)
 create mode 100644 hello.txt
```

`a1b2c3d` 是这次提交的哈希值（实际会更长，这里显示缩写）。

### 步骤4：查看历史

运行：

```bash
git log --oneline
```

你会看到类似：

```text
a1b2c3d (HEAD -> main) first: 添加 hello.txt
```

这就是你的第一次提交。

---

## 4. 修改文件并再次提交

修改 `hello.txt`，加一行内容：

```text
Hello Git
This is a second line
```

保存后运行：

```bash
git status
```

你会看到：

```text
On branch main
Changes not staged for commit:
  (use \"git add <file>...\" to update what will be committed)
  (use \"git restore <file>...\" to discard changes in working directory)
        modified:   hello.txt

no changes added to commit (use \"git add\" and/or \"git commit -a\")
```

`modified` 表示这个文件被修改了，但还没有加入暂存区。

运行：

```bash
git add hello.txt
git commit -m \"update: 添加第二行\"
```

再查看历史：

```bash
git log --oneline
```

你会看到两次提交：

```text
b2c3d4e (HEAD -> main) update: 添加第二行
a1b2c3d first: 添加 hello.txt
```

**恭喜！你已经完成了 Git 的核心工作流。**

---

## 5. 查看具体改了什么：git diff

`git status` 告诉你哪些文件变了，`git diff` 告诉你具体哪几行变了。

### 查看未暂存的改动

修改 `hello.txt`，加第三行：

```text
Hello Git
This is a second line
Third line here
```

运行：

```bash
git diff
```

你会看到类似：

```diff
diff --git a/hello.txt b/hello.txt
index ...
--- a/hello.txt
+++ b/hello.txt
@@ -1,2 +1,3 @@
 Hello Git
 This is a second line
+Third line here
```

`+` 开头的行表示新增内容。`-` 开头的行表示删除内容（这里没有）。

### 查看已暂存的改动

如果你已经 `git add` 了：

```bash
git add hello.txt
git diff --staged
```

`--staged` 显示已经加入暂存区、即将提交的改动。

**常用组合**：

| 命令 | 查看什么 |
|---|---|
| `git diff` | 工作目录相对暂存区的改动（还没 add 的） |
| `git diff --staged` | 暂存区相对最后一次提交的改动（已 add 但还没 commit 的） |
| `git diff HEAD` | 工作目录相对最后一次提交的全部改动 |

---

## 6. 查看历史：git log

`git log` 有很多有用的参数：

| 命令 | 作用 |
|---|---|
| `git log --oneline` | 一行显示一个提交（最常用） |
| `git log --graph` | 显示分支图 |
| `git log --oneline --graph --all --decorate` | 完整图形历史 |
| `git log -3` | 只看最近3次提交 |
| `git log --author=\"张三\"` | 只看某个作者的提交 |
| `git log -- 文件名` | 只看某个文件的提交历史 |

**推荐日常使用**：

```bash
git log --oneline --graph --all --decorate
```

你可以给它设置一个别名（在第15章会详细讲）：

```bash
git config --global alias.lg \"log --oneline --graph --all --decorate\"
```

之后就可以用 `git lg` 查看图形历史。

---

## 7. 查看某次提交：git show

想看某次提交的详细内容：

```bash
git show 提交哈希
```

例如：

```bash
git show a1b2c3d
```

会显示这次提交的说明、作者、时间和具体改动。

---


---

## 📌 新手跳过指引

**如果你是第一次学 Git**，建议只读**第一部分（核心流程）**。

### 你现在应该掌握的最小目标

能独立完成这个循环：

```bash
git status          # 看当前状态
git add 文件名      # 选择要提交的改动
git commit -m "说明" # 提交
git log --oneline   # 查看历史
```

如果你已经能完成这个循环3次以上，恭喜你已经具备了 Git 的基础能力！

### 第二、三部分可以先跳过

第二、三部分是进阶内容，建议：

- ✅ **立即跳到** [第4章：分支管理](./Git教程系列-04-分支管理.md)
- 🔙 **需要时再回来**，当你遇到这些需求：
  - "我只想提交部分改动" → 回来学 `git add --patch`
  - "提交错了想修改" → 回来学 `git commit --amend`
  - "提交前想检查空白字符" → 回来学 `git diff --check`

### 为什么可以跳过？

- 第二、三部分的内容**不影响**学习分支、合并、远程协作
- 这些是"提高效率"的技巧，不是"必须会"的基础
- 遇到具体需求时再学，记忆效果更好

**跳过不会影响后续章节的学习！**

---
# 第二部分：日常必备

## 8. 撤销还没 add 的修改：git restore

如果你改了文件但还没 `git add`，想撤销改动：

```bash
git restore 文件名
```

**警告**：这会**丢弃工作目录的改动**，恢复到最后一次提交的状态。改动无法找回。

例如：

```bash
# 修改了 hello.txt 但后悔了
git restore hello.txt
```

**安全检查**：

```bash
git diff 文件名    # 先看改了什么
git status         # 确认状态
git restore 文件名  # 确认后再撤销
```

---

## 9. 撤销已经 add 的修改：git restore --staged

如果你已经 `git add` 了，但不想把这个文件放进这次提交：

```bash
git restore --staged 文件名
```

这只是把文件从暂存区移出，改动还在工作目录。

例如：

```bash
git add hello.txt
git restore --staged hello.txt  # 从暂存区移出，改动保留
```

之后可以用 `git diff` 看到改动还在。

---

## 10. 忽略不该提交的文件：.gitignore

有些文件不应该提交到 Git，例如：

- 编译生成的文件（`*.o`、`*.exe`、`*.class`）
- 编辑器临时文件（`.vscode/`、`.idea/`、`*.swp`）
- 日志文件（`*.log`）
- 敏感信息（`config.local.js`、`.env`）
- 依赖文件夹（`node_modules/`、`venv/`）

在项目根目录创建 `.gitignore` 文件，写入要忽略的规则：

```gitignore
# 注释：忽略日志文件
*.log

# 忽略 node_modules 文件夹
node_modules/

# 忽略所有 .env 文件
.env
.env.local

# 但不忽略 .env.example
!.env.example
```

**规则语法**：

| 规则 | 含义 |
|---|---|
| `*.log` | 忽略所有 .log 文件 |
| `build/` | 忽略 build 文件夹 |
| `!important.log` | 不忽略这个文件（即使前面规则匹配） |
| `doc/*.txt` | 忽略 doc 下的 .txt，但不包括子文件夹 |
| `doc/**/*.pdf` | 忽略 doc 下所有 .pdf（包括子文件夹） |

**常见问题**：

如果文件已经被 Git 跟踪，添加到 `.gitignore` 不会自动忽略它。需要先移除：

```bash
git rm --cached 文件名
git commit -m \"stop tracking 文件名\"
```

`--cached` 表示只从 Git 仓库移除，文件本身保留在工作目录。

---

## 11. 什么是一次好提交？

好提交的标准：

1. **粒度合适**：一次提交只做一件事
   - ✅ 好："修复登录按钮样式"
   - ❌ 不好："修复登录按钮样式 + 添加注册功能 + 重构数据库"

2. **说明清楚**：让别人（或3个月后的你）能看懂
   - ✅ 好："fix: 修复用户名包含空格时登录失败的问题"
   - ❌ 不好："修复bug"、"临时提交"、"asdf"

3. **能通过测试**：提交前确保代码能运行
   - 不要提交会导致项目无法运行的版本

4. **不包含无关改动**：
   - 不要把调试代码、临时文件、敏感信息提交上去

**提交信息格式建议**：

```text
类型: 简短描述（不超过50字符）

可选的详细说明（如果需要解释背景、原因）
```

常见类型：

- `feat`: 新功能
- `fix`: 修复bug
- `docs`: 文档修改
- `style`: 格式调整（不影响代码逻辑）
- `refactor`: 重构
- `test`: 添加测试
- `chore`: 构建工具、依赖更新等

例如：

```bash
git commit -m \"feat: 添加用户登录功能\"
```

---


---

## 📌 第三部分：进阶技巧提示

**这部分内容更加进阶**，适合：

- 已经熟练使用 add/commit/log
- 开始追求更高效的工作流
- 需要精细控制提交内容

**完全新手建议**：先跳到 [第4章：分支管理](./Git教程系列-04-分支管理.md)，需要时再回来查阅本部分。

---
# 第三部分：进阶技巧 ⭐ 可选

新手可以先跳过这部分，需要时再回来查阅。

## 12. 精确选择改动：git add --patch

有时你在一个文件里改了多处，但只想提交其中一部分。

`git add --patch`（简写 `-p`）可以让你按"块"选择：

```bash
git add -p hello.txt
```

Git 会逐块询问：

```diff
@@ -1,3 +1,4 @@
 Hello Git
 This is a second line
+Third line here
Stage this hunk [y,n,q,a,d,s,e,?]?
```

常用选项：

| 选项 | 含义 |
|---|---|
| `y` | 暂存这一块 |
| `n` | 不暂存这一块 |
| `s` | 拆分成更小的块 |
| `q` | 退出 |
| `?` | 查看帮助 |

这样可以把一个文件的改动分成多次提交，让历史更清晰。

---

## 13. 修改最后一次提交：git commit --amend

如果刚提交完发现：

- 提交说明写错了
- 忘了加某个文件
- 发现小错误想立即修正

可以用 `--amend` 修改最后一次提交：

### 只改提交说明

```bash
git commit --amend -m \"新的提交说明\"
```

### 补文件到最后一次提交

```bash
git add 忘记的文件.txt
git commit --amend --no-edit
```

`--no-edit` 表示不修改提交说明。

**警告**：

- `--amend` 会**改写历史**。如果这次提交已经推送到远程，不要用 `--amend`，否则会导致推送冲突。
- 只能修改**最后一次**提交。

---

## 14. 检查空白问题：git diff --check

提交前检查是否有多余的空白字符（行尾空格、文件末尾空行等）：

```bash
git diff --check
```

如果有问题，会显示类似：

```text
hello.txt:3: trailing whitespace.
+This line has trailing spaces   
```

很多项目要求提交前清理空白问题，避免无意义的 diff。

---

## 15. 删除和移动文件

### 删除文件

```bash
git rm 文件名
git commit -m \"删除文件名\"
```

`git rm` 做两件事：

1. 删除工作目录的文件
2. 把删除操作加入暂存区

如果只想从 Git 移除，但保留文件：

```bash
git rm --cached 文件名
```

### 移动或重命名文件

```bash
git mv 旧文件名 新文件名
git commit -m \"重命名文件\"
```

相当于：

```bash
mv 旧文件名 新文件名
git rm 旧文件名
git add 新文件名
```

---

# 综合实践

## 一个完整小流程

```bash
# 1. 创建项目文件夹并初始化
mkdir my-project
cd my-project
git init

# 2. 创建第一个文件
echo \"# My Project\" > README.md

# 3. 查看状态
git status

# 4. 加入暂存区并提交
git add README.md
git commit -m \"docs: 添加 README\"

# 5. 创建 .gitignore
echo \"*.log\" > .gitignore
git add .gitignore
git commit -m \"chore: 添加 gitignore\"

# 6. 修改 README
echo \"This is my first Git project\" >> README.md

# 7. 查看改动
git diff

# 8. 提交修改
git add README.md
git commit -m \"docs: 更新 README 说明\"

# 9. 查看历史
git log --oneline
```

---

## 常见误解

| 误解 | 正确理解 |
|---|---|
| `git add` 就是提交 | `git add` 只是加入暂存区，`git commit` 才是提交 |
| `git commit` 会上传到 GitHub | `git commit` 只保存到本地仓库，`git push` 才上传 |
| `.gitignore` 可以忽略已跟踪的文件 | `.gitignore` 只能忽略**未跟踪**的文件，已跟踪的要用 `git rm --cached` |
| `git commit -a` 会提交所有文件 | `-a` 只提交**已跟踪**的修改文件，不包括新文件 |

---

## 提交前的自查清单

每次提交前，建议快速检查：

- [ ] 运行 `git status` 确认要提交的文件
- [ ] 运行 `git diff --staged` 确认暂存的改动
- [ ] 提交信息清楚描述了"做了什么"
- [ ] 提交粒度合适（一个提交只做一件事）
- [ ] 没有包含调试代码、临时文件或敏感信息
- [ ] （可选）运行 `git diff --check` 检查空白字符问题

**快速检查命令**：

```bash
git status           # 看要提交什么
git diff --staged    # 看具体改动
git diff --check     # 检查空白问题（可选）
```

---

## 本章命令速查表

| 命令 | 作用 | 什么时候用 |
|---|---|---|
| `git status` | 查看当前状态 | 随时用，最有用的命令 |
| `git add 文件名` | 暂存文件 | 准备提交前 |
| `git add .` | 暂存当前目录所有改动 | 想一次暂存多个文件时 |
| `git commit -m \"说明\"` | 提交 | 暂存好后 |
| `git commit -a -m \"说明\"` | 自动暂存已跟踪文件并提交 | 只改了已有文件且全部要提交时 |
| `git log --oneline` | 查看历史 | 想看保存过哪些版本时 |
| `git diff` | 查看未暂存改动 | add 之前检查改了什么 |
| `git diff --staged` | 查看已暂存改动 | commit 之前检查将提交什么 |
| `git show 提交哈希` | 查看某次提交详情 | 想知道某次提交具体改了什么时 |
| `git restore 文件` | 撤销工作目录修改 | 文件改坏且还没 add 时 |
| `git restore --staged 文件` | 从暂存区撤出 | 不想把某个文件放进这次提交时 |
| `git rm 文件` | 删除已跟踪文件并暂存删除 | 确认文件不再需要时 |
| `git mv 旧名 新名` | 移动或重命名文件并暂存 | 文件改名或移动位置时 |
| `git add -p` | 交互式暂存（进阶） | 想按块选择改动时 |
| `git commit --amend` | 修改最后一次提交（进阶） | 刚提交完且还没推送时 |
| `git diff --check` | 检查空白问题（进阶） | 提交前检查代码质量时 |

---

## 本章总结

这一章你学会了 Git 的基础工作流：

```text
工作目录修改 → git add 到暂存区 → git commit 保存到本地仓库
```

**核心命令（必学）**：

- `git status` - 随时查看状态
- `git add` - 选择要提交的改动
- `git commit -m` - 提交版本
- `git log --oneline` - 查看历史
- `git diff` - 查看具体改动

**日常必备**：

- `git restore` - 撤销修改
- `.gitignore` - 忽略文件
- 好提交习惯 - 粒度合适、说明清楚

**进阶技巧（可选）**：

- `git add -p` - 精确选择改动
- `git commit --amend` - 修改最后一次提交
- `git diff --check` - 检查空白问题

到这里，你已经能在一条主线上保存版本了。

下一章开始学习分支：如何在不影响主线的情况下开发新功能。

---

**下一步**：[分支管理](./Git教程系列-04-分支管理.md)

---

**返回目录**：[README](./README.md)

