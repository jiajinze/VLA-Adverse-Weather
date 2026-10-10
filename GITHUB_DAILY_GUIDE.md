# GitHub 每日更新指南

> 这是一份"傻瓜式"操作手册，让你知道每天该 commit 什么、怎么 commit。

## 🎯 核心理念

- **GitHub = 你的编程简历**（不是网盘，不是博客）
- **每天 1 个 commit，每次 1 个"小内容"**
- **半年后 100+ commit = 校招杀手锏**

## 📅 每天 commit 什么？（5类日更动作）

### 类型 1：写代码（最常见）
- 今天刷的 LeetCode 题
- 跑通的 YOLOv8 demo
- 复现的论文代码

### 类型 2：写笔记（最简单）
- 论文读后感（100字就够）
- 概念学习笔记
- 错题反思

### 类型 3：更新 README（最偷懒）
- 改一行字
- 加一个项目说明

### 类型 4：添加资源链接（30秒）
- 数据集链接
- 论文链接
- 工具脚本

### 类型 5：写日记（最个性化）
- 每周复盘
- 学习心得

## 🛠️ VSCode + Git 操作流程（每天 1-3 分钟）

### Step 1：打开 VSCode → 打开项目文件夹
- 顶部菜单：`文件` → `打开文件夹` → `F:\Cursor_vla\VLA-Adverse-Weather`

### Step 2：改文件 / 新建文件
- 在 VSCode 里写代码 / 写笔记

### Step 3：打开"源代码管理"
- 左侧边栏，第 3 个图标（分支形状）
- 会看到所有"未提交"的更改

### Step 4：填写 commit 消息 + 提交
- 在消息框输入：`feat(leetcode): day 1 - two sum`
- 点击 `✓ 提交`（或按 Ctrl+Enter）

### Step 5：推送到 GitHub
- 点击 `↓` 同步按钮
- 或菜单：`终端` → `Git: Push`

### Step 6：验证
- 打开 GitHub 仓库网页
- 刷新看新内容是否出现

## 🆕 完全新手？用 GitHub Desktop（最傻瓜）

下载：https://desktop.github.com

操作流程：
1. Clone 你的仓库
2. 在 VSCode 里改文件
3. 打开 GitHub Desktop
4. 左下角写 commit message
5. 点 `Commit to main`
6. 点 `Push origin`

**比命令行简单 10 倍，像发朋友圈**。

## 💬 commit 消息规范

| 场景 | 英文（推荐）| 中文 |
|------|------------|------|
| 新功能 | `feat: add XXX` | 新增：XXX |
| 修bug | `fix: XXX` | 修复：XXX |
| 文档 | `docs: update XXX` | 文档：XXX |
| 格式 | `style: format XXX` | 格式：XXX |
| 重构 | `refactor: XXX` | 重构：XXX |
| LeetCode | `feat(leetcode): day X - XXX` | 刷题：第X题 |
| 笔记 | `docs(notes): XXX` | 笔记：XXX |

**好的例子**：
- `feat(leetcode): day 1 - two sum`
- `docs(notes): read vla survey 2024`
- `feat(datasets): add adverse weather datasets list`

**不好的例子**：
- `update`
- `修改`
- `第一次提交`

## 📅 30天日更挑战（照着做就行）

### Week 1（10/10-10/16）：LeetCode + 初始化
- Day 1: 仓库初始化
- Day 2-6: LeetCode 1-5题
- Day 7: 周复盘笔记

### Week 2（10/17-10/23）：LeetCode + 工程
- Day 8-10: LeetCode 6-10题
- Day 11: 综述笔记1
- Day 12: YOLOv8 demo 代码
- Day 13-14: LeetCode + 周复盘

### Week 3（10/24-10/30）：LeetCode + 论文
- Day 15: 综述笔记2
- Day 16-20: LeetCode 11-30题
- Day 17: 数据集链接
- Day 18: JarvisIR 笔记更新
- Day 21: 周复盘

### Week 4（10/31-11/08）：综合
- Day 22-25: LeetCode 31-45题
- Day 23: DETR demo 代码
- Day 27-30: 笔记 + LeetCode

**30天目标**：
- 20+ LeetCode 答案
- 2+ 论文笔记
- 4+ 周复盘
- 1+ YOLOv8 代码
- 30+ commit

## ⚠️ 3个常见坑

### 坑1：周末一次性补 7 次 commit
**错！** 老师/面试官能看出是突击补的
**对**：每天 1-2 次，间隔均匀

### 坑2：commit 太多小修改
**错！** 改 1 个空格就 commit 一次
**对**：把今天的所有改动打包成 1-2 次 commit

### 坑3：commit 太少大杂烩
**错！** 1个月才 commit 1次，改了 100 个文件
**对**：每天 1-3 次，每次 1-3 个文件

## 📌 你的第一次 commit 演示

**目标**：commit 第 1 题 Two Sum 的代码

1. 打开 VSCode
2. 打开 `F:\Cursor_vla\VLA-Adverse-Weather` 文件夹
3. 复制 `001_two_sum.py` 到 `leetcode/solutions/2026-10/`
4. 点击左侧"源代码管理"图标
5. 看到新文件 `A 001_two_sum.py`
6. 点击 `+` 暂存
7. 消息框输入：`feat(leetcode): day 1 - two sum solution`
8. 点击 `✓ 提交`
9. 点击 `↓` 推送
10. 刷新 GitHub 网页验证

**如果中间报错，把错误信息告诉我**。

## 📞 求助信号

如果以下情况发生，**立刻问我**：
- ❌ commit 报错
- ❌ push 失败
- ❌ 不知道文件该放哪
- ❌ 不知道 commit message 写啥
- ❌ 网页看不到新内容

## 🎯 长期目标

```
Day 30    : 30+ commit
Day 90    : 100+ commit
Day 180   : 200+ commit
Day 365   : 300+ commit
校招时     : 500+ commit
```

**半年后回头看，你会感谢现在每天 commit 的自己**。
