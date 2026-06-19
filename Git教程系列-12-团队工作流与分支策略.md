# Git 团队工作流与分支策略

学会命令后，还要回答团队问题：大家到底应该怎么用 Git？是直接往 `main` 提交，还是每个功能开分支？release 和 hotfix 怎么办？PR 合并应该用 merge、squash 还是 rebase？

本章目标：

1. 认识常见团队工作流
2. 理解每种工作流适合什么团队
3. 学会选择分支策略，而不是盲目套模板
4. 明确公共分支的安全规则

---

## 1. 工作流不是命令清单

Git 命令回答的是：

> 怎么提交、合并、推送？

团队工作流回答的是：

> 谁能改哪条分支？什么时候开分支？谁来审查？怎么发布？出问题怎么回滚？

一套好工作流应该满足：

| 目标 | 含义 |
|---|---|
| 主线稳定 | `main` 不应长期处于不可用状态 |
| 改动可审查 | 重要改动合入前有人看过 |
| 发布可追踪 | 知道哪个提交对应哪个版本 |
| 故障可恢复 | 出问题能 revert、hotfix 或回滚 |
| 成本不过高 | 流程不能比问题本身更复杂 |

---

## 2. 集中式工作流

特点：所有人直接在同一条主分支上工作。

```text
A --- B --- C --- D
              ↑
             main
```

适合：

- 个人项目
- 只有 1-2 人的小项目
- 练习 Git 基础

不适合：

- 多人同时开发
- 需要代码审查
- 需要保护主线稳定的项目

风险：多人直接推 `main`，容易产生推送冲突，也容易把未审查代码放进主线。

---

## 3. Feature Branch Workflow

特点：每个任务开一个功能分支，完成后通过 PR 合回主分支。

```text
main:     A --- B -------- E
               \        /
feature:        C --- D
```

常见流程：

```bash
git switch main
git pull --ff-only
git switch -c feature-login
# 开发、提交
git push -u origin feature-login
# 创建 PR，审查后合并
```

适合：

- 大多数团队
- 需要代码审查的项目
- 功能相对独立的开发

优点：清晰、通用、容易落地。缺点：如果分支开太久，容易和主线偏离，冲突变多。

---

## 4. GitHub Flow

GitHub Flow 是 Feature Branch Workflow 的轻量版本：

```text
main 永远可部署
每个改动开短生命周期分支
通过 PR 审查
合并后尽快部署
```

适合：

- Web 服务
- SaaS 产品
- 小步快跑团队
- 持续部署团队

关键要求：

- `main` 必须稳定
- PR 要小
- CI 要可靠
- 分支生命周期短

如果团队没有自动化测试和部署能力，GitHub Flow 仍然可以用，但要在合并前增加人工验证清单。

---

## 5. Git Flow

Git Flow 会使用多类长期分支：

```text
main      发布版本
 develop  日常集成
 feature  功能开发
 release  发布准备
 hotfix   紧急修复
```

适合：

- 有明确版本发布节奏的软件
- 桌面软件、移动 App、嵌入式或企业软件
- 需要维护多个发布版本的团队

缺点：

- 分支多，流程重
- 新手容易站错分支
- 对快速迭代 Web 项目可能过度复杂

不要因为它“看起来专业”就默认使用。工作流越复杂，团队执行成本越高。

---

## 6. Trunk-based Development

特点：大家围绕一条主干快速集成，功能分支很短，甚至直接在主干附近工作。

适合：

- 工程能力强的团队
- CI/CD 完善
- 自动化测试可靠
- 功能开关或灰度机制成熟

优点：

- 集成频繁，长期冲突少
- 反馈快
- 历史简单

风险：如果没有测试和发布保护，主干很容易被破坏。

---

## 7. release 与 hotfix 分支

### release 分支

当一个版本准备发布，但主线还要继续开发时，可以从主线切出 release 分支：

```bash
git switch main
git switch -c release/1.2.0
```

release 分支通常只接受：

- 发布前 bug 修复
- 版本号调整
- 文档或配置修正

### hotfix 分支

线上版本出紧急问题时，从稳定发布点或 `main` 创建 hotfix：

```bash
git switch main
git switch -c hotfix/payment-timeout
```

修复后通常需要合回：

- 当前发布分支或 `main`
- 仍在开发的主线分支

否则同一个 bug 可能在下个版本再次出现。

---

## 8. 怎么选择工作流？

| 团队/项目 | 推荐 |
|---|---|
| 个人学习项目 | 集中式或简单 feature 分支 |
| 2-5 人小团队 | Feature Branch 或 GitHub Flow |
| Web/SaaS 持续迭代 | GitHub Flow 或 Trunk-based |
| 有版本发布节奏的 App/软件 | Git Flow 的简化版 |
| 开源项目 | fork + PR + protected main |
| 大型企业团队 | 根据发布、权限、CI 能力组合设计 |

最重要的不是名字，而是团队能否稳定执行。

---

## 9. 公共分支规则

公共分支包括：

- `main`
- `master`
- `develop`
- `release/*`
- 多人共同基于其工作的任何分支

规则：

1. 不随便 `rebase` 公共分支。
2. 不随便 `push --force` 公共分支。
3. 合并前先看状态和目标分支。
4. 重要分支开启 branch protection。
5. 通过 PR/MR 合并，而不是直接推送。

如果确实需要重写公共历史，必须提前通知团队，并说明恢复方案。

---

## 10. 本章检查点

1. Feature Branch Workflow 和 GitHub Flow 的区别是什么？
2. Git Flow 为什么不适合所有团队？
3. Trunk-based Development 依赖哪些工程能力？
4. 为什么公共分支不能随便 rebase 或强推？

---

**下一步**：[代码评审与 PR 质量](./13-代码评审与PR质量.md)

---

**返回目录**：[README](./README.md)
