# 05. 远程协作

> 15 分钟学会与团队使用 Git 协作

## 什么是远程仓库?

**本地仓库**: 你电脑上的 Git 仓库
**远程仓库**: 托管在服务器上的 Git 仓库 (如 GitHub)

```
你的电脑           GitHub            同事的电脑
   |                |                    |
   |---→ push  --→|                    |
   |                |←--- pull ←--------|
   |←--- pull ←-----|                    |
   |                |←--- push ←--------|
```

## 克隆远程仓库

### git clone: 复制仓库

```bash
git clone https://github.com/user/repo.git
```

**发生了什么?**
1. 下载完整的仓库(包括历史)
2. 创建本地工作目录
3. 自动设置 `origin` 远程仓库
4. 切换到默认分支

**示例**:
```bash
git clone https://github.com/torvalds/linux.git
cd linux
```

### 克隆指定分支

```bash
git clone -b develop https://github.com/user/repo.git
```

## 查看远程仓库

### git remote: 查看远程

```bash
git remote
```

输出:
```
origin
```

### 查看详细信息

```bash
git remote -v
```

输出:
```
origin  https://github.com/user/repo.git (fetch)
origin  https://github.com/user/repo.git (push)
```

## 推送和拉取

### git push: 推送到远程

```bash
# 推送到默认远程分支
git push

# 第一次推送需要指定
git push -u origin main
```

`-u` (--set-upstream) 的作用:
- 设置本地分支跟踪远程分支
- 以后只需要 `git push` 就行

### git pull: 拉取并合并

```bash
git pull
```

等价于:
```bash
git fetch  # 获取远程更新
git merge  # 合并到当前分支
```

### git fetch: 只获取不合并

```bash
git fetch origin
```

**区别**:
- `fetch`: 只下载,不改变本地代码
- `pull`: 下载并自动合并

**推荐**: 先 `fetch` 看看有什么更新,再决定是否 `merge`。

## 协作工作流

### 基本流程

```bash
# 1. 克隆仓库
git clone https://github.com/team/project.git
cd project

# 2. 创建功能分支
git switch -c feature/new-feature

# 3. 开发并提交
git add .
git commit -m "Add feature"

# 4. 推送分支
git push -u origin feature/new-feature

# 5. 在 GitHub 上创建 Pull Request

# 6. 合并后,更新本地
git switch main
git pull
git branch -d feature/new-feature
```

### 保持同步

```bash
# 每天开始工作前
git switch main
git pull

# 创建新功能分支
git switch -c feature/today-work
```

## 解决推送冲突

### 场景: 推送被拒绝

```bash
git push
```

错误信息:
```
! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'origin'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
```

**原因**: 远程有新提交,你的本地不是最新的。

**解决方法**:

```bash
# 1. 先拉取远程更新
git pull

# 2. 如果有冲突,解决冲突
#   (见下一章)

# 3. 再推送
git push
```

## 远程分支

### 查看远程分支

```bash
git branch -r
```

输出:
```
origin/main
origin/develop
origin/feature/login
```

### 跟踪远程分支

```bash
# 创建本地分支跟踪远程分支
git switch -c feature origin/feature
```

### 删除远程分支

```bash
git push origin --delete feature
```

## 添加多个远程仓库

### 添加远程

```bash
git remote add upstream https://github.com/original/repo.git
```

现在有两个远程:
- `origin`: 你自己的 fork
- `upstream`: 原始仓库

### 从上游同步

```bash
# 获取上游更新
git fetch upstream

# 合并到本地
git merge upstream/main

# 推送到自己的 fork
git push origin main
```

## 你只需要记住这 3 点

1. **克隆**: `git clone URL`
2. **同步**: `git pull` (拉取) → `git push` (推送)
3. **推送前先拉取**: 避免冲突

## 练习

1. 在 GitHub 创建一个新仓库
2. 用 `git clone` 克隆到本地
3. 修改文件,提交,推送
4. 在 GitHub 网页上修改文件
5. 用 `git pull` 拉取更新

## 下一步

学会协作后,难免会遇到冲突:

→ [冲突解决](06-conflict-resolution.md) - 10分钟学会解决冲突

---

**提示**:
- push 前先 pull,避免冲突
- 经常同步,减少合并难度
- 使用分支,不要都在 main 上改
