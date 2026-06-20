# 02. 安装与配置

> 10 分钟完成 Git 的安装和基本配置

## 安装 Git

### Windows

**方法1: 官方安装包** (推荐)

1. 访问 [git-scm.com](https://git-scm.com/download/win)
2. 下载安装包
3. 双击安装,全部选默认选项即可

安装完成后,右键菜单会出现 "Git Bash"。

**方法2: 通过包管理器**

```powershell
# 使用 winget
winget install Git.Git

# 使用 Chocolatey
choco install git
```

### macOS

**方法1: Homebrew** (推荐)

```bash
brew install git
```

**方法2: Xcode 自带**

```bash
xcode-select --install
```

### Linux

**Debian/Ubuntu:**
```bash
sudo apt install git
```

**Fedora/RHEL:**
```bash
sudo dnf install git
```

**Arch:**
```bash
sudo pacman -S git
```

### 验证安装

```bash
git --version
```

输出类似:
```
git version 2.40.0
```

看到版本号就说明安装成功了。

## 必要配置

安装后必须配置两件事:用户名和邮箱。

### 配置用户信息

```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱@example.com"
```

**为什么需要这个?**
- 每次提交都会记录作者信息
- 用于识别谁做了什么改动

**示例**:
```bash
git config --global user.name "Alice"
git config --global user.email "alice@example.com"
```

### 查看配置

```bash
git config --list
```

输出:
```
user.name=Alice
user.email=alice@example.com
...
```

### 配置编辑器 (可选)

Git 有时需要打开编辑器(比如写提交信息)。

**使用 VS Code:**
```bash
git config --global core.editor "code --wait"
```

**使用 Vim:**
```bash
git config --global core.editor vim
```

**使用 Nano:**
```bash
git config --global core.editor nano
```

如果不配置,Git 会使用系统默认编辑器。

## 创建第一个仓库

学会了配置,来创建第一个 Git 仓库试试!

### 步骤 1: 创建项目目录

```bash
# 创建目录
mkdir my-first-repo
cd my-first-repo
```

### 步骤 2: 初始化 Git 仓库

```bash
git init
```

输出:
```
Initialized empty Git repository in /path/to/my-first-repo/.git/
```

**发生了什么?**
- Git 创建了一个隐藏的 `.git` 目录
- 这个目录存储所有版本历史
- 当前目录现在是一个 Git 仓库了

### 步骤 3: 查看状态

```bash
git status
```

输出:
```
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

这是一个空仓库,还没有任何提交。

### 步骤 4: 创建第一个文件

```bash
echo "# My First Repo" > README.md
```

再次查看状态:
```bash
git status
```

输出:
```
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md

nothing added to commit but untracked files present (use "git add" to track)
```

Git 发现了新文件 `README.md`,但还没有跟踪它。

### 步骤 5: 第一次提交

```bash
# 添加文件到暂存区
git add README.md

# 提交
git commit -m "Initial commit"
```

输出:
```
[main (root-commit) a1b2c3d] Initial commit
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
```

🎉 恭喜!你完成了第一次 Git 提交!

## 常用配置 (可选)

这些配置不是必须的,但能让 Git 更好用。

### 彩色输出

```bash
git config --global color.ui auto
```

Git 输出会有颜色,更容易识别。

### 默认分支名

```bash
git config --global init.defaultBranch main
```

新仓库默认分支名为 `main` (而不是老式的 `master`)。

### 别名 (快捷命令)

```bash
# st = status
git config --global alias.st status

# co = checkout
git config --global alias.co checkout

# br = branch
git config --global alias.br branch

# ci = commit
git config --global alias.ci commit
```

以后就可以用:
```bash
git st      # 代替 git status
git co main # 代替 git checkout main
```

### 忽略文件权限变化 (Linux/Mac)

```bash
git config --global core.fileMode false
```

避免因为文件权限变化导致 Git 认为文件被修改。

## 配置文件位置

Git 配置保存在:
```
~/.gitconfig          # 全局配置 (--global)
.git/config           # 仓库配置 (--local)
/etc/gitconfig        # 系统配置 (--system)
```

用文本编辑器也能直接编辑 `~/.gitconfig`。

## 你只需要记住这 3 点

1. **安装后必须配置**: `user.name` 和 `user.email`
2. **初始化仓库**: `git init`
3. **查看配置**: `git config --list`

## 练习

1. 配置你的用户名和邮箱
2. 创建一个新目录,初始化为 Git 仓库
3. 创建一个文件,完成第一次提交

## 下一步

Git 已经配置好了,接下来学习日常工作流:

→ [日常工作流](03-daily-workflow.md) ⭐ 核心章节,15分钟掌握 Git 精髓

---

**故障排查**:
- 如果 `git` 命令不存在,检查是否重启了终端
- Windows 用户可以用 "Git Bash" 而不是 CMD
- 如果配置保存不了,检查是否有写权限
