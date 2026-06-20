# 第一次 Git 实战项目

## 目标

在30分钟内完成一个完整的 Git 工作流，包括：
- 初始化仓库
- 多次有意义的提交
- 创建功能分支
- 解决简单冲突
- 模拟远程协作
- 查看完整历史

**适合人群**：刚读完前3章的新手，想动手验证学习效果。

**前置要求**：
- 已安装 Git
- 已配置用户名和邮箱
- 熟悉基本的文件操作

---

## 项目：个人简历网站

我们将创建一个简单的 HTML 简历网站，通过实际操作掌握 Git 基础流程。

---

## 步骤1：初始化项目（5分钟）

### 1.1 创建项目目录

`ash
# Windows
mkdir C:\git-practice\resume-site
cd C:\git-practice\resume-site

# macOS/Linux
mkdir -p ~/git-practice/resume-site
cd ~/git-practice/resume-site
`

### 1.2 初始化 Git 仓库

`ash
git init
`

你会看到：
`
Initialized empty Git repository in .../resume-site/.git/
`

### 1.3 检查状态

`ash
git status
`

输出：
`
On branch main
No commits yet
nothing to commit
`

✅ **检查点**：
- [ ] 能看到 .git 目录（可能是隐藏的）
- [ ] git status 不报错
- [ ] 提示 "No commits yet"

---

## 步骤2：首次提交（5分钟）

### 2.1 创建 README 文件

创建文件 README.md，内容：

`markdown
# 我的简历网站

这是我的第一个 Git 项目。
`

### 2.2 查看状态

`ash
git status
`

输出：
`
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md
`

### 2.3 暂存并提交

`ash
git add README.md
git commit -m "docs: 初始化项目，添加 README"
`

### 2.4 查看历史

`ash
git log --oneline
`

输出类似：
`
a1b2c3d (HEAD -> main) docs: 初始化项目，添加 README
`

✅ **检查点**：
- [ ] git status 显示 "working tree clean"
- [ ] git log 能看到第一次提交
- [ ] 理解了"暂存 → 提交"的流程

---

## 步骤3：功能分支开发（10分钟）

### 3.1 创建主页面

在 main 分支上创建 index.html：

`html
<!DOCTYPE html>
<html>
<head>
    <title>我的简历</title>
</head>
<body>
    <h1>张三</h1>
    <p>软件工程师</p>
</body>
</html>
`

提交：

`ash
git add index.html
git commit -m "feat: 添加首页基本结构"
`

### 3.2 创建功能分支添加技能部分

`ash
git switch -c feature-skills
`

编辑 index.html，在 <p>软件工程师</p> 后添加：

`html
    <h2>技能</h2>
    <ul>
        <li>Git 版本控制</li>
        <li>HTML/CSS</li>
    </ul>
`

提交：

`ash
git add index.html
git commit -m "feat: 添加技能部分"
`

### 3.3 在主分支添加联系方式（模拟并行开发）

切回 main 分支：

`ash
git switch main
`

**注意观察**：打开 index.html，技能部分不见了！这是正常的，因为那个改动在 eature-skills 分支。

在 main 分支编辑 index.html，在 <p>软件工程师</p> 后添加：

`html
    <h2>联系方式</h2>
    <p>邮箱：zhangsan@example.com</p>
`

提交：

`ash
git add index.html
git commit -m "feat: 添加联系方式"
`

### 3.4 查看分支图

`ash
git log --oneline --graph --all --decorate
`

你会看到类似：

`
* b3c4d5e (feature-skills) feat: 添加技能部分
| * c5d6e7f (HEAD -> main) feat: 添加联系方式
|/
* a2b3c4d feat: 添加首页基本结构
* a1b2c3d docs: 初始化项目，添加 README
`

✅ **检查点**：
- [ ] 理解了在 main 分支看不到 eature-skills 的改动
- [ ] 能看到分支图，两条线分叉了
- [ ] 知道当前在哪个分支（HEAD 指向）

---

## 步骤4：合并并解决冲突（5分钟）

### 4.1 合并功能分支

`ash
git merge feature-skills
`

**预期**：会出现冲突！

输出类似：
`
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Automatic merge failed; fix conflicts and then commit the result.
`

### 4.2 查看冲突

`ash
git status
`

打开 index.html，你会看到冲突标记：

`html
    <p>软件工程师</p>
<<<<<<< HEAD
    <h2>联系方式</h2>
    <p>邮箱：zhangsan@example.com</p>
=======
    <h2>技能</h2>
    <ul>
        <li>Git 版本控制</li>
        <li>HTML/CSS</li>
    </ul>
>>>>>>> feature-skills
</body>
`

### 4.3 解决冲突

手动编辑文件，改为：

`html
    <p>软件工程师</p>
    <h2>技能</h2>
    <ul>
        <li>Git 版本控制</li>
        <li>HTML/CSS</li>
    </ul>
    <h2>联系方式</h2>
    <p>邮箱：zhangsan@example.com</p>
</body>
`

删除冲突标记（<<<<<<<, =======, >>>>>>>），保留两边的内容。

### 4.4 完成合并

`ash
git add index.html
git commit -m "merge: 合并技能和联系方式部分"
`

### 4.5 查看最终历史

`ash
git log --oneline --graph --all
`

输出类似：

`
*   d7e8f9g (HEAD -> main) merge: 合并技能和联系方式部分
|\
| * b3c4d5e (feature-skills) feat: 添加技能部分
* | c5d6e7f feat: 添加联系方式
|/
* a2b3c4d feat: 添加首页基本结构
* a1b2c3d docs: 初始化项目，添加 README
`

✅ **检查点**：
- [ ] 成功解决了第一次冲突
- [ ] 理解了冲突标记的含义
- [ ] 知道解决冲突后要 git add + git commit
- [ ] 能看到合并后的历史图

---

## 步骤5：添加样式和完善（5分钟）

### 5.1 创建样式文件

创建 style.css：

`css
body {
    font-family: Arial, sans-serif;
    max-width: 800px;
    margin: 50px auto;
    padding: 20px;
}

h1 {
    color: #2c3e50;
}

h2 {
    color: #34495e;
    border-bottom: 2px solid #3498db;
    padding-bottom: 5px;
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    padding: 5px 0;
}
`

### 5.2 修改 HTML 引入样式

编辑 index.html，在 <head> 中添加：

`html
    <link rel="stylesheet" href="style.css">
`

### 5.3 提交

`ash
git add style.css index.html
git commit -m "style: 添加 CSS 样式"
`

### 5.4 创建 .gitignore

创建 .gitignore 文件：

`
# 操作系统文件
.DS_Store
Thumbs.db

# 编辑器文件
.vscode/
.idea/

# 临时文件
*.tmp
*.log
`

提交：

`ash
git add .gitignore
git commit -m "chore: 添加 gitignore"
`

---

## 最终检查

### 查看完整历史

`ash
git log --oneline --graph --all
`

### 查看所有文件

`ash
ls
# 或 Windows: dir
`

应该看到：
- README.md
- index.html
- style.css
- .gitignore
- .git/ 目录

### 在浏览器打开

双击 index.html，在浏览器中查看你的简历网站。

---

## 🎉 完成检查清单

恭喜！如果你完成了以下所有检查点，说明你已经掌握了 Git 基础工作流：

- [ ] 成功初始化了一个 Git 仓库
- [ ] 完成了至少 5 次有意义的提交
- [ ] 创建并切换了分支
- [ ] 解决了一次合并冲突
- [ ] 理解了"工作目录 → 暂存区 → 本地仓库"的流程
- [ ] 能看懂 git log --graph 的分支图
- [ ] 知道 git status 会告诉你下一步该做什么

---

## 下一步

### 如果想继续实践

1. **添加更多功能**：
   - 教育经历部分
   - 项目经历部分
   - 为每个功能创建独立分支

2. **练习更多命令**：
   `ash
   git diff HEAD~2 HEAD        # 比较两个版本
   git show 提交哈希            # 查看某次提交详情
   git blame index.html        # 看每行是谁改的
   `

3. **模拟撤销场景**：
   - 改坏一个文件，用 git restore 恢复
   - 提交错了，用 git reset 撤销
   - 查看 git reflog 的历史记录

### 学习远程协作

完成本项目后，可以继续学习：
- 第6章：远程协作 - 学习如何推送到 GitHub
- 第8章：Pull Request - 学习如何参与团队项目

---

## 常见问题

### Q: 为什么切换分支时文件会变？

A: 因为 Git 会把工作目录的内容替换成目标分支的最新提交。这是正常的，不用担心。

### Q: 冲突能避免吗？

A: 不能完全避免，但可以减少：
- 经常拉取最新代码
- 功能分支尽量短命
- 团队约定好负责的模块

### Q: 我可以删除分支吗？

A: 可以，但要先确认合并完成：

`ash
git branch -d feature-skills    # 安全删除（必须已合并）
git branch -D feature-skills    # 强制删除（危险）
`

### Q: 这个项目可以上传到 GitHub 吗？

A: 可以！学完第6章后，你可以：

`ash
# 在 GitHub 创建仓库后
git remote add origin https://github.com/你的用户名/resume-site.git
git push -u origin main
`

---

## 时间回顾

如果你完成了整个实战项目，应该用了：

| 步骤 | 预计时间 | 你的实际时间 |
|-----|---------|------------|
| 步骤1：初始化 | 5分钟 | ___ 分钟 |
| 步骤2：首次提交 | 5分钟 | ___ 分钟 |
| 步骤3：分支开发 | 10分钟 | ___ 分钟 |
| 步骤4：解决冲突 | 5分钟 | ___ 分钟 |
| 步骤5：完善项目 | 5分钟 | ___ 分钟 |
| **总计** | **30分钟** | **___ 分钟** |

**不要紧张**：如果你用了更多时间，这完全正常！第一次操作总是需要更多时间理解和适应。

---

## 反馈

完成这个实战项目后，建议：

1. 把这个项目保留，以后可以回来复习
2. 尝试自己再创建一个不同的项目（比如个人博客、笔记本）
3. 继续学习教程的后续章节
4. 在真实项目中应用学到的技能

**记住**：Git 是用出来的，不是背出来的。多练习，遇到问题查文档，慢慢就熟练了。

---

**返回目录**：[README](./README.md)  
**继续学习**：[第4章：分支管理](./Git教程系列-04-分支管理.md)
