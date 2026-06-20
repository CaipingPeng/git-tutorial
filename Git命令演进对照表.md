# Git 命令演进：checkout vs switch/restore

## 为什么有两套命令？

Git 2.23（2019年8月）引入了 git switch 和 git restore 来替代 git checkout 的部分功能。

### 历史问题

git checkout 功能太多，容易混淆：

`ash
git checkout main           # 切换分支
git checkout -b feature     # 创建并切换分支
git checkout -- file.txt    # 恢复文件
git checkout HEAD~1 file.txt # 从历史恢复文件
git checkout v1.0           # 切换到标签
git checkout abc1234        # 切换到提交（detached HEAD）
`

同一个命令，既能切换分支，又能恢复文件，新手很容易搞混。

### 解决方案

Git 团队决定把 checkout 的职责拆分：

| 旧命令 | 新命令 | 职责 |
|-------|-------|------|
| git checkout | git switch | **专注分支操作** |
| git checkout | git restore | **专注文件恢复** |

---

## 完整对照表

### 分支操作

| 旧命令（checkout） | 新命令（switch） | 作用 |
|------------------|-----------------|------|
| git checkout main | git switch main | 切换到 main 分支 |
| git checkout -b feature | git switch -c feature | 创建并切换到 feature 分支 |
| git checkout - | git switch - | 切换到上一个分支 |
| git checkout -b feature origin/feature | git switch -c feature origin/feature | 基于远程分支创建本地分支 |
| git checkout --detach | git switch --detach | 进入 detached HEAD 状态 |
| git checkout v1.0 | git switch --detach v1.0 | 切换到标签（detached HEAD）|
| git checkout abc1234 | git switch --detach abc1234 | 切换到提交（detached HEAD）|

**switch 的优势**：
- 语义清晰：专门用于切换分支
- 更安全：不会意外修改文件
- 更直观：-c 表示 create（而不是 -b 表示 branch）

---

### 文件恢复操作

| 旧命令（checkout） | 新命令（restore） | 作用 |
|------------------|------------------|------|
| git checkout -- file.txt | git restore file.txt | 恢复工作目录中的文件 |
| git checkout HEAD file.txt | git restore file.txt | 恢复文件到 HEAD 状态 |
| git checkout HEAD~1 file.txt | git restore --source=HEAD~1 file.txt | 从历史提交恢复文件 |
| git checkout . | git restore . | 恢复当前目录所有文件 |
| （不适用） | git restore --staged file.txt | 从暂存区移除文件 |

**estore 的优势**：
- 语义清晰：专门用于恢复文件
- --staged 选项直观：明确操作暂存区
- --source 选项清晰：指定恢复来源

---

### 暂存区操作

| 旧命令 | 新命令（restore） | 作用 |
|-------|------------------|------|
| git reset HEAD file.txt | git restore --staged file.txt | 从暂存区移除文件（保留工作目录改动）|
| git reset HEAD . | git restore --staged . | 移除暂存区所有文件 |

**为什么这里用 estore？**

从逻辑上说，"从暂存区移除"就是"恢复暂存区到 HEAD 的状态"，所以用 estore --staged 更语义化。

---

## 新旧命令组合对比

### 场景1：撤销对文件的修改

**旧方式**（checkout）：
`ash
# 从暂存区撤回
git reset HEAD file.txt

# 恢复文件内容
git checkout -- file.txt
`

**新方式**（restore）：
`ash
# 从暂存区撤回
git restore --staged file.txt

# 恢复文件内容
git restore file.txt
`

**优势**：统一用 estore，更一致。

---

### 场景2：创建并切换分支

**旧方式**（checkout）：
`ash
git checkout -b feature-login
`

**新方式**（switch）：
`ash
git switch -c feature-login
`

**差异**：-c 比 -b 更直观（create）。

---

### 场景3：切换到历史提交查看代码

**旧方式**（checkout）：
`ash
git checkout abc1234
`

**新方式**（switch）：
`ash
git switch --detach abc1234
`

**优势**：--detach 明确表示进入 detached HEAD，更安全。

---

## 我应该用哪套命令？

### 推荐新手直接用新命令

**理由**：
- ✅ 语义更清晰（switch = 切换，restore = 恢复）
- ✅ 不容易混淆分支操作和文件操作
- ✅ 更安全（不会因为打错字而误操作）
- ✅ 是未来趋势

### 如果你已经熟悉 checkout

可以继续用，checkout 不会被废弃。但建议：
- 新项目、新教程用新命令
- 逐步迁移到新命令
- 团队统一命令风格

### 团队协作考虑

| 情况 | 建议 |
|------|------|
| 团队用 Git < 2.23 | 统一用旧命令 |
| 团队已升级到 Git 2.23+ | 建议统一用新命令 |
| 团队有新老成员混合 | 在文档中标注两种写法 |
| 编写教程或文档 | 优先用新命令，首次出现时标注旧命令 |

---

## Git 版本要求

| 命令 | 最低 Git 版本 |
|------|-------------|
| git switch | 2.23.0（2019年8月）|
| git restore | 2.23.0（2019年8月）|

**检查你的 Git 版本**：
`ash
git --version
`

如果版本低于 2.23，建议升级：
- Windows：重新下载最新 Git for Windows
- macOS：rew upgrade git
- Linux：使用包管理器升级

---

## 常见问题

### Q1: git checkout 会被废弃吗？

**A**: 不会。Git 团队明确表示 checkout 会继续保留，以确保向后兼容。但建议新用户学习新命令。

---

### Q2: 我能混用两套命令吗？

**A**: 可以，但不建议。建议在同一个项目或团队中统一使用一套命令，避免混淆。

---

### Q3: 为什么还有很多教程用 checkout？

**A**: 因为：
1. switch 和 estore 是 2019 年才引入的
2. 很多教程编写于 2019 年之前
3. 一些老教程没有更新

本教程优先使用新命令，首次出现时会标注旧命令写法。

---

### Q4: 什么情况下必须用 checkout？

**A**: 极少数场景下仍需要 checkout，例如：
- 同时切换分支并更新子模块
- 一些复杂的 worktree 操作

但日常 99% 的场景，switch + estore 完全够用。

---

### Q5: CI/CD 脚本应该用哪套命令？

**A**: 建议：
- 如果 CI 环境的 Git 版本 >= 2.23，用新命令
- 如果需要兼容老版本 Git，用 checkout
- 在 Dockerfile 或 CI 配置中明确指定 Git 版本

---

## 快速记忆法

### 按功能分类

| 我想做什么 | 用哪个命令 |
|----------|----------|
| 切换分支 | git switch |
| 创建分支 | git switch -c |
| 恢复文件 | git restore |
| 从暂存区撤回 | git restore --staged |

### 按单词含义记忆

- **switch** = 切换（想象电灯开关）
- **restore** = 恢复（想象恢复出厂设置）

### 避免混淆

❌ **常见错误**：
`ash
git switch file.txt        # ❌ switch 只能操作分支
git restore main           # ❌ restore 只能操作文件
`

✅ **正确用法**：
`ash
git switch main            # ✅ 切换到 main 分支
git restore file.txt       # ✅ 恢复 file.txt
`

---

## 实战练习

### 练习1：分支切换

`ash
# 旧方式
git checkout main
git checkout -b feature

# 新方式
git switch main
git switch -c feature
`

### 练习2：撤销文件改动

`ash
# 修改文件
echo "test" > file.txt

# 旧方式撤销
git checkout -- file.txt

# 新方式撤销
git restore file.txt
`

### 练习3：从暂存区撤回

`ash
# 暂存文件
git add file.txt

# 旧方式撤回
git reset HEAD file.txt

# 新方式撤回
git restore --staged file.txt
`

---

## 本教程的命令选择

本教程主要使用 git switch 和 git restore，原因：

1. ✅ 更适合新手学习（语义清晰）
2. ✅ 减少混淆（分支和文件操作分离）
3. ✅ 是未来趋势（Git 官方推荐）

**首次出现时会标注旧命令等价写法**，方便从其他教程转来的读者。

---

## 相关文档

- Git 2.23 Release Notes: https://github.com/git/git/blob/master/Documentation/RelNotes/2.23.0.txt
- Git switch 文档: https://git-scm.com/docs/git-switch
- Git restore 文档: https://git-scm.com/docs/git-restore
- Git checkout 文档: https://git-scm.com/docs/git-checkout

---

**返回教程首页**：[README](./README.md)
