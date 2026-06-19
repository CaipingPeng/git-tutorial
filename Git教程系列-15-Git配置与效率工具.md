# Git 配置与效率工具

Git 不只是命令本身。合适的配置、别名、编辑器、凭据管理和工具，可以减少很多低级错误。本章讲常用配置和效率工具。

本章目标：

1. 理解 Git 配置的层级
2. 配好用户名、邮箱、默认分支、换行符和编辑器
3. 使用 alias 简化高频命令
4. 理解 CLI、GUI、VS Code 和 hooks 的定位

---

## 1. Git 配置有层级

常见层级：

| 层级 | 命令参数 | 影响范围 |
|---|---|---|
| system | `--system` | 整台机器所有用户 |
| global | `--global` | 当前用户所有仓库 |
| local | 不加参数或 `--local` | 当前仓库 |

新手最常用的是 global：

```bash
git config --global user.name "你的名字"
git config --global user.email "you@example.com"
```

在公司项目需要使用公司邮箱时，可以进入那个仓库单独配置：

```bash
git config user.email "you@company.com"
```

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

## 5. 默认编辑器

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

## 6. 常用 alias

alias 可以把长命令变短。

```bash
git config --global alias.st status
git config --global alias.co switch
git config --global alias.br branch
git config --global alias.lg "log --oneline --graph --all --decorate"
```

之后可以用：

```bash
git st
git lg
```

不要一开始配太多 alias。先把原命令学明白，再给高频命令配别名。

---

## 7. 凭据管理

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

## 8. CLI、GUI 和编辑器 Git 面板

| 工具 | 优点 | 注意 |
|---|---|---|
| 命令行 CLI | 精确、可复制、适合学习底层逻辑 | 新手容易输错参数 |
| VS Code Git 面板 | 看 diff、解决冲突方便 | 不要只点按钮而不知道发生了什么 |
| GitHub Desktop | 适合轻量 GitHub 工作流 | 高级操作能力有限 |
| SourceTree / Fork 等 GUI | 分支图直观 | 团队排障时仍要懂命令 |

建议：用命令行建立心智模型，用 GUI 辅助查看 diff 和解决冲突。

---

## 9. hooks 入门

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

## 10. 本章检查点

1. global 配置和 local 配置有什么区别？
2. Windows 上为什么要注意换行符？
3. alias 什么时候有帮助，什么时候会妨碍学习？
4. GUI 能不能替代理解 Git？

---

**下一步**：[Git 内部原理与仓库维护](./Git教程系列-16-Git内部原理与仓库维护.md)

---

**返回目录**：[README](./README.md)
