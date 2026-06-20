# 06. 冲突解决

> 10 分钟学会处理合并冲突

## 什么是冲突?

当两个人修改了同一个文件的同一部分时,Git 无法自动合并,就会产生冲突。

**例子**:

Alice 修改了 `README.md` 第3行:
```markdown
项目简介: 这是一个很棒的项目
```

Bob 也修改了 `README.md` 第3行:
```markdown
项目简介: 这是一个超赞的项目
```

Git 不知道该保留哪个,需要手动解决。

## 冲突的标记

当发生冲突时,Git 会在文件中添加标记:

```markdown
项目简介: 
<<<<<<< HEAD
这是一个很棒的项目
=======
这是一个超赞的项目
>>>>>>> feature-branch
```

**标记说明**:
- `<<<<<<< HEAD`: 当前分支的内容开始
- `=======`: 分隔线
- `>>>>>>> feature-branch`: 要合并的分支内容结束

## 解决冲突的步骤

### 步骤 1: 尝试合并

```bash
git merge feature
```

输出:
```
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
```

### 步骤 2: 查看冲突文件

```bash
git status
```

输出:
```
both modified:   README.md
```

### 步骤 3: 打开文件解决冲突

打开 `README.md`:
```markdown
<<<<<<< HEAD
这是一个很棒的项目
=======
这是一个超赞的项目
>>>>>>> feature-branch
```

**选择保留哪个**:

方案1: 保留 HEAD (当前分支)
```markdown
这是一个很棒的项目
```

方案2: 保留 feature-branch
```markdown
这是一个超赞的项目
```

方案3: 两个都要
```markdown
这是一个很棒又超赞的项目
```

方案4: 都不要,写新的
```markdown
这是最好的项目
```

**删除标记**,保留你想要的内容。

### 步骤 4: 标记为已解决

```bash
git add README.md
```

### 步骤 5: 完成合并

```bash
git commit
```

Git 会自动生成合并提交信息。

## 完整示例

```bash
# 1. 尝试合并
git merge feature
# CONFLICT!

# 2. 查看哪些文件冲突
git status

# 3. 打开冲突文件,手动编辑
vim README.md
# 删除标记,保留想要的内容

# 4. 标记为已解决
git add README.md

# 5. 完成合并
git commit

# 6. 推送
git push
```

## 放弃合并

如果觉得太复杂,想放弃合并:

```bash
git merge --abort
```

一切恢复到合并前的状态。

## 使用工具解决冲突

### VS Code

VS Code 会高亮显示冲突,并提供按钮:
- Accept Current Change (保留当前)
- Accept Incoming Change (保留新的)
- Accept Both Changes (都保留)
- Compare Changes (对比)

### git mergetool

```bash
git mergetool
```

会启动配置的合并工具 (如 VS Code, Meld, KDiff3)。

## 减少冲突的技巧

### 1. 经常同步

```bash
# 每天开始工作前
git pull
```

越早合并,冲突越少。

### 2. 功能分支

不要都在 main 上改,使用功能分支:
```bash
git switch -c feature/my-work
```

### 3. 小步提交

一个功能完成就提交,不要积攒太多改动。

### 4. 沟通协调

如果要改同一个文件,提前沟通:
- Alice: "我要改 login.js"
- Bob: "好,那我改 profile.js"

## 常见冲突场景

### 场景1: pull 时冲突

```bash
git pull
# CONFLICT!

# 解决冲突
vim 冲突文件
git add 冲突文件
git commit

# 推送
git push
```

### 场景2: merge 分支时冲突

```bash
git merge feature
# CONFLICT!

# 解决冲突
vim 冲突文件
git add 冲突文件
git commit
```

### 场景3: rebase 时冲突

```bash
git rebase main
# CONFLICT!

# 解决冲突
vim 冲突文件
git add 冲突文件
git rebase --continue
```

## 你只需要记住这 3 点

1. **找到标记**: `<<<<<<<` `=======` `>>>>>>>`
2. **手动编辑**: 删除标记,保留想要的内容
3. **标记解决**: `git add` → `git commit`

## 练习

1. 创建两个分支,修改同一个文件的同一行
2. 尝试合并,触发冲突
3. 手动解决冲突
4. 完成合并

## 下一步

学会解决冲突后,来学习如何撤销错误:

→ [撤销错误](07-undo-mistakes.md) - 15分钟学会各种撤销操作

---

**提示**:
- 冲突不可怕,就是手动选择保留哪个
- 不确定时先 `git merge --abort`,问问同事
- 解决后记得测试代码是否还能运行
