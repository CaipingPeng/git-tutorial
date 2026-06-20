# Git 常见错误排障

排障时先做三件事：

```bash
git status
git branch
git remote -v
```

很多错误不是命令不会用，而是当前目录、当前分支、远程关系不对。

## `fatal: not a git repository`

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

含义：Git 不知道提交作者是谁。

解决：

```bash
git config --global user.name "你的名字"
git config --global user.email "you@example.com"
```

然后重新提交。

## `nothing to commit, working tree clean`

含义：当前没有可提交改动。这通常不是错误。

如果你以为自己改了文件，检查：

- 是否保存了编辑器里的文件
- 是否在正确目录
- 是否改的是被 `.gitignore` 忽略的文件
- 是否切到了另一个分支

## `Your branch is ahead of 'origin/main'`

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

## `refusing to merge unrelated histories`

含义：两个仓库没有共同历史，Git 默认不允许直接合并。

常见场景：本地 `git init` 后提交过，远程仓库也独立创建过 README。

新手优先做法：重新 clone 远程仓库，把本地文件复制进去再提交。

如果你明确知道要把两段历史合在一起，才使用：

```bash
git pull origin main --allow-unrelated-histories
```

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

**返回目录**：[README](./README.md)
