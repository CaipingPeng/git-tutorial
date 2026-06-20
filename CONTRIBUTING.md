# 贡献指南

感谢你考虑为这个 Git 教程做贡献！本指南将帮助你快速了解如何参与项目。

## 🎯 我们需要什么帮助

### 高优先级
- 🐛 **修正错误**: 命令错误、概念解释不当、链接失效
- 📝 **改进措辞**: 让表达更清晰、更易懂
- 🖼️ **补充图片**: 为缺少配图的章节添加示意图
- 💡 **实际案例**: 分享真实工作中的 Git 使用场景

### 中优先级
- 🌐 **翻译**: 将教程翻译成其他语言（保持中文为主版本）
- 🔧 **工具脚本**: 改进验证脚本、图片提取脚本
- 📚 **进阶内容**: 帮助编写进阶教程章节

### 低优先级
- 🎨 **样式优化**: Markdown 排版、代码高亮
- 📖 **扩展阅读**: 补充参考资料链接

## 📋 贡献流程

### 1. 提交 Issue（建议）

在开始工作前，先提交 Issue 说明你的想法：

`markdown
标题: [修正] 03-daily-workflow.md 中 git add 命令有误

描述:
- 位置: docs/basics/03-daily-workflow.md 第 42 行
- 问题: 命令应该是 git add . 而不是 git add *
- 影响: 可能导致新手混淆
`

### 2. Fork 并克隆

`ash
# Fork 这个仓库到你的账号下
# 然后克隆你的 Fork
git clone https://github.com/你的用户名/git-tutorial.git
cd git-tutorial
`

### 3. 创建分支

`ash
# 从 main 创建分支，用描述性名称
git switch -c fix/daily-workflow-typo
`

分支命名规范:
- ix/描述 - 修正错误
- docs/描述 - 文档改进
- eat/描述 - 新增内容
- efactor/描述 - 重构现有内容

### 4. 进行修改

#### 编辑 Markdown 文档

- 使用 UTF-8 编码
- 行尾使用 LF（Unix 风格）
- 中英文之间加空格（遵循 [中文文案排版指北](https://github.com/sparanoid/chinese-copywriting-guidelines)）
- 代码块指定语言：\\\ash 而不是 \\\

#### 添加图片

`ash
# 图片放在 assets/images/ 下，按类别分组
assets/images/
├── progit/          # Pro Git 官方图片
├── basics/          # 基础教程自绘图
├── advanced/        # 进阶教程图
└── diagrams/        # 流程图、示意图
`

在 Markdown 中引用:
`markdown
![分支示意图](../../assets/images/basics/branch-demo.png)
`

### 5. 本地验证

运行验证脚本确保没有坏链接:

`ash
python scripts/validators/check_links.py
`

### 6. 提交改动

`ash
# 暂存改动
git add docs/basics/03-daily-workflow.md

# 提交，写清晰的提交说明
git commit -m "fix: 修正 daily-workflow 中 git add 命令示例"
`

提交信息规范:
- ix: - 修正错误
- docs: - 文档改进
- eat: - 新增内容
- efactor: - 重构
- style: - 格式调整
- 	est: - 测试相关

### 7. 推送并创建 PR

`ash
# 推送到你的 Fork
git push -u origin fix/daily-workflow-typo
`

然后在 GitHub 上创建 Pull Request:

**PR 标题**: [修正] daily-workflow: 修正 git add 命令示例

**PR 描述模板**:
`markdown
## 改动类型
- [ ] 修正错误
- [ ] 文档改进
- [ ] 新增内容
- [ ] 重构

## 改动说明
修正了 03-daily-workflow.md 中 git add 命令的错误示例。

## 相关 Issue
Fixes #42

## 改动清单
- [x] 修改了 docs/basics/03-daily-workflow.md
- [x] 运行了 check_links.py 验证
- [x] 确认中英文间有空格

## 截图（如适用）
（如果改动涉及图片或格式，贴个截图）
`

## 📝 写作规范

### 语言风格

- **简洁**: 能用一句话说清楚的不用两句
- **口语化**: 像给朋友讲解一样，不要太学术
- **准确**: 命令、参数必须准确无误
- **场景化**: 从实际问题出发，而非单纯罗列功能

### 示例

❌ **不好的写法**:
`markdown
git add 命令用于将工作区的改动添加到暂存区。
它有很多参数，如 -A、-u、-p 等。
`

✅ **好的写法**:
`markdown
当你改完代码，想提交时，先用 git add 选择要提交的文件：

\\\ash
git add 文件名        # 暂存单个文件
git add .           # 暂存当前目录所有改动
\\\

这一步叫"暂存"，相当于告诉 Git："这些改动我要提交"。
`

### 章节结构

每个章节建议包含:
1. **引言** - 为什么需要学这个
2. **核心概念** - 用简单语言解释
3. **常用命令** - 带场景的命令示例
4. **实践练习** - 让读者动手
5. **常见问题** - 新手容易遇到的坑

### 代码示例

`ash
# ✅ 好的示例: 有注释，输出清晰
git status
# 输出:
# On branch main
# Changes not staged for commit:
#   modified:   README.md

git add README.md
git commit -m "更新 README"
`

`ash
# ❌ 不好的示例: 没有上下文
git add .
git commit -m "update"
`

## 🔍 审查标准

PR 会根据以下标准审查:

### 必须通过
- [ ] Markdown 语法正确
- [ ] 链接和图片路径有效
- [ ] 命令示例可运行且正确
- [ ] 中英文排版规范

### 建议满足
- [ ] 表达清晰易懂
- [ ] 有实际使用场景
- [ ] 代码示例带注释
- [ ] 图文并茂

## 🤔 常见问题

### Q: 我不确定我的想法是否合适，怎么办？

A: 先提交 Issue 讨论！描述你的想法，维护者会给反馈。

### Q: 我发现一个小错误，需要提 Issue 吗？

A: 很小的改动（如错别字）可以直接提 PR。复杂的改动建议先提 Issue。

### Q: 我想贡献进阶教程，该写什么？

A: 查看 [docs/advanced/README.md](docs/advanced/README.md) 的规划，选择一个章节，提 Issue 认领。

### Q: 我不会画图，怎么补充图片？

A: 可以提 Issue 说明需要配图的位置和内容，让社区帮忙绘制。

### Q: 可以抄其他教程的内容吗？

A: 不可以直接抄袭。可以参考别人的讲解思路，但必须用自己的话重新表达，并注明灵感来源。

## 🎯 特殊贡献类型

### 报告问题

不需要写代码也可以贡献！报告问题时请提供:
- 问题位置（文件名 + 行号）
- 问题描述
- 你的建议

### 改进图片

如果你擅长画图:
1. 使用 draw.io、Figma 或其他工具绘制
2. 导出为 PNG（透明背景，宽度 800-1200px）
3. 保存到 ssets/images/ 相应目录
4. 在对应文档中引用

### 分享实战案例

如果你在实际工作中遇到过有趣的 Git 问题和解决方案:
1. 整理成完整的案例
2. 脱敏处理（去掉公司/项目敏感信息）
3. 提交到 docs/appendix/troubleshooting.md 或相关章节

## 📜 许可协议

贡献的内容将采用与项目相同的 MIT License。提交 PR 即表示你同意:
- 你拥有所提交内容的版权
- 同意将内容以 MIT License 共享

## 🙏 致谢

感谢所有贡献者！你的每一个改进都让这个教程更好。

---

**开始贡献**: 查看 [Open Issues](https://github.com/CaipingPeng/git-tutorial/issues) | 提交 [新 Issue](https://github.com/CaipingPeng/git-tutorial/issues/new)
