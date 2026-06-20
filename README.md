# Git 教程

这是一份面向中文读者的 Git 系统教程，目标不是让你背完命令，而是让你在真实项目里安全地使用 Git：能保存版本、读懂历史、开分支、处理冲突、同步远程、写 Pull Request，也能在出错时把自己救回来。

本教程在写作时参考了多本 Git 英文著作、Git 官方文档与主流代码托管平台文档，并以原创中文讲解重写。完整来源与逐章对照见 [参考资料](./references.md)。

---


---

## 🚀 5分钟快速入门

如果你只有5分钟，先记住这4个命令：

```bash
git status              # 看当前状态（最重要！）
git add 文件名           # 选择要保存的改动
git commit -m "说明"     # 保存版本
git log --oneline       # 看历史
```

**最小工作流程**：

```bash
# 1. 在项目文件夹运行（只需一次）
git init

# 2. 编辑文件
# （用你喜欢的编辑器修改文件）

# 3. 保存版本
git add 文件名
git commit -m "说明这次改了什么"

# 4. 查看历史
git log --oneline
```

这就是 Git 的核心！想深入学习请按章节顺序阅读。
## 适合谁阅读？

适合：

- 第一次系统学习 Git 的新手
- 会敲几个 Git 命令，但不理解背后发生了什么的人
- 经常被分支、合并、冲突、远程仓库搞混的人
- 已经进团队，但对 PR、review、rebase、撤销恢复没有把握的人
- 想建立一套安全 Git 工作流的人

不要求你已经有团队协作经验。教程默认使用命令行进行讲解，平台示例以 GitHub 为主，同时说明 GitLab/Gitee 的差异。

---

## 如何使用本教程

本教程按章节循序渐进，但不必一字不漏地读完。建议这样用：

- **跟着章节顺序做**：每章先读概念，再在独立练习目录（例如 `C:\git-practice` 或 `~/git-practice`）里动手跑一遍命令。不要在重要项目里试危险命令。
- **用每章末尾的检查点自测**：大多数章节结尾有"本章检查点"，能帮你确认是否真的理解，而不只是看懂了。
- **善用速查表和排障表**：[命令速查表](./cheatsheet.md) 按"你想做什么"组织，[常见错误排障](./troubleshooting.md) 按报错信息组织。卡住时先查这两份。
- **按学习路径跳读**：如果你不是完全新手，可以直接看下面的"推荐学习路径"，挑一条适合自己的路线，不必从头读到尾。
- **遇到危险命令先看边界**：教程会反复强调 `reset --hard`、`push --force`、rebase 公共分支等操作的边界。不确定时，优先选择更安全的方式。

---

## 课程地图

```text
本地保存版本
  → 有意义地提交
  → 分支开发
  → 合并冲突
  → 远程 hub 同步
  → PR 协作
  → 撤销恢复
  → 团队工作流
  → 综合实战
```

### 第一部分：本地仓库基础

1. [基础概念](./Git教程系列-01-基础概念.md)
   - Git 是什么
   - 快照模型、仓库、工作目录、暂存区、本地仓库
   - commit、父提交、HEAD、分支和远程仓库的初步印象

2. [安装与初始化](./Git教程系列-02-安装与初始化.md)
   - Windows/macOS/Linux 安装思路
   - 配置用户名、邮箱、默认分支和换行符
   - 命令行基础
   - `git init` 和 `.git` 文件夹

3. [基础操作](./Git教程系列-03-基础操作.md)
   - `git status`、`git add`、`git commit`
   - `git log`、`git show`、`git diff`
   - `.gitignore`、`git rm`、`git mv`
   - 提交粒度、提交信息和拆分改动
   - 交互式暂存：git add --patch 按块选择
   - 提交前空白检查：git diff --check

### 第二部分：分支、合并与冲突

4. [分支管理](./Git教程系列-04-分支管理.md)
   - 为什么需要分支
   - 分支是指向提交的可移动指针
   - `HEAD`、detached HEAD、创建/切换/删除分支
   - 分支命名和生命周期

5. [合并与冲突](./Git教程系列-05-合并与冲突.md)
   - 源分支和目标分支
   - fast-forward、三方合并、no-ff、squash merge
   - 合并冲突产生原因和解决流程
   - 合并前后检查清单

### 第三部分：远程协作与 PR

6. [远程协作](./Git教程系列-06-远程协作.md)
   - 本地仓库和远程仓库
   - `origin`、`upstream`、远程跟踪分支
   - HTTPS/SSH/本地协议等远程地址选择、`clone`、`push`、`fetch`、`pull`
   - 推送失败和远程分支排障

7. [变基](./Git教程系列-07-变基.md)
   - rebase 解决什么问题
   - merge 和 rebase 的区别
   - 交互式 rebase、squash/fixup/reword/drop
   - `--force-with-lease`、reflog 恢复和团队规则

8. [拉取请求](./Git教程系列-08-拉取请求.md)
   - Pull Request / Merge Request 是什么
   - 创建 PR、写好 PR、代码审查、CI 检查
   - 合并方式选择和分支清理
   - PR 落后、冲突、被要求修改时怎么办

### 第四部分：救援、效率与团队协作

9. [撤销与恢复](./Git教程系列-09-撤销与恢复.md)
   - 未暂存、已暂存、已提交、已推送分别怎么撤销
   - `restore`、`reset`、`revert`、`reflog`
   - 安全撤销决策树

10. [暂存与保存现场](./Git教程系列-10-暂存与保存现场.md)
    - `git stash` 保存现场
    - `apply`、`pop`、`drop`、`stash branch`、stash 冲突
    - stash 和临时提交怎么选
    - assume-unchanged/skip-worktree 忽略本地文件改动

11. [提交历史与查询](./Git教程系列-11-提交历史与查询.md)
    - `log`、`show`、`grep`、`blame`、`bisect`
    - 如何读历史、定位问题、找到改动原因
    - `git cherry` 判断提交是否已被吸收
    - `git tag` 标记版本、release tag 与 release branch 的区别、`git describe` 和 `git shortlog`

12. [团队工作流与分支策略](./Git教程系列-12-团队工作流与分支策略.md)
    - 集中式、Feature Branch、GitHub Flow、Git Flow、Trunk-based
    - CI 反馈、QA/集成分支和短生命周期功能分支
    - release/hotfix 分支
    - 个人分支、共享分支、公共分支的更新规则
    - 发布回流、分支保护和公共分支治理
    - Forking Workflow 的协作位置
    - 小团队、开源项目、企业项目如何选择

13. [代码评审与 PR 质量](./Git教程系列-13-代码评审与PR质量.md)
    - 好 PR 和坏 PR
    - review checklist
    - reviewer、assignee、label、milestone 等 PR 元数据
    - 作者和审查者职责
    - 合并前检查

14. [GitHub 实战与开源贡献](./Git教程系列-14-GitHub实战与开源贡献.md)
    - SSH key、fork、upstream、issue、PR
    - fork、origin、upstream 和本地 clone 的关系
    - GitHub/GitLab/Gitee 差异
    - 开源贡献完整流程、issue 和 bug report 写法

15. [Git 配置与效率工具](./Git教程系列-15-Git配置与效率工具.md)
    - 常用 config、`push.default`、alias、editor、credential helper
    - commit template 和 hooks 的本地/服务端边界
    - `.gitattributes` 统一跨平台换行与二进制规则
    - CLI、GUI、VS Code、GitHub Desktop 如何配合

### 第五部分：内部原理与综合实战

16. [Git 内部原理与仓库维护](./Git教程系列-16-Git内部原理与仓库维护.md)
    - blob、tree、commit、tag 的对象模型
    - 索引、引用、HEAD、reflog、stash、FETCH_HEAD、ORIG_HEAD
    - 用 `rev-parse`、`cat-file`、`ls-tree`、`ls-files --stage` 观察仓库内部状态
    - 修订号语法（`HEAD~`、`^`、`@{n}`）和 `git worktree` 多工作目录
    - submodule、subtree 与 patch 工作流的适用边界
    - `.gitignore` 对已跟踪文件无效的原因和事后补救边界
    - bare 仓库、archive、bundle、迁移和历史清理的安全边界

    - 从零创建练习项目
    - 分支、冲突、远程、PR、review、stash、清理
    - 故意犯错并用 reflog 恢复


---

## 实用资源

本教程配套以下实用资源，帮助你更高效地学习和使用 Git：

### 快速参考

- **[命令速查表](./cheatsheet.md)** - 按功能组织的常用命令，包含新手10大命令和每日工作流
- **[术语对照表](./术语对照表.md)** - 50+ Git 中英文术语对照，帮助阅读英文资料
- **[危险命令参考](./危险命令参考.md)** - 详解高危命令的风险、使用边界和安全替代方案

### 问题排查

- **[常见错误排障](./troubleshooting.md)** - 按错误信息组织的解决方案，包含10+实战场景
- 排障思维流程图和求助前检查清单

### 深度学习

- **[参考资料](./references.md)** - 完整的参考书籍和文档来源

---
### 附录

- [命令速查表](./cheatsheet.md) - 按场景查找命令
- [常见错误排障](./troubleshooting.md) - 按错误信息查找解决方案
- [常见误解澄清](./Git常见误解澄清.md) - 10个最常见的Git误解 ⭐ 新增
- [参考资料](./references.md) - 完整的参考书籍和文档来源

## 审阅报告

本教程经过系统审阅，与 Git 官方文档对照验证：

- [优化执行摘要](./优化执行摘要.md) - 快速了解教程质量和优化建议
- [深度审阅报告](./Git教程深度审阅报告-2026-06-21.md) - 详细的技术审阅和修改建议

---

### 以下是原有的附录链接（保持不变）

- [命令速查表(./cheatsheet.md)
- [常见错误排障](./troubleshooting.md)
- [参考资料](./references.md)

---

## 推荐学习路径

### 路径 A：完全新手

```text
01 → 02 → 03 → 04 → 05 → 06 → 08 → 09
```

先把本地提交、分支、合并、远程和 PR 跑通，再学救援和综合实战。第 7 章 rebase 是进阶协作工具，完全新手可以先跳过，等能看懂 PR 和推送拒绝后再回来读。读到第 12 章团队工作流时若遇到 rebase 相关概念，可回看第 7 章。

### 路径 B：会基础命令但经常出错

```text
03 → 04 → 05 → 09 → troubleshooting → 10 → 11
```

重点补暂存区、分支指针、冲突、撤销恢复和错误信息判断。

### 路径 C：准备进入团队协作

```text
06 → 08 → 07 → 12 → 13 → 14
```

重点理解远程分支、PR、rebase 边界、review 和团队工作流。

### 路径 D：想补 Git 内部原理

```text
01 → 03 → 04 → 09 → 10 → 11 → 16
```

重点理解对象模型、索引、引用、reflog、stash、忽略规则和仓库维护。

---

## 核心心智模型

### Git 是快照系统

Git 每次提交保存的是项目在某一刻的快照，而不是简单保存“这次改了几行”。理解快照模型后，分支、恢复和历史查询都会更自然。

### 版本控制是可信系统

Git 不是把 `最终版2` 变成更漂亮的文件名，而是帮你建立一套可以信任的工作习惯：什么时候保存、保存了什么、为什么这样改、以后怎么找回。提交太少，历史帮不上忙；提交太乱，历史也会失去解释力。

### 本地保存版本

```text
工作目录 → git add → 暂存区 → git commit → 本地仓库
```

远程协作时再加一层：

```text
本地仓库 → git push → 远程仓库
远程仓库 → git fetch / git pull → 本地仓库
```

`git commit` 和 `git push` 是两个动作。前者保存到自己电脑上的仓库，后者才把提交同步给远程仓库。

### 分支开发

```text
main 稳定主线
  └── feature 分支开发新功能
```

### 合并改动

```text
git switch 目标分支
git merge 源分支
```

### 远程同步

```text
本地仓库 ← git fetch / git pull → 远程仓库
本地仓库 → git push → 远程仓库
```

团队通常把 GitHub/GitLab/Gitee 上的仓库当作 hub：每个人先和 hub 同步，而不是互相直接拷贝文件。这个中心地位主要是团队约定，技术上每个克隆下来的仓库仍然保存完整历史。

### PR 协作

```text
创建功能分支 → 提交 → 推送 → 创建 PR → 审查 → 合并 → 清理分支
```

---

## 危险命令先认识

这些命令不是不能学，而是必须知道边界：

| 命令 | 风险 | 新手原则 |
|---|---|---|
| `git reset --hard` | 丢弃工作目录和暂存区改动 | 先看 `git status`，确认不要这些改动 |
| `git clean -fd` | 删除未跟踪文件 | 先用 `git clean -nd` 预览 |
| `git push --force` | 可能覆盖别人远程历史 | 团队中优先不要用，必要时用 `--force-with-lease` 并确认规则 |
| `git rebase` | 会重写当前分支提交 | 只对自己的分支谨慎使用 |
| `git branch -D` | 强制删除未合并分支 | 先确认提交能从其他分支或 reflog 找回 |

详细撤销恢复见 [撤销与恢复](./Git教程系列-09-撤销与恢复.md)。

---

## 学习建议

1. 每学一个命令，都问自己：它解决什么问题？它改变了哪个区域？
2. 多用 `git status`，它通常会告诉你下一步该做什么。
3. 合并前先确认自己在哪个分支。
4. 冲突不是错误，只是 Git 需要你决定最终内容。
5. 不确定是否会影响别人时，不要强推，不要随便 rebase 公共分支。
6. 练习命令时使用独立目录，例如 `C:\git-practice` 或 `~/git-practice`，不要在重要项目里试危险命令。

---

## 维护与反馈

Git 命令本身相对稳定，但 GitHub、GitLab、Gitee 的页面入口、权限策略和默认分支规则可能变化。阅读平台相关章节时，如果发现页面名称或流程和当前平台不一致，优先以平台官方文档为准，并回到本教程对应章节更新示例。

---

## 外部资源

- Git 官方文档：`https://git-scm.com/book/zh/v2`
- Git 官方参考手册：`https://git-scm.com/docs`
- GitHub Docs：`https://docs.github.com`
- GitLab Docs：`https://docs.gitlab.com`
- Gitee 帮助中心：`https://help.gitee.com`
- 交互式分支练习：`https://learngitbranching.js.org/`

本教程完整参考资料及逐章对照见 [参考资料](./references.md)。

---

## 许可

本教程采用 CC BY-NC-SA 4.0 许可协议。


