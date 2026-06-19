# Git 提交历史与查询

会提交只是第一步。真正进入项目后，你还需要读懂历史：谁改了什么、为什么改、某个 bug 从哪次提交开始出现、某个文件为什么变成现在这样。

本章目标：

1. 用 `git log` 按不同方式查看历史
2. 用 `git show` 查看某次提交内容
3. 用 `git blame` 找到某一行最后是谁改的
4. 用 `git bisect` 定位哪个提交引入了问题

---

## 1. 读历史时先问什么？

不要一上来堆命令。先确定你想回答的问题：

| 问题 | 适合命令 |
|---|---|
| 最近有哪些提交？ | `git log --oneline` |
| 分支怎么分叉和合并的？ | `git log --oneline --graph --all --decorate` |
| 某次提交到底改了什么？ | `git show 提交哈希` |
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

## 3. 分支图：`--graph --all --decorate`

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

## 4. 查看某次提交：`git show`

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

## 5. 查看某个文件历史

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

## 6. 找某一行是谁改的：`git blame`

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

## 7. 用二分法找 bug：`git bisect`

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

## 8. 历史查询的安全边界

本章命令大多是只读的，但有两个例外要注意：

| 命令 | 风险 |
|---|---|
| `git bisect` | 会切换工作目录到不同提交；开始前保持工作目录干净 |
| `git show 哈希:文件` | 只读，不会改文件 |

运行 `bisect` 前先：

```bash
git status
```

最好看到工作目录干净。

---

## 9. 本章检查点

1. 想看分支合并图，用哪条命令？
2. 想看某次提交具体 diff，用哪条命令？
3. `git blame` 的正确使用目的是什么？
4. `git bisect reset` 为什么重要？

---

**下一步**：[团队工作流与分支策略](./12-团队工作流与分支策略.md)

---

**返回目录**：[README](./README.md)
