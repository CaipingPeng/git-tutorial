# 04. 分支基础

> 15 分钟学会 Git 最强大的功能:分支

## 为什么需要分支?

想象你正在开发一个网站:
- 主线代码是稳定运行的版本
- 你想添加一个新功能,但不确定会不会成功
- 你不想破坏主线代码

**解决方案**: 创建一个分支!

```
主分支 main:  A---B---C---D
                   \
新功能分支:          E---F
```

- 在分支上开发新功能
- 不影响主分支
- 功能完成后再合并回主分支

## 创建和切换分支

### git branch: 查看分支

```bash
git branch
```

输出:
```
* main
```

`*` 表示当前在 main 分支。

### 创建新分支

```bash
git branch feature
```

这会基于当前分支创建一个名为 `feature` 的新分支。

### git switch: 切换分支

```bash
git switch feature
```

现在你在 `feature` 分支了。

### 创建并切换 (快捷方式)

```bash
git switch -c feature
```

等价于:
```bash
git branch feature
git switch feature
```

## 分支的工作流程

**完整示例**:

```bash
# 1. 查看当前分支
git branch
# * main

# 2. 创建并切换到新分支
git switch -c add-login

# 3. 在新分支上开发
vim login.html
git add login.html
git commit -m "Add login page"

vim login.js
git add login.js
git commit -m "Add login logic"

# 4. 切回主分支
git switch main

# 5. 合并分支
git merge add-login

# 6. 删除已合并的分支
git branch -d add-login
```

## 合并分支

### git merge: 合并

```bash
# 先切换到要合并到的分支
git switch main

# 合并其他分支
git merge feature
```

**发生了什么?**
- Git 把 `feature` 分支的改动合并到 `main`
- `feature` 分支仍然存在,可以继续用或删除

### 合并的两种情况

#### 情况1: 快进合并 (Fast-forward)

```
合并前:
main:     A---B---C
               \
feature:        D---E

合并后:
main:     A---B---C---D---E
               \         /
feature:        D-------E
```

**特点**: main 没有新提交,直接移动指针。

#### 情况2: 三方合并 (3-way merge)

```
合并前:
main:     A---B---C---F
               \
feature:        D---E

合并后:
main:     A---B---C---F---M
               \         /
feature:        D-------E
```

**特点**: main 和 feature 都有新提交,创建合并提交 M。

## 删除分支

```bash
# 删除已合并的分支
git branch -d feature

# 强制删除(即使没合并)
git branch -D feature
```

## 查看分支

### 查看所有分支

```bash
git branch -a
```

输出:
```
* main
  feature
  remotes/origin/main
  remotes/origin/feature
```

### 查看分支的最后一次提交

```bash
git branch -v
```

输出:
```
* main    e4f5g6h Update homepage
  feature a1b2c3d Add login
```

## 分支命名

**常见的分支命名**:

- `main` / `master`: 主分支
- `develop`: 开发分支
- `feature/login`: 功能分支
- `bugfix/issue-123`: 修复分支
- `hotfix/critical-bug`: 紧急修复

**推荐格式**: `类型/描述`

```bash
git switch -c feature/user-profile
git switch -c bugfix/navbar-responsive
git switch -c hotfix/security-patch
```

## 实战场景

### 场景1: 开发新功能

```bash
# 创建功能分支
git switch -c feature/shopping-cart

# 开发...
git add cart.js
git commit -m "Add cart functionality"

git add cart.css
git commit -m "Style shopping cart"

# 完成后合并
git switch main
git merge feature/shopping-cart

# 删除分支
git branch -d feature/shopping-cart

# 推送
git push
```

### 场景2: 紧急修复 bug

```bash
# 正在 feature 分支开发
git status
# 发现主线有紧急 bug

# 切回主分支
git switch main

# 创建修复分支
git switch -c hotfix/critical-bug

# 修复...
git add fix.js
git commit -m "Fix critical bug"

# 合并
git switch main
git merge hotfix/critical-bug

# 推送
git push

# 回到功能分支继续开发
git switch feature
```

### 场景3: 放弃分支

```bash
# 创建了分支,但发现方向不对
git switch -c bad-idea

# 做了一些改动...
git add .
git commit -m "Try something"

# 算了,不要这个分支了
git switch main
git branch -D bad-idea
```

## git checkout vs git switch

**老命令** (Git 2.23 之前):
```bash
git checkout feature    # 切换分支
git checkout -b feature # 创建并切换
```

**新命令** (推荐):
```bash
git switch feature      # 切换分支
git switch -c feature   # 创建并切换
```

**为什么改?**
- `checkout` 功能太多,容易混淆
- `switch` 只负责切换分支,更清晰

## 你只需要记住这 3 点

1. **创建并切换**: `git switch -c 分支名`
2. **合并分支**: `git switch main` → `git merge 分支名`
3. **删除分支**: `git branch -d 分支名`

## 练习

1. 创建一个新分支 `feature/test`
2. 在分支上修改文件并提交
3. 切回 `main` 分支
4. 合并 `feature/test` 分支
5. 删除 `feature/test` 分支

## 下一步

学会了分支,接下来学习如何与团队协作:

→ [远程协作](05-remote-collaboration.md) - 15分钟掌握 GitHub 协作

---

**提示**:
- 经常用分支,不要在 main 上直接开发
- 功能完成再合并,保持 main 的稳定性
- 合并后及时删除分支,保持仓库整洁
