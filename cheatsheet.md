# Git 命令速查表

这份速查表按"你想做什么"组织，而不是按命令字母排序。

> 💡 **使用提示**：
> - 🟢 绿色标记：日常安全命令
> - 🟡 黄色标记：需要理解后使用
> - 🔴 红色标记：危险操作，使用前三思

---


---

## 🚨 紧急救援速查

遇到问题时的快速解决方案：

| 我遇到的问题 | 快速方案 | 详细说明 |
|---|---|---|
| 刚提交错了，还没推送 | `git commit --amend` 或 `git reset HEAD~1` | 修改最后一次提交或撤销提交但保留改动 |
| 刚提交错了，已经推送 | `git revert HEAD` | 创建一个新提交来撤销上次改动 |
| 推送被拒绝 | `git pull` 然后再 `git push` | 先拉取远程更新，解决冲突后再推送 |
| 冲突不会解决 | `git merge --abort` 或 `git rebase --abort` | 取消正在进行的合并或变基 |
| 文件改坏了想恢复 | `git restore 文件名` | 恢复到最后一次提交的状态（**会丢失未提交改动**） |
| 删错分支了 | `git reflog` 找到提交，`git switch -c 新分支名 哈希` | 从 reflog 找回提交并创建新分支 |
| 不知道在哪个分支 | `git status` 和 `git branch` | 查看当前状态和所有分支 |
| 忘了自己改了什么 | `git diff` | 查看未暂存的改动 |
| 不小心 `git add` 了不该加的 | `git restore --staged 文件名` | 从暂存区撤出，改动保留 |
| 想撤销最近3次提交但保留改动 | `git reset --soft HEAD~3` | 提交撤销，改动保留在暂存区 |
| rebase 搞乱了想回到之前 | `git reflog` 找到 rebase 前的提交，`git reset --hard 哈希` | 强制回到 rebase 之前的状态 |
| 想放弃本地所有改动，对齐远程 | `git fetch origin` 然后 `git reset --hard origin/main` | **危险操作**，会丢失所有本地改动 |

**救援三步曲**：

1. **不要慌** - Git 很难真正丢失已提交的内容
2. **先看状态** - `git status` 和 `git log --oneline`
3. **查 reflog** - `git reflog` 是最后的救命稻草，记录了 HEAD 的所有移动

**记住**：
- 只要提交过，就能从 `reflog` 找回
- 还没提交的改动被 `git restore` 或 `git reset --hard` 删除后无法恢复
- 遇到不确定的操作，先在测试分支上试验

---
## 新手最常用的10个命令

初学者应该先掌握这10个命令，它们覆盖了80%的日常工作：

| 命令 | 作用 | 安全性 |
|-----|------|--------|
| `git status` | 查看当前状态（最有用的命令） | 🟢 只读 |
| `git add 文件名` | 把改动加入暂存区 | 🟢 安全 |
| `git commit -m "说明"` | 提交到本地仓库 | 🟢 安全 |
| `git log --oneline` | 查看提交历史 | 🟢 只读 |
| `git diff` | 查看未暂存的改动 | 🟢 只读 |
| `git branch` | 查看分支列表 | 🟢 只读 |
| `git switch 分支名` | 切换分支 | 🟡 会改变工作目录 |
| `git merge 分支名` | 合并分支 | 🟡 可能产生冲突 |
| `git pull` | 从远程拉取并合并 | 🟡 可能产生冲突 |
| `git push` | 推送到远程仓库 | 🟡 会影响远程 |

---

## 每日工作流速览

### 开始新功能
\\\ash
git switch main                  # 切到主分支
git pull                         # 拉取最新代码
git switch -c feature-新功能     # 创建并切换到功能分支
\\\

### 日常提交
\\\ash
git status                       # 查看改了什么
git add 文件名                   # 暂存改动
git commit -m "说明"             # 提交
\\\

### 同步和合并
\\\ash
git push                         # 推送到远程
# 在 GitHub/GitLab 创建 PR
# PR 审查通过后合并
git switch main                  # 回到主分支
git pull                         # 拉取合并后的代码
git branch -d feature-旧功能     # 删除已合并的分支
\\\

---

## 我想知道当前状态

| 目标 | 命令 |
|---|---|
| 查看当前分支、改动和 Git 建议 | `git status` |
| 查看当前分支列表 | `git branch` |
| 查看远程仓库地址 | `git remote -v` |
| 查看上游关系 | `git branch -vv` |

## 我想保存改动

| 目标 | 命令 |
|---|---|
| 暂存某个文件 | `git add 文件名` |
| 暂存当前目录改动 | `git add .` |
| 提交暂存区 | `git commit -m "说明"` |
| 修改最后一次提交说明或补文件 | `git commit --amend` |
| 暂存所有已跟踪文件并提交（快捷方式，慎用：跳过暂存选择） | `git commit -am "说明"` |

## 我想看改了什么

| 目标 | 命令 |
|---|---|
| 看未暂存改动 | `git diff` |
| 看已暂存改动 | `git diff --staged` |
| 看工作目录相对最近提交的全部改动 | `git diff HEAD` |
| 看两个提交/标签之间的差异统计 | `git diff A..B --stat` |
| 看某次提交内容 | `git show 提交哈希` |

## 我想看历史

| 目标 | 命令 |
|---|---|
| 简洁历史 | `git log --oneline` |
| 图形历史 | `git log --oneline --graph --all --decorate` |
| 看 B 有而 A 没有的提交 | `git log A..B --oneline` |
| 在当前版本里搜索内容 | `git grep -n "关键词"` |
| 在某个标签或提交里搜索内容 | `git grep -n "关键词" v1.0.0` |
| 看某个文件历史 | `git log -- 文件名` |
| 看每行最后是谁改的 | `git blame 文件名` |
| 用自动命令二分定位坏提交 | `git bisect run 测试命令` |
| 找回 HEAD 移动记录 | `git reflog` |
| 按作者统计提交数 | `git shortlog -sn` |
| 列出标签 | `git tag` |
| 查看某个标签以来的提交 | `git log v1.0.0..HEAD --oneline` |

## 我想标记版本

| 目标 | 命令 |
|---|---|
| 创建附注标签（正式发布用） | `git tag -a v1.0.0 -m "说明"` |
| 创建轻量标签 | `git tag v1.0.0` |
| 给某次提交打标签 | `git tag -a v0.9.0 哈希 -m "说明"` |
| 列出标签 | `git tag` |
| 按模式过滤标签 | `git tag -l "v1.*"` |
| 查看标签指向的提交 | `git show v1.0.0` |
| 查看上次发布以来的提交 | `git log v1.0.0..HEAD --oneline` |
| 推送单个标签 | `git push origin v1.0.0` |
| 推送所有标签 | `git push origin --tags` |
| 推送并附带附注标签 | `git push --follow-tags` |
| 从标签开分支修 bug | `git switch -c hotfix-1.0 v1.0.0` |
| 删本地标签 | `git tag -d v1.0.0` |
| 删远程标签 | `git push origin --delete v1.0.0` |

## 我想配置 Git

| 目标 | 命令 |
|---|---|
| 设置全局用户名和邮箱 | `git config --global user.name "名字"` / `git config --global user.email "邮箱"` |
| 只为当前仓库设置身份 | `git config user.name "名字"`（去掉 `--global`） |
| 设置默认分支名为 main | `git config --global init.defaultBranch main` |
| 配置命令别名 | `git config --global alias.co checkout` |
| 设置默认编辑器 | `git config --global core.editor "code --wait"` |
| 跨平台换行符自动转换 | `git config --global core.autocrlf input`（macOS/Linux）或 `true`（Windows） |
| 列出所有配置及来源 | `git config --list --show-origin` |
| 编辑全局配置文件 | `git config --global --edit` |

## 我想清理仓库

| 目标 | 命令 |
|---|---|
| 预览将删除的未跟踪文件和目录 | `git clean -nd` |
| 删除未跟踪文件和目录（危险） | `git clean -fd` |
| 压缩松散对象并清理 | `git gc` |
| 更激进地清理（慎用） | `git gc --aggressive` |
| 立即清理不可达对象 | `git prune` |
| 删除已被远程删除的本地远程引用 | `git fetch -p` |
| 查看对象占用空间 | `git count-objects -vH` |
| 检查仓库完整性 | `git fsck` |

## 我想开分支或切分支

| 目标 | 命令 |
|---|---|
| 创建并切换分支 | `git switch -c 分支名` |
| 切换到已有分支 | `git switch 分支名` |
| 切回上一个分支 | `git switch -` |
| 从某个提交创建分支 | `git switch -c 分支名 提交哈希` |
| 重命名当前分支 | `git branch -m 新分支名` |
| 删除已合并本地分支 | `git branch -d 分支名` |
| 强制删除本地分支 | `git branch -D 分支名` |
| 删除远程分支 | `git push origin --delete 分支名` |

## 我想合并分支

| 目标 | 命令 |
|---|---|
| 把源分支合进当前分支 | `git merge 源分支` |
| 取消正在进行的合并 | `git merge --abort` |
| 查看合并后的历史 | `git log --oneline --graph --all --decorate` |

## 我想同步远程

| 目标 | 命令 |
|---|---|
| 克隆仓库 | `git clone URL` |
| 获取远程更新但不合并 | `git fetch origin` |
| 拉取并整合当前分支上游 | `git pull` |
| 只允许快进拉取 | `git pull --ff-only` |
| 首次推送并设置上游 | `git push -u origin 分支名` |
| 推送当前分支 | `git push` |
| 修改已有远程地址 | `git remote set-url origin 新URL` |
| 清理已删除远程分支引用 | `git fetch -p` |
| 基于远程分支创建本地跟踪分支 | `git switch --track origin/分支名` |

## 我推不上去

| 场景 | 优先命令 |
|---|---|
| 远程有别人新提交 | `git fetch origin` 后观察历史 |
| 想让当前分支追上远程 | `git pull --ff-only` 或按团队规则 merge/rebase |
| 自己 rebase 后需要更新自己的远程分支 | `git push --force-with-lease` |
| 确认丢弃本地并对齐远程（危险） | `git fetch origin` 后 `git reset --hard origin/main` |
| 公共分支推送失败 | 不要强推，先找原因或按团队流程处理 |

最后一行会丢掉当前分支上没有保存好的工作区修改，也会让本地独有提交暂时离开分支历史。只在练习仓库、临时分支，或你确认本地内容都不要时使用。

## 我想撤销

| 场景 | 命令 |
|---|---|
| 丢弃未暂存修改 | `git restore 文件名` |
| 从暂存区撤回但保留文件修改 | `git restore --staged 文件名` |
| 撤销已提交但未推送，保留改动在工作区 | `git reset --mixed HEAD~1` |
| 撤销已提交但未推送，保留改动在暂存区 | `git reset --soft HEAD~1` |
| 撤销已推送提交 | `git revert 提交哈希` |
| 找回误删提交 | `git reflog` 后从目标提交创建分支 |
| 预览将删除的未跟踪文件 | `git clean -nd` |
| 删除未跟踪文件和目录 | `git clean -fd` |

## 我想临时保存现场

| 目标 | 命令 |
|---|---|
| 保存未提交改动 | `git stash push -m "说明"` |
| 查看 stash 列表 | `git stash list` |
| 应用但保留 stash | `git stash apply` |
| 应用并删除 stash | `git stash pop` |
| 从 stash 创建新分支 | `git stash branch 新分支名 stash@{0}` |
| 删除 stash | `git stash drop stash@{0}` |

## 我想排查忽略规则或仓库内部

| 目标 | 命令 |
|---|---|
| 显示被忽略文件 | `git status --ignored` |
| 查看哪个忽略规则命中文件 | `git check-ignore -v 文件名` |
| 查看 Git 正在跟踪哪些文件 | `git ls-files` |
| 停止跟踪文件但保留本地文件 | `git rm --cached 文件名` |
| 查看当前提交完整哈希 | `git rev-parse HEAD` |
| 查看 Git 对象类型 | `git cat-file -t 对象哈希` |
| 查看 Git 对象内容 | `git cat-file -p 对象哈希` |
| 递归列出某次提交的 tree/blob | `git ls-tree -r HEAD` |
| 查看索引里的暂存记录 | `git ls-files --stage` |
| 查看对象占用空间 | `git count-objects -vH` |
| 检查仓库完整性 | `git fsck` |
| 新开一个工作树检出的分支 | `git worktree add ../path 分支` |
| 列出所有工作树 | `git worktree list` |
| 提交跨平台换行/二进制规则 | `.gitattributes` |
| 初始化子模块内容 | `git submodule update --init --recursive` |
| 检查补丁能否应用 | `git apply --check 补丁文件` |
| 应用邮件补丁为提交 | `git am --signoff < 补丁文件` |

## 我想导出或离线搬运仓库

| 目标 | 命令 |
|---|---|
| 导出当前提交的源码 zip，不含历史 | `git archive HEAD --format=zip --output=../project.zip` |
| 导出完整历史到 bundle | `git bundle create ../project.bundle --all` |
| 检查 bundle 是否可用 | `git bundle verify ../project.bundle` |
| 从 bundle 克隆仓库 | `git clone ../project.bundle project-copy` |
| 克隆成 bare 仓库 | `git clone --bare my-project my-project.git` |
| 导出当前分支相对 main 的补丁 | `git format-patch main` |

---

**返回目录**：[README](./README.md)

