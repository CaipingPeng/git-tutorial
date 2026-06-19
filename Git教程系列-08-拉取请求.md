# Git 拉取请求（Pull Request）

前面你已经学过：

- 用 commit 保存版本
- 用 branch 分开工作
- 用 merge 整合分支
- 用 remote/push/fetch/pull 和远程仓库同步
- 用 rebase 整理个人分支历史

这一章讲真实团队协作中非常常见的一步：Pull Request，简称 PR。

GitHub 叫 Pull Request，GitLab 通常叫 Merge Request，简称 MR。名字不同，核心思想类似。

本章目标：

1. 理解 PR 不是 Git 命令，而是托管平台上的协作流程
2. 知道为什么团队不直接往 `main` 推代码
3. 学会从功能分支创建 PR 的完整流程
4. 理解代码审查、修改、合并和清理分支
5. 看懂 PR 中的源分支和目标分支

---

## 1. Pull Request 是什么？

Pull Request 可以理解为：

> 我在一个分支上完成了改动，请求把这些改动合并到另一个分支；在合并前，请大家先检查一下。

它不是一个普通 Git 命令。

你不会在本地终端里输入：

```bash
git pull-request
```

PR 通常是在 GitHub、GitLab、Gitee 这样的平台网页上创建的。

典型流程是：

```text
创建功能分支 → 本地开发 → commit → push 到远程 → 创建 PR → 代码审查 → 合并 → 清理分支
```

---

## 2. 为什么需要 PR？

如果每个人都直接往 `main` 推代码，会有风险：

- 没人检查代码质量
- 错误代码可能直接进入主线
- 不知道某个改动为什么要做
- 多人同时改动时难以讨论
- 主分支可能随时变得不稳定

PR 的作用是把“合并前的讨论和检查”制度化。

| 没有 PR | 有 PR |
|---|---|
| 直接把代码推到 main | 先推到功能分支 |
| 改动可能没人看 | 审查者可以逐行看 diff |
| 讨论散落在聊天软件 | 讨论集中在 PR 页面 |
| 主线更容易被破坏 | 合并前可以先测试和审查 |
| 历史缺少上下文 | PR 标题、描述、评论保留原因 |

PR 的目标不是增加麻烦，而是保护主线质量。

---

## 3. PR 里的源分支和目标分支

PR 本质上也是一次“准备合并”。

所以它也有两个重要角色：

| 角色 | 含义 | 示例 |
|---|---|---|
| 源分支 source branch | 你的改动所在分支 | `feature-login` |
| 目标分支 target/base branch | 你想合并进去的分支 | `main` |

如果你创建 PR：

```text
feature-login → main
```

意思是：

> 请求把 `feature-login` 的改动合并进 `main`。

这和第 5 章的合并方向是一致的。

---

## 4. 完整 PR 工作流

下面是一套最常见的工作流。

### 第一步：同步主分支

开始新功能前，先让本地 `main` 尽量是最新的：

```bash
git switch main
git fetch origin
git merge origin/main
```

如果你已经熟悉 `pull`，也可以：

```bash
git switch main
git pull
```

### 第二步：创建功能分支

```bash
git switch -c feature-login
```

不要直接在 `main` 上开发新功能。

### 第三步：开发并提交

修改文件后：

```bash
git status
git diff
git add login.html login.css
git commit -m "添加登录页面"
```

如果功能比较大，可以分成多次清晰提交。

### 第四步：推送功能分支

第一次推送这个分支：

```bash
git push -u origin feature-login
```

这会把本地 `feature-login` 上传到远程仓库。

### 第五步：在平台创建 PR

打开 GitHub/GitLab/Gitee 的仓库页面，通常会看到创建 PR/MR 的入口。

填写：

| 内容 | 建议 |
|---|---|
| 标题 | 简短说明改动，例如“添加登录页面” |
| 描述 | 说明为什么改、主要改了什么、怎么验证 |
| 源分支 | `feature-login` |
| 目标分支 | `main` |
| 审查者 | 指定需要看代码的人 |

如果改动还没完成，但想提前让队友看到方向，可以创建 Draft PR。Draft PR 表示“欢迎先看，但暂时不要合并”。

### 第六步：等待审查和修改

审查者可能会：

- 通过
- 留评论
- 要求修改
- 提醒你补测试或改说明

如果需要修改，不要重新创建 PR。

你只需要继续在同一个分支上提交并推送：

```bash
# 修改文件后
git add 文件名
git commit -m "根据审查意见调整登录样式"
git push
```

PR 页面会自动更新。

### 第七步：合并 PR

审查通过后，可以在平台页面点击合并。

常见合并方式包括：

| 方式 | 大致含义 |
|---|---|
| Create a merge commit | 保留分支历史，创建合并提交 |
| Squash and merge | 把多个提交压成一个提交再合并 |
| Rebase and merge | 变基后合并，让历史更线性 |

不同团队会有不同规则。新手先按团队要求来。

### 第八步：同步本地 main 并清理分支

PR 合并后，你本地的 `main` 还不知道远程已经更新。

同步：

```bash
git switch main
git fetch origin
git merge origin/main
```

删除本地功能分支：

```bash
git branch -d feature-login
```

如果远程功能分支已经在平台上删除，本地还显示远程引用，可以清理：

```bash
git fetch -p
```

---

## 5. PR 不是 pull

很多新手会被名字迷惑。

Pull Request 里面有 `pull`，但它不是 `git pull`。

| 名称 | 类型 | 含义 |
|---|---|---|
| `git pull` | Git 命令 | 从远程下载并合并到本地 |
| Pull Request | 平台协作流程 | 请求把一个分支合并到另一个分支 |

可以这样记：

> `git pull` 是你把远程更新拉到本地；Pull Request 是你请求别人把你的分支合进去。

---

## 6. PR 页面主要看什么？

不同平台界面不同，但通常都有这些内容：

| 区域 | 作用 |
|---|---|
| Conversation / Discussion | 讨论区，说明问题和审查意见 |
| Commits | 这个 PR 包含哪些提交 |
| Files changed / Changes | 具体改了哪些文件、哪些行 |
| Checks / CI | 自动测试、构建、代码检查结果 |
| Reviewers | 谁负责审查 |
| Merge button | 审查通过后合并入口 |

审查代码时，重点通常看 `Files changed`。

它本质上就是平台帮你展示了类似 `git diff` 的结果。

### CI 和分支保护

团队项目里，PR 通常还会有自动检查：

| 名称 | 含义 |
|---|---|
| CI | 自动运行测试、构建、格式检查或安全扫描 |
| required checks | 必须通过的检查 |
| branch protection | 保护 `main` 等重要分支，限制直接推送或强制要求 review |

如果 PR 页面显示检查失败，不要只想着“怎么绕过”。先点开失败日志，判断是代码问题、测试问题还是环境问题。

---

## 7. PR 描述应该写什么？

第 8 章只要求你能把 PR 创建出来，所以这里先掌握最小可用描述。更完整的标题、模板、review checklist 放到 [代码评审与 PR 质量](./Git教程系列-13-代码评审与PR质量.md) 再细讲。

入门阶段，一个 PR 描述至少回答三件事：

| 问题 | 示例 |
|---|---|
| 做了什么？ | 添加登录页面和入口链接 |
| 为什么做？ | 为后续用户登录流程准备页面基础 |
| 怎么验证？ | 打开首页，点击登录入口，确认能看到登录页面 |

不一定每次都写得很长。重点是让审查者不用猜：这个 PR 的目的、主要改动和验证方式是什么。

---

## 8. 审查意见来了怎么办？

收到审查意见很正常，不代表你写得差。

常见处理方式：

| 审查意见 | 你可以怎么做 |
|---|---|
| 发现 bug | 修改后提交并 push |
| 建议重命名 | 判断合理就修改，不确定就回复讨论 |
| 要求补说明 | 更新 PR 描述或代码注释 |
| 要求拆分 PR | 和团队确认范围，必要时拆分 |
| 不理解你的实现 | 解释原因，或改成更清楚的实现 |

修改后：

```bash
git add 文件名
git commit -m "根据审查意见调整实现"
git push
```

PR 会自动包含新提交。

---

## 9. 合并前发现 main 更新了怎么办？

你创建 PR 后，别人可能先把其他 PR 合进了 `main`。

这时你的分支可能落后于 `main`。

常见处理方式有两种：

### 方式一：merge 最新 main

```bash
git switch feature-login
git fetch origin
git merge origin/main
git push
```

这会在你的功能分支里合入最新 `main`。

### 方式二：rebase 到最新 main（进阶）

有些团队会要求用 rebase 更新 PR 分支，让历史更线性：

```bash
git switch feature-login
git fetch origin
git rebase origin/main
```

如果这个分支已经推送到远程，rebase 后可能需要特殊推送，例如：

```bash
git push --force-with-lease
```

但这涉及改写远程分支历史。即使 `--force-with-lease` 比普通 `--force` 更安全，也不应该作为新手默认操作。

> 是否使用 rebase 和 force-with-lease 更新 PR 分支，要看团队规则。不了解时优先使用方式一：merge 最新 main。

---

## 10. PR 合并后为什么还要清理？

功能分支完成并合并后，如果一直不删，分支会越来越多。

通常要清理两处：

1. 远程功能分支
2. 本地功能分支

平台上合并 PR 后，通常会提供按钮删除远程分支。

本地删除：

```bash
git switch main
git branch -d feature-login
```

清理远程分支引用：

```bash
git fetch -p
```

这样本地分支列表会更干净。

---

## 11. 一个从开发到合并的完整例子

```bash
# 1. 回到 main
git switch main

# 2. 同步远程 main
git fetch origin
git merge origin/main

# 3. 创建功能分支
git switch -c feature-login

# 4. 开发后检查状态
git status
git diff

# 5. 提交
git add login.html login.css
git commit -m "添加登录页面"

# 6. 推送功能分支
git push -u origin feature-login
```

然后去 GitHub/GitLab/Gitee 页面创建 PR：

```text
source branch: feature-login
target branch: main
```

如果审查要求修改：

```bash
# 继续在 feature-login 上改
git add login.html
git commit -m "根据审查意见调整登录页面"
git push
```

PR 合并后：

```bash
git switch main
git fetch origin
git merge origin/main
git branch -d feature-login
git fetch -p
```

---

## 12. 常见误解

| 误解 | 正确理解 |
|---|---|
| PR 是 Git 命令 | 不是。它是 GitHub/GitLab/Gitee 等平台上的协作流程 |
| PR 和 `git pull` 是一回事 | 不是。名字像，但含义不同 |
| 创建 PR 后不能再改 | 可以。继续向同一分支 push，PR 会更新 |
| PR 合并后本地 main 会自动更新 | 不会。你还需要 fetch/merge 或 pull |
| PR 合并后功能分支必须永远保留 | 不需要。通常会删除已合并分支 |
| 所有项目都用同一种合并方式 | 不一定。团队可能选择 merge、squash 或 rebase |

---

## 13. 本章命令速查表

| 命令 | 作用 | 什么时候用 |
|---|---|---|
| `git switch main` | 切回主分支 | 开始新功能前、PR 合并后 |
| `git fetch origin` | 获取远程更新 | 同步远程状态前 |
| `git merge origin/main` | 把远程 main 合进当前分支 | 更新本地 main 或功能分支时 |
| `git switch -c 分支名` | 创建功能分支 | 开始新任务时 |
| `git push -u origin 分支名` | 推送功能分支并设置上游 | 第一次推送 PR 分支时 |
| `git push` | 推送后续提交 | PR 修改后更新远程分支 |
| `git branch -d 分支名` | 删除本地已合并分支 | PR 合并后清理 |
| `git fetch -p` | 清理远程分支引用 | 远程分支已删除后 |

---

## 14. 本章总结

Pull Request 把前面学过的知识串起来了：

1. 用分支隔离开发。
2. 用 commit 保存清晰的改动。
3. 用 push 把功能分支上传到远程。
4. 在平台上创建 PR，请求合并到目标分支。
5. 通过审查、讨论和自动检查保护主分支质量。
6. 合并后同步本地并清理分支。

学到这里，你已经掌握了 Git 新手阶段最重要的完整路径：

```text
本地保存版本 → 分支开发 → 合并冲突 → 远程同步 → PR 协作
```

---

**下一步**：[撤销与恢复](./Git教程系列-09-撤销与恢复.md)

**进阶阅读**：[代码评审与 PR 质量](./Git教程系列-13-代码评审与PR质量.md)

---

**返回目录**：[README](./README.md)
