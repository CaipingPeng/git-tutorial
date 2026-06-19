# Git 教程

这是一份面向中文读者的 Git 系统教程，目标不是让你背完命令，而是让你在真实项目里安全地使用 Git：能保存版本、读懂历史、开分支、处理冲突、同步远程、写 Pull Request，也能在出错时把自己救回来。

本教程参考了以下允许使用的资料方向，并以原创中文讲解重写：

- 《Learning Git A Hands-On and Visual Guide to the Basics of Git》
- 《Git Apprentice: Getting Started with Git Commands & Concepts》：入门路径、暂存区、分支图、合并图和远程同步案例。
- 《Git for Teams》：团队工作流、分支策略、评审和协作规则。
- 《Git Learn Version Control with Git》：基础概念、生命周期、常见命令和错误修复。
- 《Git Mastery Accelerated Crash Course》：安装配置、SSH、`.gitignore`、stash、rebase、hooks 和排障。
- 《Git Prodigy》：GitHub、开源贡献、CLI/GUI 协作。
- Git 官方文档与主流代码托管平台文档。
- 《Learn Git The Hard Way》：四阶段内容流转、仓库平等模型、push 失败诊断、rebase/squash/force push 风险、reflog 救援和 hooks 边界。
- 《Mastering Git》：Git 对象模型、索引、引用、stash 内部机制、`.gitignore` 失效原因、历史清理和工作流取舍。
- 《Advanced Git》：rebase 冲突视角、`.gitignore` 事后补救、reset/reflog/revert 边界，以及集中式、功能分支、Gitflow、Forking Workflow 的协作取舍。
- 《Git Essentials, Second Edition》：提交质量、配置层级、别名安全、bare/archive/bundle 备份、SVN 迁移心态和工作流选择。

完整来源说明见 [参考资料](./references.md)。

---

## 适合谁阅读？

适合：

- 第一次系统学习 Git 的新手
- 会敲几个 Git 命令，但不理解背后发生了什么的人
- 经常被分支、合并、冲突、远程仓库搞混的人
- 已经进团队，但对 PR、review、rebase、撤销恢复没有把握的人
- 想建立一套安全 Git 工作流的人

不要求你已经有团队协作经验。教程默认使用命令行进行讲解，平台示例以 GitHub 为主，同时说明 GitLab/Gitee 的差异。

---

## 课程地图

```text
本地保存版本
  → 分支开发
  → 合并冲突
  → 远程同步
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
   - HTTPS/SSH、`clone`、`push`、`fetch`、`pull`
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
    - `apply`、`pop`、`drop`、stash 冲突
    - stash 和临时提交怎么选

11. [提交历史与查询](./Git教程系列-11-提交历史与查询.md)
    - `log`、`show`、`blame`、`bisect`
    - 如何读历史、定位问题、找到改动原因

12. [团队工作流与分支策略](./Git教程系列-12-团队工作流与分支策略.md)
    - 集中式、Feature Branch、GitHub Flow、Git Flow、Trunk-based
    - release/hotfix 分支
    - 个人分支、共享分支、公共分支的更新规则
    - Forking Workflow 的协作位置
    - 小团队、开源项目、企业项目如何选择

13. [代码评审与 PR 质量](./Git教程系列-13-代码评审与PR质量.md)
    - 好 PR 和坏 PR
    - review checklist
    - 作者和审查者职责
    - 合并前检查

14. [GitHub 实战与开源贡献](./Git教程系列-14-GitHub实战与开源贡献.md)
    - SSH key、fork、upstream、issue、PR
    - fork、origin、upstream 和本地 clone 的关系
    - GitHub/GitLab/Gitee 差异
    - 开源贡献完整流程

15. [Git 配置与效率工具](./Git教程系列-15-Git配置与效率工具.md)
    - 常用 config、`push.default`、alias、editor、credential helper
    - CLI、GUI、VS Code、GitHub Desktop 如何配合
    - hooks 入门

### 第五部分：内部原理与综合实战

16. [Git 内部原理与仓库维护](./Git教程系列-16-Git内部原理与仓库维护.md)
    - blob、tree、commit、tag 的对象模型
    - 索引、引用、HEAD、reflog、stash、FETCH_HEAD、ORIG_HEAD
    - `.gitignore` 对已跟踪文件无效的原因和事后补救边界
    - bare 仓库、archive、bundle、迁移和历史清理的安全边界

17. [综合实战项目](./Git教程系列-17-综合实战项目.md)
    - 从零创建练习项目
    - 分支、冲突、远程、PR、review、清理
    - 故意犯错并用 reflog 恢复

### 附录

- [命令速查表](./cheatsheet.md)
- [常见错误排障](./troubleshooting.md)
- [参考资料](./references.md)

---

## 推荐学习路径

### 路径 A：完全新手

```text
01 → 02 → 03 → 04 → 05 → 06 → 08 → 09 → 17
```

先把本地提交、分支、合并、远程和 PR 跑通，再学救援和综合实战。

### 路径 B：会基础命令但经常出错

```text
03 → 04 → 05 → 09 → troubleshooting → 10 → 11
```

重点补暂存区、分支指针、冲突、撤销恢复和错误信息判断。

### 路径 C：准备进入团队协作

```text
06 → 08 → 07 → 12 → 13 → 14 → 17
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

## 外部资源

- Git 官方文档：`https://git-scm.com/book/zh/v2`
- Git 官方参考手册：`https://git-scm.com/docs`
- GitHub Docs：`https://docs.github.com`
- GitLab Docs：`https://docs.gitlab.com`
- Gitee 帮助中心：`https://help.gitee.com`
- 交互式分支练习：`https://learngitbranching.js.org/`
