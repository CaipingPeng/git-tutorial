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
| 《Mastering Git: Understanding Git Internals and Commands》, Chris Belanger & Jawwad Ahmad | Git 内部对象模型、索引/暂存区、引用、stash 内部机制、`.gitignore` 对已跟踪文件无效的原因、历史清理、集中式/功能分支/Gitflow/fork 工作流取舍 |
| 《Advanced Git: Understanding Git Collaboration & Workflows (2nd Edition)》, Jawwad Ahmad & Chris Belanger | rebase 冲突中的 `HEAD` 视角、`git rebase --skip` 边界、`.gitignore` 事后补救、reset/reflog/revert 的撤销边界、集中式/Feature Branch/Gitflow/Forking Workflow 的团队协作取舍 |
| 《Git Essentials, Second Edition》, Ferdinando Santacroce | 提交质量与提交信息、配置层级、`push.default`、alias 边界、stash/amend/blame 的协作语境、bare 仓库、`git archive`、`git bundle`、从 SVN/旧系统迁移到 Git 的原则 |
| 《Git Notes for Professionals》, GoalKicker（Stack Overflow 文档汇编） | 命令级食谱补充：标签、`.gitattributes`、`git worktree`、`git clean`、修订号语法、`shortlog`/`.mailmap`、Git LFS、子模块/子树、bisect/blame 进阶用法 |

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

《Mastering Git》PDF 版权页允许使用或修改书中 art/images/designs，但要求保留 attribution: “Artwork/images/designs: from Mastering Git, available at www.raywenderlich.com”。本次实际检查候选图页后，未采用该书图片：多数候选图是 GitHub 页面截图、终端截图，或与当前教程已有分支/合并图重复；Git 内部对象模型和仓库维护内容改用原创中文讲解、表格和 Mermaid 图示。

《Advanced Git》PDF 版权页允许使用或修改书中 art/images/designs，但要求保留 attribution: “Artwork/images/designs: from Advanced Git, available at www.raywenderlich.com”。本次检查了集中式/分支工作流、Gitflow、Forking Workflow 和 PR 页面相关候选图；由于候选图多为英文流程图、旧版 GitHub 页面截图或与中文教程可用 Mermaid 图重复，正文未采用该书位图，也未新增图片提取脚本。相关结构和教学角度已消化为原创中文讲解、表格和 Mermaid 图示。

《Git Essentials, Second Edition》PDF 版权页显示 “Copyright © 2017 Packt Publishing. All rights reserved.”，未看到允许复用原图的开放许可说明。本次读取了目录、元数据、章节文本和图片分布，并检查了对象模型、三阶段区域、rebase/merge/cherry-pick、配置层级、提交质量、工作流和 SVN 迁移等候选图页；因候选图多为英文终端截图、旧界面截图、版权漫画或可由中文 Mermaid/表格更清楚表达，正文未采用该书位图，也未新增图片提取脚本。相关教学点已消化为原创中文讲解、表格和 Mermaid 图示。

《Git Notes for Professionals》PDF 的“About”页说明：文本内容来自 Stack Overflow 文档，按 Creative Commons BY-SA 许可发布；图片“may be copyright of their respective owners unless otherwise specified”。该书是一本命令级食谱，本教程只吸收其结构、教学角度和命令用法，原创中文重写，未复制原文段落。因其图片版权状态不明确，本次未提取、未引用该书图片；相关知识点改用原创中文讲解、表格和 Mermaid 图示。

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
