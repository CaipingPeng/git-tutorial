# Git 命令速查表

这份速查表按“你想做什么”组织，而不是按命令字母排序。

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

## 我想看改了什么

| 目标 | 命令 |
|---|---|
| 看未暂存改动 | `git diff` |
| 看已暂存改动 | `git diff --staged` |
| 看工作目录相对最近提交的全部改动 | `git diff HEAD` |
| 看某次提交内容 | `git show 提交哈希` |

## 我想看历史

| 目标 | 命令 |
|---|---|
| 简洁历史 | `git log --oneline` |
| 图形历史 | `git log --oneline --graph --all --decorate` |
| 看某个文件历史 | `git log -- 文件名` |
| 看每行最后是谁改的 | `git blame 文件名` |
| 找回 HEAD 移动记录 | `git reflog` |

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
| 清理已删除远程分支引用 | `git fetch -p` |

## 我推不上去

| 场景 | 优先命令 |
|---|---|
| 远程有别人新提交 | `git fetch origin` 后观察历史 |
| 想让当前分支追上远程 | `git pull --ff-only` 或按团队规则 merge/rebase |
| 自己 rebase 后需要更新自己的远程分支 | `git push --force-with-lease` |
| 公共分支推送失败 | 不要强推，先找原因或按团队流程处理 |

## 我想撤销

| 场景 | 命令 |
|---|---|
| 丢弃未暂存修改 | `git restore 文件名` |
| 从暂存区撤回但保留文件修改 | `git restore --staged 文件名` |
| 撤销已提交但未推送，保留改动在工作区 | `git reset --mixed HEAD~1` |
| 撤销已提交但未推送，保留改动在暂存区 | `git reset --soft HEAD~1` |
| 撤销已推送提交 | `git revert 提交哈希` |
| 找回误删提交 | `git reflog` 后从目标提交创建分支 |

## 我想临时保存现场

| 目标 | 命令 |
|---|---|
| 保存未提交改动 | `git stash push -m "说明"` |
| 查看 stash 列表 | `git stash list` |
| 应用但保留 stash | `git stash apply` |
| 应用并删除 stash | `git stash pop` |
| 删除 stash | `git stash drop stash@{0}` |

## 我想排查忽略规则或仓库内部

| 目标 | 命令 |
|---|---|
| 显示被忽略文件 | `git status --ignored` |
| 查看哪个忽略规则命中文件 | `git check-ignore -v 文件名` |
| 停止跟踪文件但保留本地文件 | `git rm --cached 文件名` |
| 查看当前提交完整哈希 | `git rev-parse HEAD` |
| 查看 Git 对象内容 | `git cat-file -p 对象哈希` |
| 查看对象占用空间 | `git count-objects -vH` |
| 检查仓库完整性 | `git fsck` |

## 我想导出或离线搬运仓库

| 目标 | 命令 |
|---|---|
| 导出当前提交的源码 zip，不含历史 | `git archive HEAD --format=zip --output=../project.zip` |
| 导出完整历史到 bundle | `git bundle create ../project.bundle --all` |
| 检查 bundle 是否可用 | `git bundle verify ../project.bundle` |
| 从 bundle 克隆仓库 | `git clone ../project.bundle project-copy` |
| 克隆成 bare 仓库 | `git clone --bare my-project my-project.git` |

---

**返回目录**：[README](./README.md)
