# 参考资料

本教程参考资料的使用原则：吸收主题覆盖、教学路径和实践重点，用原创中文重新组织；不复制书中段落或练习。少量图片仅在对应书籍许可允许时使用，并保留必要署名。

## 本地参考书籍

以下书籍来自本仓库的 `referencesBook/` 目录，只使用用户允许参考的 Git 书籍。

| 资料 | 本教程借鉴的方向 |
|---|---|
| 《Git for Teams: A User-Centered Approach to Creating Efficient Workflows in Git》 | 团队协作、分支策略、代码评审、PR 流程、工作流选择 |
| 《Git Learn Version Control with Git: A step-by-step Ultimate beginners Guide》 | Git 基础概念、生命周期、常用操作、stash、reset、tag、错误修复 |
| 《Git Mastery Accelerated Crash Course》 | 安装配置、SSH、`.gitignore`、GitHub、rebase、stash、hooks、常见问题排障 |
| 《Git Prodigy: Mastering Version Control with Git and GitHub》 | Git/GitHub 实战、CLI/GUI 配合、开源贡献、分支与合并实践 |
| 《Learning Git A Hands-On and Visual Guide to the Basics of Git》 | 可视化理解快照、分支、合并和基础命令 |
| 《Git Apprentice: Getting Started with Git Commands & Concepts》 | 入门路径、暂存区、`git log` 查询、分支/合并图、远程同步与多 remote 场景 |
| 《Learn Git The Hard Way》, Ian Miell | 四阶段内容流转、分布式仓库平等模型、命令行实操顺序、push 被拒绝诊断、rebase/squash/force push 协作风险、reflog 救援、cherry-pick 和 hooks 边界 |

## 图片署名

本教程使用的以下图片来自 《Git Apprentice: Getting Started with Git Commands & Concepts》：

- `assets/git-apprentice-staging-area-files.png`
- `assets/git-apprentice-staging-area-selection.png`
- `assets/git-apprentice-branch-history.png`
- `assets/git-apprentice-fast-forward-merge.png`
- `assets/git-apprentice-three-way-merge.png`

Attribution: Artwork/images/designs: from Git Apprentice, available at www.raywenderlich.com.

`assets/image-20260609170357060.png`、`assets/image-20260608215317639.png`、`assets/image-20260608221704134.png` 是本教程配套的 Windows 操作截图，用于说明安装后菜单和 `.git` 隐藏目录查看方式。

《Learn Git The Hard Way》PDF 版权页显示 “© 2018 - 2020 Ian Miell”，未在本地 PDF 中看到允许复用原图的开放许可说明。因此本次未提取、未引用该书原图；相关教学点改为原创中文讲解、Markdown 表格和 Mermaid 图示。

## 官方与平台资料

| 资料 | 用途 |
|---|---|
| Git 官方书籍 Pro Git：`https://git-scm.com/book/zh/v2` | 概念、命令语义、分支、远程、变基等基础依据 |
| Git 官方参考手册：`https://git-scm.com/docs` | 命令参数、边界条件和准确表述 |
| GitHub Docs：`https://docs.github.com` | Pull Request、fork、SSH、branch protection、review、Actions 基础 |
| GitLab Docs：`https://docs.gitlab.com` | Merge Request、CI、分支保护差异说明 |
| Gitee 帮助中心：`https://help.gitee.com` | 中文平台用户的仓库、PR/合并请求和 SSH 使用差异 |

## 版本与平台假设

- 教程命令默认使用较新的 Git 2.x。
- 切换分支优先使用 `git switch`，同时说明老教程中的 `git checkout`。
- 默认主分支名使用 `main`；遇到老项目的 `master` 时，把它理解为主分支名称即可。
- 命令行示例以 Git Bash / macOS Terminal / Linux shell 为主。
- 平台协作示例以 GitHub 为主，必要时标注 GitLab 的 Merge Request 和 Gitee 差异。

---

**返回目录**：[README](./README.md)
