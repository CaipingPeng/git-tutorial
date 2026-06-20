# Git 综合实战项目

这一章把前面学过的知识串起来。你会从零创建一个练习项目，经历提交、分支、冲突、远程、PR、review 修改、清理分支和 reflog 救援。

本章目标：

1. 用一条完整主线练习 Git 日常工作流
2. 故意制造一次冲突并解决
3. 理解远程和 PR 在真实流程中的位置
4. 故意犯错，并用 reflog 找回提交

建议在独立练习目录运行，不要在重要项目里试：

```text
C:\git-practice
```

或：

```text
~/git-practice
```

---

## 1. 创建练习项目

```bash
mkdir git-practice
cd git-practice
git init -b main
```

创建文件：

```text
README.md
notes.md
```

`README.md` 内容：

```markdown
# Git Practice

这是一个 Git 综合练习项目。
```

`notes.md` 内容：

```markdown
# Notes

- 初始化项目
```

提交：

```bash
git status
git add README.md notes.md
git commit -m "初始化练习项目"
```

---

## 2. 添加 `.gitignore`

创建 `.gitignore`：

```text
*.log
.env
node_modules/
dist/
```

提交：

```bash
git add .gitignore
git commit -m "添加 Git 忽略规则"
```

检查：创建一个 `debug.log`，运行 `git status`，它不应该出现在待提交列表里。

---

## 3. 创建功能分支

```bash
git switch -c feature/daily-notes
```

修改 `notes.md`：

```markdown
# Notes

- 初始化项目
- 添加每日记录功能
```

提交：

```bash
git add notes.md
git commit -m "添加每日记录说明"
```

查看分支图：

```bash
git log --oneline --graph --all --decorate
```

---

## 4. 制造并解决冲突

切回 `main`：

```bash
git switch main
```

把 `notes.md` 改成：

```markdown
# Notes

- 初始化项目
- 添加项目待办列表
```

提交：

```bash
git add notes.md
git commit -m "添加项目待办说明"
```

现在合并功能分支：

```bash
git merge feature/daily-notes
```

你应该会看到冲突。打开 `notes.md`，整理成最终内容：

```markdown
# Notes

- 初始化项目
- 添加项目待办列表
- 添加每日记录功能
```

完成合并：

```bash
git add notes.md
git commit -m "合并每日记录功能"
```

---

## 5. 清理本地分支

```bash
git branch -d feature/daily-notes
```

查看分支：

```bash
git branch
```

只剩 `main` 即可。

---

## 6. 连接远程仓库

在 GitHub/GitLab/Gitee 上创建一个空仓库，不要勾选自动生成 README，避免 unrelated histories。

添加远程：

```bash
git remote add origin 你的仓库URL
git push -u origin main
```

如果你只是本地练习，也可以跳过远程和 PR 步骤。

---

## 7. 模拟 PR 工作流

创建新分支：

```bash
git switch -c feature/readme-guide
```

修改 `README.md`，添加：

```markdown
## 使用方式

这个项目用于练习 Git 提交、分支、合并和恢复。
```

提交并推送：

```bash
git add README.md
git commit -m "补充项目使用方式"
git push -u origin feature/readme-guide
```

在平台网页创建 PR：

```text
feature/readme-guide → main
```

PR 描述写明：

- 为什么补充说明
- 改了哪个文件
- 如何验证：阅读 README

---

## 8. 模拟 review 修改

假设 reviewer 说：“说明再具体一点。”

继续在同一分支修改 `README.md`，然后：

```bash
git add README.md
git commit -m "根据评审意见完善使用说明"
git push
```

PR 页面会自动更新。不需要重新创建 PR。

合并 PR 后，本地同步：

```bash
git switch main
git fetch origin
git merge origin/main
git branch -d feature/readme-guide
git fetch -p
```

---

## 9. 故意犯错并用 reflog 救回

创建一次提交：

```bash
echo "临时实验" >> notes.md
git add notes.md
git commit -m "临时实验提交"
```

查看最近历史：

```bash
git log --oneline -3
```

现在故意 reset：

```bash
git reset --hard HEAD~1
```

最近提交从分支上消失了。用 reflog 找：

```bash
git reflog
```

找到类似：

```text
abc1234 HEAD@{1}: commit: 临时实验提交
```

创建救援分支：

```bash
git switch -c rescue-experiment abc1234
```

现在提交又被分支保护起来了。

---

## 9.5 中途切分支：用 stash 保存现场

真实开发里经常遇到这种情况：你在功能分支改到一半，还没准备好提交，突然需要切回 `main` 修一个紧急问题。直接切分支会被 Git 拦下，因为未提交的改动可能被覆盖。

先制造这个场景。切到功能分支并做未提交改动：

```bash
git switch -c feature/quick-note
echo "还没写完的草稿" >> notes.md
git status
```

此时 `notes.md` 有未暂存改动。现在假设要紧急切回 `main`，先把现场存起来：

```bash
git stash push -u -m "quick-note 草稿"
```

`-u` 让 stash 连未跟踪文件一起保存。存完后工作目录变干净，可以安全切分支：

```bash
git switch main
```

在 `main` 上处理完紧急事务并提交后，回到功能分支恢复现场：

```bash
git switch feature/quick-note
git stash pop
```

`pop` 会恢复改动并删除该 stash。如果恢复时遇到冲突（比如你刚才在 `main` 上也改了同一处），Git 会保留 stash 不删除，等你解决冲突后手动 `git stash drop`。

判断要点：

| 情况 | 建议 |
|---|---|
| 改动已经能说清楚，只是还没提交 | 优先正常 `git commit`，stash 留给真正没写完的现场 |
| 改动半成品，但必须马上切分支 | `git stash push -u -m "说明"` |
| 不确定 stash 里存了什么 | `git stash list` 看列表，`git stash show -p stash@{0}` 看内容 |
| stash 堆了很多条 | 不要长期囤积，要么 pop 回去继续做，要么 `git stash branch` 转成正式分支 |

stash 是临时抽屉，不是长期仓库。每条 stash 都应该尽快被 pop 或转成分支，不要让它堆成“失物招领处”。

---

## 10. 完整检查清单

完成本章后，你应该做过：

- [ ] 初始化仓库
- [ ] 创建 `.gitignore`
- [ ] 提交多个版本
- [ ] 创建功能分支
- [ ] 制造并解决冲突
- [ ] 合并并删除分支
- [ ] 连接远程仓库
- [ ] 创建 PR
- [ ] 根据 review 修改并推送
- [ ] 用 reflog 找回提交
- [ ] 用 stash 保存中途现场并恢复

如果这些都能独立完成，你已经不是“只会背命令”的 Git 新手了。

---

## 11. 下一步怎么练？

1. 把本章项目重做一遍，但换成自己的文件名。
2. 重做 9.5 节的 stash 场景，但这次在 `main` 上也改 `notes.md` 同一行，制造恢复冲突。
3. 用 `git rebase -i` 把两个小提交 squash 成一个。
4. 和朋友互相 fork 仓库，练习真正的 PR review。
5. 读 [常见错误排障](./troubleshooting.md)，把每个错误至少理解一遍。

---

**返回目录**：[README](./README.md)
