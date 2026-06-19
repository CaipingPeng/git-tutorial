# GitHub 实战与开源贡献

Git 是版本控制工具，GitHub/GitLab/Gitee 是代码托管平台。很多新手把它们混在一起：以为 PR 是 Git 命令，以为远程仓库就是 GitHub。本章把平台协作讲清楚。

本章目标：

1. 理解 Git、GitHub、GitLab、Gitee 的关系
2. 学会 HTTPS 与 SSH 的选择
3. 理解 fork、origin、upstream
4. 跑通开源贡献的标准流程

---

## 1. Git 和 GitHub 不是一回事

| 名称 | 它是什么 | 你用它做什么 |
|---|---|---|
| Git | 本地版本控制工具 | commit、branch、merge、rebase |
| GitHub | 代码托管平台 | 远程仓库、PR、issue、review、Actions |
| GitLab | 代码托管和 DevOps 平台 | MR、CI/CD、权限、项目管理 |
| Gitee | 中文代码托管平台 | 仓库、Pull Request、企业协作 |

即使没有 GitHub，你仍然可以在本地使用 Git。即使会用 GitHub 网页，也不代表理解 Git 命令。

---

## 2. HTTPS 和 SSH 怎么选？

克隆仓库时常见两种地址。

HTTPS：

```text
https://github.com/user/project.git
```

SSH：

```text
git@github.com:user/project.git
```

| 方式 | 优点 | 注意 |
|---|---|---|
| HTTPS | 容易开始，适合新手 | 推送时通常需要 token 或凭据管理器 |
| SSH | 日常推送方便，适合长期开发 | 需要生成 SSH key 并添加到平台 |

如果你只是 clone 公共仓库学习，HTTPS 很简单。如果你要长期推送自己的项目，SSH 更顺手。

---

## 3. SSH key 基本流程

生成 key：

```bash
ssh-keygen -t ed25519 -C "you@example.com"
```

一路确认后，会生成公钥和私钥。公钥通常在：

```text
~/.ssh/id_ed25519.pub
```

把公钥内容添加到 GitHub/GitLab/Gitee 的 SSH keys 页面。

测试 GitHub 连接：

```bash
ssh -T git@github.com
```

如果提示认证成功，就可以使用 SSH 地址 clone/push。

不要把私钥 `id_ed25519` 发给别人，也不要提交进仓库。

---

## 4. origin 和 upstream

在自己的仓库里，`origin` 通常表示你主要推送的远程仓库。

在 fork 工作流里，经常有两个远程：

```text
upstream：原作者仓库
origin：你 fork 后自己账号下的仓库
```

查看：

```bash
git remote -v
```

添加 upstream：

```bash
git remote add upstream 原项目URL
```

同步原项目更新：

```bash
git fetch upstream
git switch main
git merge upstream/main
```

然后推到自己的 fork：

```bash
git push origin main
```

---

## 5. 开源贡献标准流程

```text
fork 原项目
  → clone 自己的 fork
  → 添加 upstream
  → 创建功能分支
  → 修改并提交
  → 推送到 origin
  → 创建 PR 到 upstream
  → 根据 review 修改
  → 合并后同步本地
```

命令示例：

```bash
git clone git@github.com:your-name/project.git
cd project
git remote add upstream git@github.com:original-owner/project.git
git fetch upstream
git switch main
git merge upstream/main
git switch -c fix-doc-typo
# 修改文件
git add README.md
git commit -m "修正文档拼写错误"
git push -u origin fix-doc-typo
```

然后在平台网页上创建 PR：

```text
your-name:fix-doc-typo → original-owner:main
```

---

## 6. issue、PR 和 review 的关系

| 平台功能 | 用途 |
|---|---|
| issue | 记录问题、需求、讨论 |
| PR/MR | 请求把代码改动合入目标分支 |
| review | 对 PR 进行审查和反馈 |
| CI | 自动运行测试、构建、检查 |
| branch protection | 限制谁能合并、要求检查通过 |

开源项目通常希望你先看贡献指南，再提交 PR。常见文件名：

```text
CONTRIBUTING.md
CODE_OF_CONDUCT.md
README.md
```

---

## 7. GitHub、GitLab、Gitee 的差异

| 平台 | 合并请求名称 | 常见特点 |
|---|---|---|
| GitHub | Pull Request | 开源生态强，Actions 常用于 CI |
| GitLab | Merge Request | CI/CD 与权限体系集成较深 |
| Gitee | Pull Request | 中文用户友好，国内访问更方便 |

命令层面几乎一样：clone、push、fetch、pull 仍然是 Git 命令。差异主要在网页、权限、CI 和审查流程。

---

## 8. 开源贡献礼仪

1. 先读 README 和贡献指南。
2. 小改动可以直接 PR，大改动先开 issue 讨论。
3. PR 描述写清楚背景和验证。
4. 不要催维护者立刻合并。
5. review 要求修改时，继续在同一分支提交并 push。
6. 不要把 unrelated changes 混进 PR。

开源贡献不是“我提交了你必须收”。维护者要对项目长期质量负责。

---

## 9. 本章检查点

1. Git 和 GitHub 的区别是什么？
2. fork 工作流里 origin 和 upstream 分别是什么？
3. 为什么私钥不能提交到仓库？
4. 开源 PR 前应该先看哪些文件？

---

**下一步**：[Git 配置与效率工具](./15-Git配置与效率工具.md)

---

**返回目录**：[README](./README.md)
