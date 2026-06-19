# Git 提交历史与查询

会提交只是第一步。真正进入项目后，你还需要读懂历史：谁改了什么、为什么改、某个 bug 从哪次提交开始出现、某个文件为什么变成现在这样。

本章目标：

1. 用 `git log` 按不同方式查看历史
2. 用 `git show` 查看某次提交内容
3. 知道 `git cherry-pick` 适合什么场景
4. 用 `git blame` 找到某一行最后是谁改的
5. 用 `git bisect` 定位哪个提交引入了问题

---

## 1. 读历史时先问什么？

不要一上来堆命令。先确定你想回答的问题：

| 问题 | 适合命令 |
|---|---|
| 最近有哪些提交？ | `git log --oneline` |
| 分支怎么分叉和合并的？ | `git log --oneline --graph --all --decorate` |
| 某次提交到底改了什么？ | `git show 提交哈希` |
| 想把某个提交搬到当前分支 | `git cherry-pick 提交哈希` |
| 某个文件经历了哪些提交？ | `git log -- 文件名` |
| 某一行是谁改的？ | `git blame 文件名` |
| bug 从哪次提交开始出现？ | `git bisect` |

---

## 2. 简洁历史：`git log --oneline`

```bash
git log --oneline
```

示例：

```text
c3d4e5f 修复登录按钮样式
a1b2c3d 添加登录页面
9f8e7d6 初始化项目
```

每行包括：

| 内容 | 含义 |
|---|---|
| `c3d4e5f` | 提交短哈希 |
| `修复登录按钮样式` | 提交说明 |

如果历史很多，可以限制数量：

```bash
git log --oneline -5
```

---

## 3. 给 log 加筛选条件

真实项目里的提交会很多，`git log --oneline` 只能解决“最近发生了什么”。如果你要回答更具体的问题，就需要给 `log` 加筛选条件。

常用筛选方式：

| 你想找什么 | 命令示例 | 说明 |
|---|---|---|
| 最近 5 次提交 | `git log --oneline -5` | 控制输出数量 |
| 某个作者的提交 | `git log --author="Alice"` | 作者名可以写部分匹配 |
| 某段时间后的提交 | `git log --since="2026-06-01"` | 适合查近期改动 |
| 某段时间前的提交 | `git log --until="2026-06-10"` | 可和 `--since` 搭配 |
| 提交说明里包含关键词 | `git log --grep="login"` | 查提交信息，不查文件内容 |
| 改过某个文件的提交 | `git log -- README.md` | `--` 后面是路径 |
| 每次提交的文件统计 | `git log --stat` | 想先看影响范围时 |

这些条件可以组合。例如：

```bash
git log --oneline --author="Alice" --since="2026-06-01" -- README.md
```

这条命令可以读成：

> 查 Alice 从 2026-06-01 以来，影响过 README.md 的提交，并用一行显示。

如果命令结果为空，不一定是 Git 出错。更常见的原因是：作者名、时间范围、文件路径或关键词限制得太窄。

---

## 4. 分支图：`--graph --all --decorate`

```bash
git log --oneline --graph --all --decorate
```

示例：

```text
*   e5f6a7b (HEAD -> main) Merge branch 'feature-login'
|\
| * c3d4e5f (feature-login) 添加登录按钮
| * b2c3d4e 添加登录页面
* | a1b2c3d 更新首页文案
|/
* 9f8e7d6 初始化项目
```

重点看：

- `HEAD -> main`：你现在在哪个分支
- `feature-login`：功能分支指向哪里
- `|\`、`|/`：哪里分叉、哪里合并

不要试图背图形符号。先看分支名和提交顺序。

---

## 5. 查看某次提交：`git show`

如果你想知道某次提交具体改了什么：

```bash
git show c3d4e5f
```

它通常会显示：

- 提交哈希
- 作者
- 时间
- 提交说明
- diff 内容

如果只想看提交说明和统计：

```bash
git show --stat c3d4e5f
```

如果只想看某个文件在某次提交中的版本：

```bash
git show c3d4e5f:路径/文件名
```

---

## 6. 搬运单个提交：`git cherry-pick`

有时你不想合并整个分支，只想把某一个提交带到当前分支。例如：

- bug 修复提交在 `feature-login` 上，但 `main` 也急需这个修复
- 某个文档修正提交应该先进入发布分支
- 你误把一个独立改动提交到了别的分支

这时可以先看清历史：

```bash
git log --oneline --graph --decorate --all -12
```

确认要搬运的提交哈希后，切到目标分支：

```bash
git switch main
git cherry-pick c3d4e5f
```

这条命令的意思是：

> 把 `c3d4e5f` 这个提交所代表的改动，重新应用到当前分支上，并生成一个新提交。

注意，它不是“移动原提交”。cherry-pick 后当前分支上会出现一个新提交，内容来自原提交，但提交哈希通常不同。

如果发生冲突，处理方式和 rebase 更像：

```bash
git status
# 编辑冲突文件
git add 冲突文件
git cherry-pick --continue
```

如果发现选错提交，可以取消：

```bash
git cherry-pick --abort
```

新手阶段要记住边界：cherry-pick 适合少量独立提交；如果你想整合一整条功能分支，通常应该用 merge、rebase 或 PR。

---

## 7. 查看某个文件历史

```bash
git log -- README.md
```

简洁形式：

```bash
git log --oneline -- README.md
```

这会只显示影响过 `README.md` 的提交。

如果文件被重命名过，可以加：

```bash
git log --follow --oneline -- README.md
```

`--follow` 会尝试跨重命名追踪文件历史。

---

## 8. 找某一行是谁改的：`git blame`

```bash
git blame README.md
```

示例：

```text
a1b2c3d4 (Alice 2026-06-01 10:00:00 +0800  12) 本项目使用 Git 管理版本
```

它告诉你：

- 这一行最后一次由哪个提交改动
- 作者是谁
- 时间是什么
- 行内容是什么

注意：`blame` 不是为了“甩锅”。正确用法是找到上下文，再用 `git show` 看那次提交为什么这么改。

---

## 9. 用二分法找 bug：`git bisect`

场景：你知道现在有 bug，也知道以前某个版本没 bug，但不知道中间哪次提交引入了它。

开始：

```bash
git bisect start
```

标记当前版本是坏的：

```bash
git bisect bad
```

标记某个旧提交是好的：

```bash
git bisect good 旧提交哈希
```

Git 会自动切到中间某个提交。你运行测试或手动验证，然后告诉 Git：

```bash
git bisect good
```

或：

```bash
git bisect bad
```

重复几次后，Git 会定位第一个坏提交。

结束二分，回到原状态：

```bash
git bisect reset
```

---

## 10. 历史查询的安全边界

本章命令大多是只读的，但有两个例外要注意：

| 命令 | 风险 |
|---|---|
| `git bisect` | 会切换工作目录到不同提交；开始前保持工作目录干净 |
| `git cherry-pick` | 会在当前分支创建新提交；开始前确认目标分支正确 |
| `git show 哈希:文件` | 只读，不会改文件 |

运行 `bisect` 前先：

```bash
git status
```

最好看到工作目录干净。

---

## 11. 本章检查点

1. 想看分支合并图，用哪条命令？
2. 想看某次提交具体 diff，用哪条命令？
3. `cherry-pick` 适合搬运整个分支还是单个独立提交？
4. `git blame` 的正确使用目的是什么？
5. `git bisect reset` 为什么重要？

---

**下一步**：[团队工作流与分支策略](./Git教程系列-12-团队工作流与分支策略.md)

---

**返回目录**：[README](./README.md)
