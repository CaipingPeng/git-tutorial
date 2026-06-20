# Git 常见错误排障

排障时先做三件事：

```bash
git status
git branch
git remote -v
```

很多错误不是命令不会用，而是当前目录、当前分支、远程关系不对。

## `fatal: not a git repository`

**英文原文**：`fatal: not a git repository (or any of the parent directories): .git`

含义：当前目录不是 Git 仓库，或者你不在项目根目录/子目录里。

优先检查：

```bash
pwd
ls -a
```

如果没有 `.git`，要么 `cd` 到正确项目目录，要么在练习目录里运行：

```bash
git init
```

## `Please tell me who you are`

**英文原文**：
```
Please tell me who you are.

Run
  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"
```

含义：Git 不知道提交作者是谁。

解决：

```bash
git config --global user.name "你的名字"
git config --global user.email "you@example.com"
```

然后重新提交。

## `nothing to commit, working tree clean`

**英文原文**：`nothing to commit, working tree clean`

含义：当前没有可提交改动。这通常不是错误。

如果你以为自己改了文件，检查：

- 是否保存了编辑器里的文件
- 是否在正确目录
- 是否改的是被 `.gitignore` 忽略的文件
- 是否切到了另一个分支

## `Your branch is ahead of 'origin/main'`

**英文原文**：`Your branch is ahead of 'origin/main' by N commit(s)`

含义：本地分支有远程还没有的提交。

如果这些提交应该上传：

```bash
git push
```

如果你只是想确认差异：

```bash
git log --oneline origin/main..HEAD
```

## `Your branch is behind 'origin/main'`

**英文原文**：`Your branch is behind 'origin/main' by N commit(s)`

含义：远程分支有你本地没有的提交。

先获取并观察：

```bash
git fetch origin
git log --oneline --graph --all --decorate
```

如果团队要求线性更新，可以用：

```bash
git pull --ff-only
```

如果不能快进，按团队规则选择 merge 或 rebase。

## `non-fast-forward`

常见于推送失败。含义：远程分支已经前进，你的本地提交不能直接覆盖它。

不要立刻 `push --force`。

优先流程：

```bash
git fetch origin
git log --oneline --graph --all --decorate
```

然后判断：

| 情况 | 处理 |
|---|---|
| 远程是别人的新提交 | 先整合远程，再推送 |
| 这是你自己的功能分支，刚做过 rebase | 确认无别人基于它工作后用 `git push --force-with-lease` |
| 是 `main`、`master`、`release` 等公共分支 | 不要强推，按团队流程处理 |

## `merge conflict`

含义：Git 无法自动合并，需要你手动决定最终内容。

流程：

```bash
git status
# 打开冲突文件，删除 <<<<<<< ======= >>>>>>> 标记并整理最终内容
git add 冲突文件
git commit
```

如果暂时不想继续：

```bash
git merge --abort
```

## `Your local changes would be overwritten`

常见于切分支、pull 或 merge 时。含义：你当前工作目录里的未提交改动，可能会被目标分支或远程更新覆盖，Git 先停下来保护你。

先看当前改动：

```bash
git status
git diff
```

根据改动是否还要，选择一种方式：

| 你想怎样 | 建议 |
|---|---|
| 这些改动有价值，而且已经能描述 | 先提交到当前分支 |
| 这些改动有价值，但暂时不想提交 | `git stash push -u -m "说明"` |
| 这些改动确定不要 | `git restore 文件名`，未跟踪文件用 `git clean -nd` 先预览 |

处理完以后再切分支或拉取。不要为了绕过提示直接用危险命令覆盖工作目录。

## `You are in 'detached HEAD' state`

含义：你现在不是站在某个分支上，而是直接站在某个提交上。

如果只是查看历史，可以不用处理。

如果你在这里做了有用提交，马上创建分支保护它：

```bash
git switch -c rescue-work
```

如果你是因为运行了类似 `git checkout origin/main` 才看到这条提示，说明你切到的是远程跟踪分支指向的提交，而不是一个可继续日常开发的本地分支。想基于它继续工作，先创建本地分支：

```bash
git switch -c my-work origin/main
```

## `pathspec ... did not match`

常见原因：分支名、文件名或路径写错，或者远程分支还没 fetch 到本地。

检查：

```bash
git branch --all
ls
```

如果是远程分支，先：

```bash
git fetch origin
```

## `Permission denied (publickey)`

常见于 SSH 连接 GitHub/GitLab/Gitee 失败。

检查：

- 是否生成 SSH key
- 公钥是否添加到平台账号
- remote URL 是否是 SSH 格式
- 当前机器的 ssh-agent 是否能找到私钥

可先查看远程地址：

```bash
git remote -v
```

## `could not read Username`

常见于 HTTPS 凭据问题。

处理思路：

- 确认远程 URL 是否正确
- 使用平台要求的 token，而不是账号密码
- 重新登录 Git Credential Manager
- 或改用 SSH

## `remote origin already exists`

含义：当前仓库里已经有一个名叫 `origin` 的远程地址。常见场景是你重复运行了 `git remote add origin ...`。

先看现有远程：

```bash
git remote -v
```

如果只是 URL 写错了，优先改地址：

```bash
git remote set-url origin 新URL
```

如果这个 `origin` 确实不该存在，再删除后重新添加：

```bash
git remote remove origin
git remote add origin 新URL
```

不要在没看 `git remote -v` 的情况下反复 add。远程名只是本地仓库里的别名，真正重要的是它指向哪里、你有没有权限 push。

## `refusing to merge unrelated histories`

含义：两个仓库没有共同历史，Git 默认不允许直接合并。

常见场景：本地 `git init` 后提交过，远程仓库也独立创建过 README。

新手优先做法：重新 clone 远程仓库，把本地文件复制进去再提交。

如果你明确知道要把两段历史合在一起，才使用：

```bash
git pull origin main --allow-unrelated-histories
```

---

## LF/CRLF 换行符警告

典型表现：提交后看到 `LF will be replaced by CRLF`，或跨平台协作时文件被标记为整文件改动。

原因：Windows、macOS、Linux 默认换行符不同，Git 的 `core.autocrlf` 设置会在签出/提交时转换换行符。

推荐做法是用 `.gitattributes` 显式声明，而不是只靠个人配置：

```text
* text=auto eol=lf
```

查看当前文件实际换行符：

```bash
git ls-files --eol
```

只想改个人配置时：

| 平台 | 推荐设置 |
|---|---|
| Windows | `git config --global core.autocrlf true` |
| macOS/Linux | `git config --global core.autocrlf input` |

如果已经因为换行符转换产生大量“假改动”，先提交或 stash 现有改动，再统一规范化，避免把格式改动和真实改动混在一个提交里。

---

## `.gitignore` 写了但文件还在被跟踪

典型表现：

```bash
echo ".env" >> .gitignore
git status
```

但 `git status` 仍然显示 `.env` 被修改。

原因通常是：这个文件已经进入过 Git 的索引或历史。`.gitignore` 只影响未跟踪文件，不会让 Git 自动忘记已经跟踪的文件。

保留本地文件，但让 Git 停止跟踪：

```bash
git rm --cached .env
git add .gitignore
git commit -m "停止跟踪本地环境配置"
```

查看到底是哪条规则命中了忽略：

```bash
git check-ignore -v .env
```

如果这个文件里有密钥、token 或密码，停止跟踪不等于清除了历史；需要先轮换泄露凭据，再按团队规则清理历史。

---

## `Git 和 GitHub 到底有什么区别？`

很多人初学时会混淆这两个名字。其实很简单：

| 概念 | 是什么 |
|---|---|
| **Git** | 一个版本控制软件，在你自己电脑上运行 |
| **GitHub** | 一个基于 Git 的在线代码托管平台 |

就像"照片"和"朋友圈"的区别：你手机拍照（Git），可以把照片发到朋友圈（GitHub）。没有朋友圈，你一样可以拍照；但有了朋友圈，你可以和朋友分享照片、协作编辑。

你在自己的电脑上 `git init`、`git add`、`git commit`，这些操作完全不依赖 GitHub。只有当你需要和他人协作（推送、拉取、提 PR），才需要 GitHub（或 GitLab、Gitee 等类似的托管平台）。

### 一句话记住

> **Git 是工具，GitHub 是平台。** 工具可以独立使用，平台提供协作基础设施。

---

## `bad index file sha1 signature` / `index file corrupt`

含义：Git 的索引文件损坏了。索引是暂存区的内部文件，不是你的项目源文件本身。

先确认没有正在进行的合并、rebase 或 cherry-pick，再在仓库根目录运行：

```bash
mv .git/index .git/index.backup
git reset
```

`git reset` 会根据当前提交重新生成索引。之后运行：

```bash
git status
```

如果工作目录里有未提交改动，重新检查这些改动是否还在。这个问题不常见；如果反复出现，优先检查磁盘、杀毒软件、同步盘或编辑器插件是否在干扰 `.git/` 目录。

---

**返回目录**：[README](./README.md)


## 排障思维流程

`mermaid
flowchart TD
    A[遇到Git问题] --> B{能看到错误信息吗?}
    B -- 是 --> C[复制完整错误信息]
    B -- 否 --> D[运行 git status]
    C --> E[在本文档搜索错误信息]
    D --> E
    E --> F{找到解决方案了吗?}
    F -- 是 --> G[按步骤操作]
    F -- 否 --> H[检查三件事]
    H --> I[1. git status<br/>2. git branch<br/>3. git remote -v]
    I --> J[用搜索引擎搜索<br/>完整错误信息]
`

---

## 更多常见场景

### 推送被拒绝 (rejected)

完整错误可能是：

`	ext
! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'https://github.com/...'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
`

**含义：** 远程分支有你本地没有的提交，Git 拒绝直接推送以避免覆盖别人的工作。

**解决步骤：**

1. 先拉取远程改动：
   `ash
   git pull
   `

2. 如果有冲突，解决冲突后提交

3. 再次推送：
   `ash
   git push
   `

**不要使用 git push --force**，除非你：
- 明确知道会覆盖什么
- 已经和团队确认过
- 这是你的个人分支

---

### 合并冲突太乱，想放弃这次合并

如果正在合并过程中，运行 git status 看到：

`	ext
You have unmerged paths.
`

放弃本次合并：

`ash
git merge --abort
`

这会回到合并前的状态。

---

### 不小心提交了敏感信息（密码、密钥）

**场景1：刚提交，还没推送**

`ash
# 撤销最后一次提交，保留改动在工作目录
git reset --soft HEAD~1

# 从文件中移除敏感信息

# 重新提交
git add .
git commit -m "修正后的提交"
`

**场景2：已经推送到远程**

这很严重。敏感信息一旦推送，就可能已经被别人看到或克隆下来。

⚠️ **立即行动：**
1. 立即更换泄露的密码/密钥
2. 联系仓库管理员
3. 考虑使用 git filter-branch 或 BFG Repo-Cleaner 清理历史（会重写历史，影响所有协作者）

**预防措施：**
- 使用 .gitignore 忽略敏感文件
- 提交前用 git diff --staged 检查
- 使用 git-secrets 工具预防

---

### 提交历史一团糟，想重新整理

**如果还没推送：**

使用交互式 rebase：

`ash
git rebase -i HEAD~5  # 整理最近5次提交
`

会打开编辑器，你可以：
- squash：合并提交
- eword：修改提交信息
- drop：删除提交
- eorder：调整顺序

**如果已经推送：**

不要 rebase 已推送的公共分支。可以考虑：
- 创建新的干净分支重新开始
- 或者接受现状，以后注意提交质量

---

### 切换分支时提示有未提交改动

错误：

`	ext
error: Your local changes to the following files would be overwritten by checkout:
        file.txt
Please commit your changes or stash them before you switch branches.
`

**原因：** 工作目录有改动，切换分支可能会丢失这些改动。

**方案1：提交改动**

`ash
git add .
git commit -m "保存当前工作"
git switch 其他分支
`

**方案2：暂存改动（不想提交）**

`ash
git stash
git switch 其他分支
# 工作完成后回来
git switch 原分支
git stash pop
`

**方案3：放弃改动（确定不要了）**

`ash
git restore .
git switch 其他分支
`

---

### 误删了一个分支

如果分支还没被垃圾回收（通常30天内）：

`ash
# 查看最近的操作记录
git reflog

# 找到分支被删除前的提交哈希，例如 abc1234

# 重建分支
git switch -c 恢复的分支名 abc1234
`

---

### git pull 后代码变乱了

git pull = git fetch + git merge

如果 pull 后出现问题：

`ash
# 查看合并前的状态
git reflog

# 回到 pull 之前（例如显示为 HEAD@{1}）
git reset --hard HEAD@{1}
`

⚠️ --hard 会丢弃工作目录改动，使用前确认！

**更安全的做法：**

以后用两步代替 git pull：

`ash
git fetch origin
git log --oneline --graph --all --decorate  # 先看看远程有什么
git merge origin/main  # 确认后再合并
`

---

### 提交后发现commit message写错了

**场景1：最后一次提交，还没推送**

`ash
git commit --amend
`

会打开编辑器让你修改提交信息。

或者直接：

`ash
git commit --amend -m "正确的提交信息"
`

**场景2：已经推送**

不要修改已推送的提交信息，除非：
- 这是你的个人分支
- 团队同意你修改

---

### 不知道自己在哪个分支上改了东西

如果你改了代码，但不记得在哪个分支：

`ash
git status  # 看当前分支和改动
git branch  # 确认分支列表
`

如果改动在错误的分支：

`ash
git stash              # 保存改动
git switch 正确的分支
git stash pop         # 恢复改动
`

---

## 求助前的检查清单

在向别人求助前，请先完成这个清单：

- [ ] 运行 git status 并截图
- [ ] 运行 git log --oneline --graph --all -10 并截图
- [ ] 复制完整的错误信息（不要只说"报错了"）
- [ ] 说明你想做什么操作
- [ ] 说明期望的结果是什么
- [ ] 说明实际发生了什么
- [ ] 确认是否已经推送到远程

---

## 紧急救援命令

当你不确定发生了什么，又担心搞砸时：

### 先备份当前状态

`ash
# 创建一个临时分支保存当前状态
git switch -c backup-
`

### 查看最近的操作记录

`ash
git reflog -20
`

这会显示 HEAD 的移动历史，通常能帮你找回"丢失"的提交。

### 检查仓库完整性

`ash
git fsck
`

如果仓库损坏，这个命令会报告。

---

## 最后的建议

1. **不要慌张**：Git 很少真正丢失数据，大多数错误都能恢复
2. **求助时说清楚**：完整的错误信息 + 你想做什么 + 已经尝试了什么
3. **定期备份**：重要项目定期推送到远程
4. **学会 reflog**：它是 Git 的"后悔药"
5. **练习环境试错**：不确定的命令先在测试目录里试

记住：**git status 和 git reflog 是你最好的朋友。**
