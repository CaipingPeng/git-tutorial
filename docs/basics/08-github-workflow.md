# 08. GitHub 工作流

> 15 分钟学会 Fork、Pull Request 和开源贡献

这是基础教程的最后一章,学完你就能参与开源项目了!

## Fork 工作流

GitHub 上最常用的协作方式就是 Fork + Pull Request。

### 完整流程

```
1. Fork      →  2. Clone    →  3. Branch   →  4. Commit
   (GitHub)       (本地)          (本地)          (本地)
                                                    ↓
8. Merge     ←  7. Review   ←  6. PR       ←  5. Push
   (GitHub)       (GitHub)        (GitHub)        (GitHub)
```

## 步骤详解

### 1. Fork 项目

在 GitHub 项目页面,点击右上角的 "Fork" 按钮。

**效果**: 在你的账号下创建一个副本。

```
原始仓库: github.com/original/repo
你的 Fork: github.com/yourname/repo
```

### 2. Clone 到本地

```bash
git clone https://github.com/yourname/repo.git
cd repo
```

### 3. 添加上游仓库

```bash
git remote add upstream https://github.com/original/repo.git
```

现在有两个远程:
- `origin`: 你的 Fork
- `upstream`: 原始仓库

### 4. 创建功能分支

```bash
git switch -c fix-typo
```

**永远不要在 main 分支上直接修改!**

### 5. 修改、提交、推送

```bash
# 修改文件
vim README.md

# 提交
git add README.md
git commit -m "Fix typo in README"

# 推送到你的 Fork
git push -u origin fix-typo
```

### 6. 创建 Pull Request

1. 访问你的 Fork 页面
2. 点击 "Compare & pull request"
3. 填写 PR 标题和描述
4. 点击 "Create pull request"

**好的 PR 描述**:
```markdown
## 改动说明
修复了 README 中的拼写错误

## 改动内容
- 第10行: "recieve" → "receive"
- 第15行: "occured" → "occurred"

## 测试
已检查所有拼写
```

### 7. 代码审查

项目维护者会审查你的代码:
- 提出修改建议
- 批准合并
- 或者拒绝

如果需要修改:
```bash
# 在同一个分支继续修改
vim README.md
git add README.md
git commit -m "Address review comments"
git push
```

PR 会自动更新。

### 8. 合并

维护者合并你的 PR 后:
```bash
# 切回 main
git switch main

# 从上游拉取更新
git pull upstream main

# 推送到你的 Fork
git push origin main

# 删除功能分支
git branch -d fix-typo
git push origin --delete fix-typo
```

## 保持同步

### 定期同步上游

```bash
# 获取上游更新
git fetch upstream

# 切换到 main
git switch main

# 合并上游 main
git merge upstream/main

# 推送到你的 Fork
git push origin main
```

**建议**: 每次开始新功能前都同步一次。

## Issue 管理

### 提交 Issue

在项目页面点击 "Issues" → "New issue"。

**好的 Issue**:
```markdown
## 问题描述
运行 `npm start` 时报错

## 重现步骤
1. git clone repo
2. npm install
3. npm start

## 错误信息
```
Error: Cannot find module 'express'
```

## 环境信息
- OS: macOS 13.0
- Node: v18.0.0
- npm: 9.0.0
```

### 关联 Issue

提交 PR 时,可以关联 Issue:
```markdown
Fix typo in README

Closes #123
```

PR 合并后,Issue 自动关闭。

## Pull Request 最佳实践

### 1. 保持 PR 小而专注

❌ 不好:
```
- 修复 bug
- 添加新功能
- 重构代码
- 更新文档
```

✅ 好:
```
- 只修复一个 bug
```

### 2. 写清楚的描述

❌ 不好:
```
fix bug
```

✅ 好:
```
Fix null pointer exception in UserService

When user.email is null, UserService.sendEmail() 
throws NullPointerException. This PR adds null check.

Fixes #123
```

### 3. 提交历史清晰

❌ 不好:
```
- fix
- fix again
- oops
- final fix
```

✅ 好:
```
- Fix null pointer exception in UserService
```

可以用 `git commit --amend` 或 `git rebase -i` 整理提交。

### 4. 及时回应审查

- 维护者提出问题,尽快回复
- 被拒绝不要气馁,询问原因
- 按建议修改代码

## 贡献代码清单

开始贡献前,检查这些:

- [ ] 阅读了 CONTRIBUTING.md
- [ ] 遵守了代码风格
- [ ] 通过了所有测试
- [ ] 更新了文档
- [ ] 提交信息清晰
- [ ] PR 描述完整

## 你只需要记住这 3 点

1. **Fork → Clone**: 复制项目到本地
2. **Branch → Commit → Push**: 在分支上开发
3. **Pull Request**: 提交合并请求

## 练习

1. Fork 一个开源项目(如 first-contributions)
2. Clone 到本地
3. 创建分支,修改 README
4. 提交 Pull Request

推荐练习项目:
- [first-contributions](https://github.com/firstcontributions/first-contributions)
- [awesome-for-beginners](https://github.com/MunGell/awesome-for-beginners)

## 恭喜!

完成了基础教程的全部 8 章,你现在可以:

✅ 理解 Git 的核心概念
✅ 独立管理代码版本
✅ 使用分支并行开发
✅ 与团队协作
✅ 解决合并冲突
✅ 撤销各种错误
✅ 参与开源项目

## 下一步

**继续学习**:
- [进阶教程](../advanced/README.md) - 深入原理和高级技巧
- [命令速查表](../appendix/cheatsheet.md) - 快速参考
- [常见问题](../appendix/troubleshooting.md) - 故障排查

**实践项目**:
- 创建自己的项目
- 贡献开源项目
- 帮助队友解决 Git 问题

---

**感谢学习!**

如果这套教程对你有帮助,欢迎:
- ⭐ Star 这个项目
- 📢 分享给朋友
- 🐛 提交 Issue 和 PR
