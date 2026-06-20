# 07. 撤销错误

> 15 分钟学会各种撤销操作

Git 的一大优势就是可以随时撤销。本章介绍常见的"后悔药"。

## 撤销场景速查

| 想撤销什么 | 命令 |
|---|---|
| 工作目录的改动 | `git restore 文件` |
| 暂存区的文件 | `git restore --staged 文件` |
| 上一次提交 | `git reset --soft HEAD^` |
| 上一次提交+改动 | `git reset --hard HEAD^` |
| 提交信息写错 | `git commit --amend` |

## 撤销工作目录的改动

### 场景: 改坏了,想恢复

```bash
# 修改了文件,但发现改错了
vim index.html

# 撤销改动
git restore index.html
```

文件恢复到上次提交的状态。

**撤销所有改动**:
```bash
git restore .
```

## 撤销暂存

### 场景: 不小心 add 了

```bash
# 不小心添加了不该提交的文件
git add secret.txt

# 从暂存区移除
git restore --staged secret.txt
```

文件仍在工作目录,只是不再暂存。

## 修改提交

### 场景: 提交信息写错了

```bash
git commit -m "Fix bug"
# 哦不,应该写 "Fix login bug"

# 修改上一次提交信息
git commit --amend -m "Fix login bug"
```

### 场景: 忘记添加文件

```bash
git commit -m "Add feature"
# 哦不,忘记添加 style.css 了

# 添加文件并修改提交
git add style.css
git commit --amend --no-edit
```

`--no-edit` 表示不修改提交信息。

**警告**: 只能修改**还没推送**的提交!

## 回退提交

### git reset: 回退到某个提交

有三种模式:

#### --soft: 只移动 HEAD,保留改动

```bash
git reset --soft HEAD^
```

- 回退一个提交
- 改动保留在暂存区
- 可以重新提交

**用途**: 想重新组织提交。

#### --mixed: 移动 HEAD,改动回到工作目录

```bash
git reset HEAD^
```

(默认就是 --mixed)

- 回退一个提交
- 改动保留在工作目录,但不在暂存区
- 可以重新 add

**用途**: 想修改后再提交。

#### --hard: 彻底回退,丢弃改动

```bash
git reset --hard HEAD^
```

- 回退一个提交
- 改动被丢弃
- 工作目录变干净

**用途**: 想彻底放弃这个提交。

**警告**: 这个操作会丢失代码,慎用!

### 回退多个提交

```bash
# 回退 3 个提交
git reset --hard HEAD~3

# 回退到指定提交
git reset --hard a1b2c3d
```

### reset 对比

| 模式 | HEAD | 暂存区 | 工作目录 |
|---|---|---|---|
| --soft | ✓ 移动 | ✗ 不变 | ✗ 不变 |
| --mixed | ✓ 移动 | ✓ 清空 | ✗ 不变 |
| --hard | ✓ 移动 | ✓ 清空 | ✓ 清空 |

## 反转提交

### git revert: 创建一个反向提交

```bash
git revert a1b2c3d
```

- 不是删除提交
- 而是创建一个新提交,内容是反向的
- 更安全,保留历史

**对比**:
```
reset (删除提交):
A---B---C       →  A---B

revert (反向提交):
A---B---C       →  A---B---C---C'
```

**用途**: 已经推送的提交,想撤销。

## 恢复删除的文件

### 场景: 删除了文件

```bash
# 误删了文件
rm important.txt

# 恢复
git restore important.txt
```

### 场景: 提交后删除了文件

```bash
# 之前提交中有这个文件,但现在被删了
git log --all --full-history -- deleted-file.txt
# 找到包含这个文件的提交 a1b2c3d

# 恢复
git restore --source=a1b2c3d deleted-file.txt
```

## 找回丢失的提交

### git reflog: 操作日志

```bash
git reflog
```

输出:
```
e4f5g6h HEAD@{0}: reset: moving to HEAD^
a1b2c3d HEAD@{1}: commit: Add feature
b2c3d4e HEAD@{2}: commit: Fix bug
```

reflog 记录了所有 HEAD 的移动。

### 恢复误删的提交

```bash
# 不小心 reset --hard 了
git reset --hard HEAD^
# 哦不!想要回来

# 查看 reflog
git reflog
# e4f5g6h HEAD@{1}: commit: Important work

# 恢复
git reset --hard e4f5g6h
```

## 清理工作目录

### git clean: 删除未跟踪文件

```bash
# 预览会删除什么
git clean -n

# 删除未跟踪文件
git clean -f

# 删除未跟踪文件和目录
git clean -fd
```

**警告**: 这些文件会被永久删除,无法恢复!

## 常见场景

### 场景1: 改了几个文件,想全部撤销

```bash
git restore .
```

### 场景2: 提交了,想回退

```bash
# 保留改动,重新提交
git reset --soft HEAD^

# 彻底放弃
git reset --hard HEAD^
```

### 场景3: 已经 push 了,想撤销

```bash
# 不要用 reset,用 revert
git revert HEAD
git push
```

### 场景4: 删除了文件,想恢复

```bash
git restore 文件名
```

### 场景5: reset 错了,想恢复

```bash
git reflog
git reset --hard HEAD@{1}
```

## checkout vs restore vs reset

Git 2.23 新增了 `restore` 和 `switch`,让命令更清晰:

| 操作 | 老命令 | 新命令 |
|---|---|---|
| 撤销文件 | `git checkout -- file` | `git restore file` |
| 切换分支 | `git checkout branch` | `git switch branch` |
| 回退提交 | `git reset` | `git reset` |

推荐使用新命令 `restore` 和 `switch`。

## 你只需要记住这 3 点

1. **撤销改动**: `git restore 文件`
2. **回退提交**: `git reset --hard HEAD^` (慎用!)
3. **已推送**: 用 `git revert`,不用 `reset`

## 练习

1. 修改一个文件,用 `restore` 撤销
2. 提交后,用 `reset --soft` 回退
3. 用 `reflog` 查看操作历史

## 下一步

基础教程的最后一章,学习 GitHub 工作流:

→ [GitHub 工作流](08-github-workflow.md) - 15分钟学会开源贡献

---

**提示**:
- `restore` 撤销工作目录改动
- `reset` 回退提交
- `revert` 反转已推送的提交
- `reflog` 是最后的救命稻草
