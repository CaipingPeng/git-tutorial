# Git 暂存与保存现场

真实开发中，你经常会遇到这种情况：手头功能改到一半，突然要切分支修 bug；或者本地有一堆实验改动，但暂时不想提交。这个时候可以用 `git stash` 保存现场。

本章目标：

1. 理解 stash 解决什么问题
2. 学会保存、查看、应用、删除 stash
3. 知道 stash 冲突怎么处理
4. 会判断什么时候用 stash，什么时候用临时提交

---

## 1. stash 解决什么问题？

Git 有一个经常被忽略的心理层面的好处：**它让你不再害怕修改**。知道自己的所有改动都可以随时保存现场或撤销，会给你一种“安全网”的感觉。stash 就是这个安全网中最方便的工具之一——当你正在工作但需要切换到其他任务时，不需要匆忙提交一个半成品 commit，也不需要丢弃当前进度。保存现场，切换分支，处理完再回来，干干净净。

切换分支前，Git 有时会阻止你：

```text
error: Your local changes to the following files would be overwritten by checkout
```

这不是 Git 刁难你，而是在保护你：目标分支的文件状态可能覆盖你当前未提交的改动。

如果这些改动暂时不想提交，也不想丢弃，就可以：

```bash
git stash push -m "临时保存登录页面改动"
```

stash 可以理解为：

> 把当前未提交改动打包放进临时抽屉，让工作目录恢复干净。

它解决的是“我还没准备好提交，但现在需要一个干净工作目录”的问题。它不是用来替代 commit 的长期保存机制。

```text
工作目录/暂存区的未提交改动
        │ git stash push
        ▼
stash 临时记录
        │ git stash apply / pop
        ▼
重新回到工作目录
```

---

## 2. 保存现场

先看状态：

```bash
git status
```

如果有未提交改动：

```text
Changes not staged for commit:
  modified:   login.html
```

保存：

```bash
git stash push -m "临时保存登录页面改动"
```

再看状态：

```bash
git status
```

通常会回到：

```text
nothing to commit, working tree clean
```

现在你可以安全切分支。

---

## 3. 查看 stash 列表

```bash
git stash list
```

示例：

```text
stash@{0}: On feature-login: 临时保存登录页面改动
stash@{1}: On main: 尝试新的首页文案
```

`stash@{0}` 是最近一次保存的 stash。

如果想看某个 stash 里大概改了什么：

```bash
git stash show stash@{0}
```

想看详细 diff：

```bash
git stash show -p stash@{0}
```

---

## 4. 应用 stash：`apply` 和 `pop`

应用前先确认自己站在正确分支上，并且当前工作目录尽量干净：

```bash
git status
git branch --show-current
```

因为 stash 恢复的是一组文件改动，不是“回到当时的完整仓库状态”。如果你在错误分支上应用，或者当前文件已经有其他修改，就更容易冲突。

### 只应用，不删除 stash

```bash
git stash apply stash@{0}
```

适合：你想先试试看恢复结果，stash 仍然保留。

### 应用并删除 stash

```bash
git stash pop stash@{0}
```

适合：你确定恢复后不再需要这份 stash。

| 命令 | 是否恢复改动 | 是否删除 stash |
|---|---|---|
| `git stash apply` | 是 | 否 |
| `git stash pop` | 是 | 是，成功应用后删除 |

新手更推荐先用 `apply`，确认没问题后再删除。

---

## 5. 删除 stash

删除指定 stash：

```bash
git stash drop stash@{0}
```

清空所有 stash：

```bash
git stash clear
```

`clear` 会删除全部 stash，通常不建议新手使用。至少先运行：

```bash
git stash list
```

确认里面没有重要现场。

---

## 6. stash 默认不保存什么？

默认 `git stash` 主要保存已跟踪文件的改动。未跟踪的新文件不一定会被保存。

如果你想连未跟踪文件一起保存：

```bash
git stash push -u -m "保存包含新文件的现场"
```

这里 `-u` 表示 include untracked。

如果新文件是构建产物、日志、依赖目录，应该先考虑 `.gitignore`，不要把垃圾文件 stash 来 stash 去。

---

## 7. stash 也可能冲突

如果你保存现场后，目标分支或当前文件又发生了变化，再应用 stash 时可能冲突。

Git 会提示类似：

```text
CONFLICT (content): Merge conflict in login.html
```

处理方式和合并冲突类似：

```bash
git status
# 打开冲突文件，整理最终内容，删除冲突标记
git add login.html
```

如果是 `stash pop` 发生冲突，Git 通常不会删除那份 stash，避免你丢现场。解决后再查看：

```bash
git stash list
```

确认是否还需要手动 `drop`。

---

## 8. stash 还是临时提交？

| 场景 | 建议 |
|---|---|
| 只是几分钟内切分支处理别的事 | stash |
| 改动还很乱，不值得进入历史 | stash |
| 改动已经有明确意义，可以描述 | 临时提交 |
| 需要和别人共享当前进度 | 提交并推送分支 |
| 可能隔几天才回来处理 | 临时提交更可靠 |

stash 是临时抽屉，不是长期仓库。不要让 `git stash list` 堆成“失物招领处”。

---

## 9. 推荐工作流

```bash
# 1. 发现要切分支，但当前有改动
git status

# 2. 保存现场
git stash push -u -m "说明这份现场是什么"

# 3. 切分支处理别的任务
git switch main

# 4. 回来继续原任务
git switch feature-login
git stash apply stash@{0}

# 5. 确认恢复没问题后删除
git stash drop stash@{0}
```

---

## 10. 本章检查点

1. `stash apply` 和 `stash pop` 有什么区别？
2. 为什么 stash 不是长期保存方案？
3. 新文件要一起 stash 时，应该加什么参数？
4. stash 冲突和 merge 冲突的处理流程有什么相同点？

---

**下一步**：[提交历史与查询](./Git教程系列-11-提交历史与查询.md)

---

**返回目录**：[README](./README.md)
