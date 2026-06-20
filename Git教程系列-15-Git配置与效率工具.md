# Git 配置与效率工具

Git 不只是命令本身。合适的配置、别名、编辑器、凭据管理和工具，可以减少很多低级错误。本章讲常用配置和效率工具。

本章目标：

1. 理解 Git 配置的层级
2. 配好用户名、邮箱、默认分支、换行符和编辑器
3. 认识 `push.default` 和命令纠错配置的安全边界
4. 使用 alias 简化高频命令
5. 理解 CLI、GUI、VS Code 和 hooks 的定位

---

## 1. Git 配置有层级

常见层级：

| 层级 | 命令参数 | 常见位置 | 影响范围 |
|---|---|---|---|
| system | `--system` | Git 安装目录下的 `gitconfig` | 整台机器所有用户 |
| global | `--global` | 当前用户的 `.gitconfig` | 当前用户所有仓库 |
| local | 不加参数或 `--local` | 当前仓库的 `.git/config` | 当前仓库 |

新手最常用的是 global：

```bash
git config --global user.name "你的名字"
git config --global user.email "you@example.com"
```

在公司项目需要使用公司邮箱时，可以进入那个仓库单独配置：

```bash
git config user.email "you@company.com"
```

同一个配置项出现在多个层级时，离当前仓库更近的配置优先生效：

```text
local 覆盖 global
global 覆盖 system
```

所以你在某个公司仓库里配置了 `user.email`，不会影响其他个人项目；反过来，如果某个仓库里的邮箱“不听话”，也不要只盯着 global 配置，要检查 local 配置。

---

## 2. 查看配置来自哪里

查看所有配置：

```bash
git config --list
```

查看配置和来源文件：

```bash
git config --list --show-origin
```

只看某一项来自哪里：

```bash
git config --show-origin --get user.email
```

如果某个配置看起来“不听话”，通常是 local 配置覆盖了 global 配置。

---

## 3. 默认分支名

建议把新仓库默认分支设为 `main`：

```bash
git config --global init.defaultBranch main
```

以后运行：

```bash
git init
```

新仓库默认主分支就是 `main`。

这不会自动改已有仓库的分支名。

---

## 4. Windows 换行符：`core.autocrlf`

Windows 和 Unix 系统的换行符不同，可能导致 diff 里出现大量无意义变化。

常见配置：

| 系统 | 建议 |
|---|---|
| Windows | `git config --global core.autocrlf true` |
| macOS/Linux | `git config --global core.autocrlf input` |

团队项目最好再配 `.gitattributes`，统一关键文件的换行规则。

如果你发现没改内容但 Git 显示整文件变化，优先怀疑换行符。

---

## 5. 用 `.gitattributes` 统一跨平台规则

`core.autocrlf` 是每个人本机的配置，团队成员可能各不相同。更可靠的做法是把换行规则写进仓库里的 `.gitattributes`，让规则跟着项目走，而不是跟着某台电脑走。

在仓库根目录创建 `.gitattributes`：

```text
* text=auto eol=lf
*.bat text eol=crlf
*.ps1 text eol=crlf
*.png binary
*.jpg binary
```

含义：

| 规则 | 作用 |
|---|---|
| `* text=auto eol=lf` | 让 Git 自动处理文本文件，仓库里统一存 LF |
| `*.bat text eol=crlf` | Windows 批处理脚本保持 CRLF |
| `*.png binary` | 明确告诉 Git 这是二进制文件，不要做换行转换、不要尝试 diff |

`.gitattributes` 相比 `core.autocrlf` 的优势：

| 维度 | `core.autocrlf` | `.gitattributes` |
|---|---|---|
| 作用范围 | 单台机器 | 跟随仓库，所有克隆生效 |
| 能否针对具体文件类型 | 不能 | 能 |
| 是否需要提交 | 不需要 | 需要提交进仓库 |

另一个常见用途是标记二进制文件。Git 默认会猜哪些文件是二进制，但偶尔会猜错，导致 diff 里出现乱码或无意义的“整文件变化”。在 `.gitattributes` 里显式声明 `*.png binary`、`*.xlsx binary` 可以避免这类误判。

新手建议：只要项目里有 Windows 脚本或图片等二进制资源，就尽早提交一个 `.gitattributes`，比事后到处修换行问题省事得多。

---

## 6. 默认编辑器

如果 Git 打开了你不会退出的编辑器，会很痛苦。可以指定 VS Code：

```bash
git config --global core.editor "code --wait"
```

如果使用 Vim，保存退出是：

```text
按 Esc
输入 :wq
回车
```

不想保存退出：

```text
按 Esc
输入 :q!
回车
```

---

## 7. 推送和纠错相关配置

有些配置会改变 Git 的默认行为。新手不需要一次配很多，但要认识两个容易影响安全性的选项。

### `push.default`

`push.default` 决定你只输入 `git push` 时，Git 默认推送什么。

推荐大多数新项目使用：

```bash
git config --global push.default simple
```

常见取值可以这样理解：

| 取值 | 行为 | 适合谁 |
|---|---|---|
| `simple` | 只推送当前分支到同名上游分支 | 大多数开发者 |
| `nothing` | 不指定目标就拒绝推送 | 想强制自己每次写清楚目标的人 |
| `current` | 推送当前分支到远程同名分支 | 熟悉团队规则后再考虑 |
| `matching` | 推送所有同名分支 | 新手不要用，容易把不想推的分支也推上去 |

如果你经常不确定 `git push` 会把什么推到哪里，先看：

```bash
git branch -vv
git remote -v
```

### `help.autocorrect`

Git 可以在你输错命令时自动猜测并执行，例如把 `chekcout` 猜成 `checkout`。这听起来方便，但也可能让你没看清就执行了错误命令。

如果你想开启一个短暂等待窗口：

```bash
git config --global help.autocorrect 10
```

`10` 表示等待 1 秒后执行猜测命令。按 `Ctrl+C` 可以取消。新手如果还在熟悉命令，保持默认关闭也完全可以；不要为了省一次输入，把危险操作交给自动猜测。

---

### `fetch.prune`

每次 `git fetch` 时自动清理本地已不存在的远程分支引用：

```bash
git config --global fetch.prune true
```

启用后，`git branch -r` 里不会再有那些远程早已删除的分支名。

### `color.ui`

Git 默认已开启彩色输出。如果需要在脚本中禁用颜色：

```bash
git config --global color.ui never
```

大多数情况下保留默认 `auto` 即可。

### 全局忽略文件

如果有一些文件所有仓库都想忽略（如 `.DS_Store`），可以配置全局 .gitignore：

```bash
git config --global core.excludesFile ~/.gitignore_global
```

然后在 `~/.gitignore_global` 中添加规则。

### 通过网页查看帮助

```bash
git help -w log
```

会在浏览器中打开更完整的帮助页面。

---

## 8. 常用 alias

alias 可以把长命令变短，是 Git 配置里最提升效率的功能之一。

```bash
git config --global alias.st status
git config --global alias.sw switch
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.co checkout
git config --global alias.lg "log --oneline --graph --all --decorate"
git config --global alias.last "log -1 HEAD"
git config --global alias.unstage "restore --staged --"
git config --global alias.df "diff --stat HEAD"
git config --global alias.tree "log --oneline --graph --all"
git config --global alias.pf "push --force-with-lease"
git config --global alias.pullr "pull --rebase"
git config --global alias.adp "add --patch"
git config --global alias.cip "commit --patch"
```

之后可以用：

```bash
git st
git sw main
git lg
git last
git unstage README.md
```

alias 的好处是减少重复输入，坏处是可能把命令含义藏起来。建议遵守：

| 原则 | 说明 |
|---|---|
| 先学原命令，再配别名 | 排障和看教程时仍然能听懂别人说什么 |
| 优先给只读命令配别名 | `status`、`log`、`branch` 风险低 |
| 不给危险命令起过短名字 | 不要把 `reset --hard`、`clean -fd` 包成一两个字母 |
| 团队脚本里少用个人 alias | 别人的机器上不一定有你的别名 |

有些资料会建议：

```bash
git config --global alias.undo "reset --soft HEAD~1"
```

这个别名确实能撤销最近一次本地提交，并保留改动。但它本质仍是 `reset`，新手最好先直接输入完整命令，确认自己知道它会影响哪一段历史。

Git alias 还支持用 `!` 调用外部 shell 命令。它很强，但也更难排查。学习阶段不建议把 `git add -A`、`git commit`、`git push` 串成一个“一键提交推送”别名，因为这会绕过 `status`、`diff` 和 `diff --staged` 这几个关键检查点。

不要一开始配太多 alias。先把原命令学明白，再给真正高频、低风险的命令配别名。

---

## 9. 凭据管理

HTTPS 推送通常需要 token 或凭据管理器。Windows 上 Git for Windows 常搭配 Git Credential Manager。

如果认证反复失败，检查：

```bash
git remote -v
```

确认你使用的是 HTTPS 还是 SSH。

| 问题 | 方向 |
|---|---|
| HTTPS 要用户名密码 | 平台通常要求 token，不再接受账号密码 |
| SSH Permission denied | 检查 SSH key 是否生成并添加到平台 |
| 公司电脑权限受限 | 按公司安全规范配置，不要绕过策略 |

---

## 10. CLI、GUI 和编辑器 Git 面板

| 工具 | 优点 | 注意 |
|---|---|---|
| 命令行 CLI | 精确、可复制、适合学习底层逻辑 | 新手容易输错参数 |
| VS Code Git 面板 | 看 diff、解决冲突方便 | 不要只点按钮而不知道发生了什么 |
| GitHub Desktop | 适合轻量 GitHub 工作流 | 高级操作能力有限 |
| SourceTree / Fork 等 GUI | 分支图直观 | 团队排障时仍要懂命令 |

建议：用命令行建立心智模型，用 GUI 辅助查看 diff 和解决冲突。

更实际的组合方式是：常规流程用命令行确认状态和执行命令，复杂差异用 GUI 看清楚。比如提交前先运行：

```bash
git status
git diff
git diff --staged
```

如果 diff 很长，再打开 VS Code Git 面板或专业 Git GUI 按文件查看。这样你既不会只靠按钮猜 Git 做了什么，也能利用图形工具降低阅读成本。

---

## 11. hooks 入门

Git hook 是在某些动作前后自动执行的脚本。

常见 hook：

| hook | 触发时机 | 用途 |
|---|---|---|
| `pre-commit` | 提交前 | 格式化、lint、禁止提交密钥 |
| `commit-msg` | 提交信息生成后 | 检查提交信息格式 |
| `pre-push` | 推送前 | 跑测试或安全检查 |

hook 可以提高质量，但不要把它当成唯一防线。CI 仍然需要在远程重新检查。

还要注意：普通 hook 文件通常放在当前仓库的 `.git/hooks/` 里，它们默认不会随着 `git commit`、`git push` 一起分享给别人。也就是说，你本地的 `pre-commit` 能拦住你自己，不一定能拦住队友。

团队里常见做法是：

| 做法 | 适合场景 |
|---|---|
| 在 README 里说明如何安装本地 hooks | 小团队或学习项目 |
| 使用工具统一安装 hooks | 前端项目常见，例如 husky |
| 在 CI 或平台保护规则里重复检查 | 必须保证团队一致执行的规则 |
| 服务端 hook 或平台规则 | 自建 Git 服务或企业平台 |

所以 hooks 的定位是：本地提前提醒，远程最终把关。不要因为本地 hook 通过了，就省掉 PR 检查或 CI。

---

## 12. 本章检查点

1. global 配置和 local 配置有什么区别？
2. Windows 上为什么要注意换行符？
3. `push.default simple` 解决了什么问题？
4. alias 什么时候有帮助，什么时候会妨碍学习？
5. GUI 能不能替代理解 Git？

---

**下一步**：[Git 内部原理与仓库维护](./Git教程系列-16-Git内部原理与仓库维护.md)

---

**返回目录**：[README](./README.md)
