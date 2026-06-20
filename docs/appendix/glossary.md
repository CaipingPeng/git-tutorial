# Git 术语表

按字母排序的 Git 常用术语中英对照与解释。

## A

**Add (添加/暂存)**  
将工作区的改动标记到暂存区，准备下次提交。命令: git add

**Amend (修补)**  
修改最近一次提交的内容或说明。命令: git commit --amend

## B

**Bare Repository (裸仓库)**  
只包含 Git 数据的仓库，没有工作目录，常用作远程中心仓库。

**Bisect (二分查找)**  
通过二分法自动定位引入 bug 的提交。命令: git bisect

**Blob (二进制大对象)**  
Git 内部存储文件内容的对象类型。

**Branch (分支)**  
指向某次提交的可移动指针，用于并行开发。命令: git branch

## C

**Cherry-pick (挑选提交)**  
将其他分支的某次提交应用到当前分支。命令: git cherry-pick

**Clone (克隆)**  
从远程仓库复制完整历史到本地。命令: git clone

**Commit (提交)**  
将暂存区内容保存为仓库历史的一个快照。命令: git commit

**Commit Hash (提交哈希)**  
用 SHA-1 生成的唯一标识某次提交的 40 位字符串（常简写前 7 位）。

**Conflict (冲突)**  
合并或变基时，同一文件同一位置有不同修改，需手动解决。

## D

**Detached HEAD (游离 HEAD)**  
HEAD 直接指向某次提交而非分支，此时提交容易丢失，需谨慎。

**Diff (差异)**  
显示文件或提交之间的改动。命令: git diff

**Distributed (分布式)**  
每个开发者都有完整仓库副本，无需依赖中心服务器。

## F

**Fast-forward (快进合并)**  
目标分支是当前分支的直接后代时，直接移动指针，不产生合并提交。

**Fetch (获取)**  
从远程仓库下载更新，但不自动合并到本地分支。命令: git fetch

**Fork (派生/复刻)**  
在 GitHub/GitLab 等平台复制他人仓库到自己账号下，用于开源贡献。

## G

**Git Object (Git 对象)**  
Git 内部存储的基本单位，包括 blob、tree、commit、tag 四种类型。

## H

**HEAD**  
指向当前检出分支或提交的特殊指针，代表"你现在在哪里"。

**Hash (哈希)**  
见 Commit Hash。

**Hook (钩子)**  
在 Git 特定操作（如提交、推送）前后自动执行的脚本。

## I

**Index (索引/暂存区)**  
见 Staging Area。

## L

**Log (日志)**  
查看提交历史。命令: git log

## M

**Merge (合并)**  
将两个分支的历史整合到一起。命令: git merge

**Merge Commit (合并提交)**  
有两个父提交的特殊提交，记录分支合并点。

## O

**Origin (远程源)**  
默认远程仓库的别名，通常指克隆来源。

## P

**Pull (拉取)**  
相当于 etch + merge，获取并整合远程分支。命令: git pull

**Pull Request / PR (拉取请求)**  
在 GitHub 上请求将自己的分支合并到目标分支的功能。

**Push (推送)**  
将本地提交上传到远程仓库。命令: git push

## R

**Rebase (变基)**  
将一系列提交移动到新基础提交之上，让历史更线性。命令: git rebase

**Reflog (引用日志)**  
记录 HEAD 和分支移动历史，用于找回丢失提交。命令: git reflog

**Remote (远程仓库)**  
托管在网络或其他路径的仓库副本。命令: git remote

**Repository / Repo (仓库)**  
存储项目所有文件及完整历史的 .git 目录。

**Reset (重置)**  
移动分支指针，可撤销提交。命令: git reset

**Restore (恢复)**  
恢复工作区或暂存区文件到之前状态。命令: git restore

**Revert (还原)**  
用新提交撤销某次历史提交的改动。命令: git revert

## S

**SHA / SHA-1**  
Git 用来生成提交哈希的加密算法（新版 Git 正迁移到 SHA-256）。

**Snapshot (快照)**  
Git 的提交存储方式，每次提交保存文件的完整状态，而非增量。

**Stage / Staging Area (暂存区)**  
位于工作区和仓库之间的中间层，用 git add 选择要提交的改动。

**Stash (储藏)**  
临时保存未提交改动，清空工作区。命令: git stash

**Submodule (子模块)**  
在一个 Git 仓库中引用另一个仓库。命令: git submodule

**Switch (切换)**  
切换分支或创建新分支。命令: git switch（替代旧的 git checkout）

## T

**Tag (标签)**  
给某次提交打上永久标记，常用于版本发布。命令: git tag

**Tracking Branch (跟踪分支)**  
与远程分支关联的本地分支，可直接用 git pull/push。

**Tree (树对象)**  
Git 内部表示目录结构的对象类型，包含文件和子目录。

## U

**Upstream (上游)**  
本地分支跟踪的远程分支，如 origin/main。

**Untracked Files (未跟踪文件)**  
工作区中从未被 git add 的新文件，Git 不会记录其改动。

## W

**Working Directory / Working Tree (工作目录/工作区)**  
你实际编辑文件的目录，包含从仓库检出的文件。

**Worktree (工作树)**  
同一仓库的多个工作目录，可同时检出不同分支。命令: git worktree

---

## 三区模型

Git 的核心理解模型，描述文件的三种状态：

1. **Working Directory (工作区)** - 你编辑的文件
2. **Staging Area / Index (暂存区)** - git add 后等待提交
3. **Repository (仓库)** - git commit 后永久保存

`
工作区 ──git add──> 暂存区 ──git commit──> 仓库
       <─git restore──       <─git reset──
`

---

**返回目录**：[README](../../README.md) | [基础教程](../basics/) | [进阶教程](../advanced/)
