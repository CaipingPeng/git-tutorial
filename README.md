# Git 教程 - 从入门到进阶

一套清晰、实用的 Git 中文教程,适合新手入门和进阶学习。

## 📚 教程特色

- ✅ **分层清晰**: 基础版(日常够用) + 进阶版(深入原理)
- ✅ **场景驱动**: 从实际问题出发,而非命令堆砌
- ✅ **简洁实用**: 只讲最常用的 20%,覆盖 80% 场景
- ✅ **图文并茂**: 31 张 Pro Git 官方图片 + 自绘图表
- ✅ **持续更新**: 基于官方文档,保持最新

## 🎯 快速开始

### 零基础入门

如果你完全不懂 Git,从这里开始:

→ **[基础教程](docs/basics/README.md)** (8 章,约 2 小时)

**核心章节** (必读):
1. [Git 是什么](docs/basics/01-introduction.md) - 5 分钟了解 Git
2. [安装与配置](docs/basics/02-installation.md) - 10 分钟完成设置
3. [日常工作流](docs/basics/03-daily-workflow.md) ⭐ - 15 分钟掌握核心操作

### 已有基础,想深入学习

→ **[进阶教程](docs/advanced/README.md)** (开发中)

深入讲解 Git 内部原理、高级技巧和最佳实践。

### 快速查询

→ **[命令速查表](docs/appendix/cheatsheet.md)** - 一页纸快速参考
→ **[故障排查](docs/appendix/troubleshooting.md)** - 解决常见问题

## 📖 目录

### 基础教程 (覆盖 95% 日常场景)

| 章节 | 内容 | 时间 |
|---|---|---|
| [01. Git 是什么](docs/basics/01-introduction.md) | 为什么用 Git,核心概念 | 5 分钟 |
| [02. 安装与配置](docs/basics/02-installation.md) | 安装和基本配置 | 10 分钟 |
| [03. 日常工作流](docs/basics/03-daily-workflow.md) ⭐ | status/add/commit/push | 15 分钟 |
| [04. 分支基础](docs/basics/04-branching.md) | 创建、切换、合并分支 | 15 分钟 |
| [05. 远程协作](docs/basics/05-remote-collaboration.md) | clone/pull/push | 15 分钟 |
| [06. 冲突解决](docs/basics/06-conflict-resolution.md) | 理解和解决冲突 | 10 分钟 |
| [07. 撤销错误](docs/basics/07-undo-mistakes.md) | restore/reset/revert | 15 分钟 |
| [08. GitHub 工作流](docs/basics/08-github-workflow.md) | Fork/PR/开源贡献 | 15 分钟 |

**总计**: 约 100 分钟

### 进阶教程 (深入原理和技巧)

开发中...

### 附录

- [命令速查表](docs/appendix/cheatsheet.md) - 一页纸参考
- [故障排查](docs/appendix/troubleshooting.md) - 常见问题解决
- [术语表](docs/appendix/glossary.md) - Git 术语解释
- [学习资源](docs/appendix/resources.md) - 推荐资源

## 🎓 学习路径

### 路径 1: 快速上手 (30 分钟)

适合急着用 Git 的新手:
1. [安装与配置](docs/basics/02-installation.md)
2. [日常工作流](docs/basics/03-daily-workflow.md) ⭐
3. [分支基础](docs/basics/04-branching.md)

### 路径 2: 完整学习 (2 小时)

适合想系统学习的初学者:
- 按顺序学完全部 8 章基础教程
- 完成每章的练习
- 实践一个真实项目

### 路径 3: 查漏补缺 (按需)

适合有基础但有疑问的开发者:
- 跳到你需要的章节
- 查阅命令速查表
- 遇到问题看故障排查

## 💡 教程设计理念

### 简洁 > 全面

- 不追求覆盖所有命令
- 只讲最常用的 20%
- 每章控制在 10-15 分钟阅读

### 场景 > 功能

- 从实际问题出发
- "怎么撤销改动" 而非 "git reset 的所有参数"
- 每个命令都有明确的使用场景

### 体验 > 指标

- 让用户感觉"Git 原来不难"
- 30 个讲透的命令 > 100 个蜻蜓点水
- 学会并能用 > 背诵命令

## 🛠️ 项目结构

```
git-tutorial/
├── docs/                    # 📚 教程文档
│   ├── basics/              # 基础教程 (8章)
│   ├── advanced/            # 进阶教程 (开发中)
│   └── appendix/            # 附录 (速查表/FAQ)
├── assets/                  # 📷 静态资源
│   └── images/              # 图片资源
├── references/              # 📖 参考资料
│   ├── books/               # 参考书籍
│   ├── official-docs/       # 官方文档 (272个)
│   ├── analysis/            # 优化分析报告
│   └── archive/             # 归档的旧教程
└── scripts/                 # 🔧 工具脚本
```

## 📚 参考资料

本教程融合了以下权威资源:

- **[Pro Git](https://git-scm.com/book/zh)** - 官方教程,深入全面
- **[gittutorial](https://git-scm.com/docs/gittutorial)** - 官方入门教程
- **Git 官方文档** - 272 个命令文档
- **社区最佳实践** - 开源项目经验总结

完整引用记录见 [references.md](docs/appendix/resources.md)

## 🤝 贡献

欢迎贡献!

- 🐛 **发现错误**: 提交 [Issue](https://github.com/CaipingPeng/git-tutorial/issues)
- 💡 **改进建议**: 提交 [Pull Request](https://github.com/CaipingPeng/git-tutorial/pulls)
- ⭐ **觉得有用**: Star 这个项目

查看 [贡献指南](CONTRIBUTING.md) 了解详情。

## 📜 版权信息

- 教程内容: MIT License
- Pro Git 图片: CC BY-NC-SA 3.0 (来源已标注)

详见 [LICENSE](LICENSE)

## 🎯 学习建议

1. **边学边练**: 不要只看,一定要动手实践
2. **由浅入深**: 先完成基础教程,再看进阶内容
3. **遇到问题**: 先查速查表和 FAQ,再搜索或提问
4. **实战项目**: 学完基础后,找个真实项目练手
5. **帮助他人**: 教是最好的学,尝试帮助队友解决 Git 问题

## 📧 联系方式

- GitHub: [@CaipingPeng](https://github.com/CaipingPeng)
- 项目地址: [git-tutorial](https://github.com/CaipingPeng/git-tutorial)

---

**开始学习**: [基础教程 →](docs/basics/README.md)

**快速上手**: [日常工作流 →](docs/basics/03-daily-workflow.md)
