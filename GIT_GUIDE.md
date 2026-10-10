# Git 完整操作指引（手把手版）

> 适合 Git 新手。每一步都有详细说明。

## 第一部分：准备工作

### 1.1 安装 Git

**Windows**:
1. 打开 https://git-scm.com/download/win
2. 下载 64-bit Git for Windows Setup
3. 双击安装：**所有选项全部用默认**（一路 Next）
4. 安装完成后，在开始菜单找到 `Git Bash`（后续用这个）

**Mac**:
```bash
# Mac自带git，或者：
brew install git
```

**Linux**:
```bash
sudo apt install git
```

### 1.2 验证安装

打开 Git Bash（或 PowerShell），输入：
```bash
git --version
```
应该看到：`git version 2.x.x`

### 1.3 配置身份（必做！）

```bash
git config --global user.name "你的名字"
git config --global user.email "your_email@example.com"
```

> ⚠️ 邮箱最好和你 GitHub 注册邮箱一致

### 1.4 配置 SSH 密钥（可选但推荐）

避免每次 push 都输密码：

```bash
# 1. 生成密钥（一路回车）
ssh-keygen -t ed25519 -C "your_email@example.com"

# 2. 复制公钥（Windows用 clip，Mac用 pbcopy）
cat ~/.ssh/id_ed25519.pub | clip

# 3. 到 GitHub 设置：
#    Settings → SSH and GPG keys → New SSH key
#    Title 随便填
#    Key 粘贴刚才复制的
#    点击 Add SSH key
```

---

## 第二部分：创建 GitHub 仓库

### 2.1 登录 GitHub
打开 https://github.com 并登录

### 2.2 新建仓库

1. 右上角 `+` 号 → `New repository`
2. 填写：
   - **Repository name**: `VLA-Adverse-Weather`
   - **Description**: `Research notes and reproductions on VLA for autonomous driving in adverse weather`
   - **Public**（公开，选Private简历上看不到）
   - ⬜ Add a README file（**不勾选**，我们手动建）
   - ⬜ Add .gitignore（**不勾选**，我们手动建）
   - ⬜ Choose a license（**不勾选**，我们手动建）
3. 点击 `Create repository`

### 2.3 记录仓库 URL
创建后页面会显示两种URL：
- HTTPS: `https://github.com/你的用户名/VLA-Adverse-Weather.git`
- SSH: `git@github.com:你的用户名/VLA-Adverse-Weather.git`

记下来，下面要用。

---

## 第三部分：本地操作

### 3.1 准备工作目录

打开 Git Bash：

```bash
# 进入 F:\Cursor_vla
cd /f/Cursor_vla

# 创建仓库目录
mkdir VLA-Adverse-Weather
cd VLA-Adverse-Weather
```

### 3.2 初始化 Git

```bash
git init
```

应该看到：`Initialized empty Git repository in F:/Cursor_vla/VLA-Adverse-Weather/.git/`

### 3.3 添加远程仓库

```bash
# 用 HTTPS（简单）
git remote add origin https://github.com/你的用户名/VLA-Adverse-Weather.git

# 或用 SSH（推荐，无需每次输密码）
git remote add origin git@github.com:你的用户名/VLA-Adverse-Weather.git
```

### 3.4 复制我准备好的所有文件

把 `F:\Cursor_vla\github-template\` 下的所有文件**复制**到 `F:\Cursor_vla\VLA-Adverse-Weather\` 下：

```
README.md
.gitignore
LICENSE
papers/README.md
papers/adverse-weather/jarvisir.md
papers/adverse-weather/seal.md
papers/adverse-weather/drivevlm.md
datasets/README.md
code/README.md
tools/README.md
notes/README.md
```

### 3.5 检查状态

```bash
git status
```

应该看到一堆 `Untracked files` 列表。

### 3.6 暂存所有文件

```bash
git add .
```

`add .` 表示添加所有文件。如果只想添加某个文件：
```bash
git add README.md
```

### 3.7 提交（commit）

```bash
git commit -m "feat: initialize repo with paper notes and structure"
```

commit message 规范：
- `feat:` 新功能
- `fix:` 修bug
- `docs:` 文档更新
- `style:` 格式调整
- `refactor:` 重构

### 3.8 推送到 GitHub

```bash
# 第一次推送需要 -u 参数
git branch -M main
git push -u origin main
```

如果是 HTTPS，会要求输入 GitHub 用户名和密码。
> ⚠️ 现在 GitHub 不再支持密码登录，需要用 **Personal Access Token (PAT)**

#### 生成 PAT 的方法：
1. GitHub 右上角头像 → `Settings`
2. 左侧最下 `Developer settings`
3. `Personal access tokens` → `Tokens (classic)` → `Generate new token`
4. 勾选 `repo`（全选）
5. 底部 `Generate token`
6. **复制token**（只显示一次！）

之后 push 时：
- Username: 你的GitHub用户名
- Password: 粘贴 PAT（不是密码）

---

## 第四部分：日常使用

### 4.1 修改文件后提交

```bash
# 1. 看改了什么
git status
git diff

# 2. 暂存
git add .

# 3. 提交
git commit -m "docs: add weekly review"

# 4. 推送
git push
```

### 4.2 拉取更新

```bash
# 当你在多台设备上工作时，先拉取
git pull
```

### 4.3 常用命令速查

| 命令 | 作用 |
|------|------|
| `git status` | 看状态 |
| `git log` | 看提交历史 |
| `git log --oneline` | 简洁版历史 |
| `git diff` | 看具体改动 |
| `git add <file>` | 暂存文件 |
| `git commit -m "msg"` | 提交 |
| `git push` | 推送到 GitHub |
| `git pull` | 拉取更新 |
| `git clone <url>` | 克隆仓库 |

### 4.4 撤销操作（危险！慎用）

```bash
# 撤销工作区修改（未暂存）
git checkout -- <file>

# 撤销暂存
git reset HEAD <file>

# 修改最后一次 commit message
git commit --amend -m "new message"
```

---

## 第五部分：进阶技巧

### 5.1 分支管理

```bash
# 创建并切换分支
git checkout -b feature/paper-notes

# 看所有分支
git branch

# 切换分支
git checkout main

# 合并分支
git merge feature/paper-notes

# 删除分支
git branch -d feature/paper-notes
```

### 5.2 处理冲突

当多人改同一个文件时：
1. `git pull` 时可能冲突
2. 打开冲突文件，会看到：
```
<<<<<<< HEAD
你的修改
=======
别人的修改
>>>>>>> branch-name
```
3. 手动编辑保留正确的内容
4. 删除 `<<<<`、`====`、`>>>>` 标记
5. `git add .` → `git commit` → `git push`

### 5.3 .gitignore 规则

```gitignore
# 忽略文件夹
__pycache__/
*.pyc

# 忽略文件
*.log
*.tmp

# 不忽略（!取反）
!important.log
```

---

## 第六部分：常见问题

### Q1: push 时报错 "failed to push some refs"
**原因**: 远程有更新，本地没拉取
**解决**:
```bash
git pull --rebase
git push
```

### Q2: commit 后想撤回
```bash
# 保留修改，只撤回 commit
git reset --soft HEAD^

# 完全撤回（危险！）
git reset --hard HEAD^
```

### Q3: 想删除 GitHub 上的文件但保留本地
```bash
git rm --cached <file>
git commit -m "chore: remove file from tracking"
git push
```

### Q4: 误把大文件 commit 了
```bash
# 从历史中删除
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch path/to/file" \
  --prune-empty --tag-name-filter cat -- --all

git push --force
```

### Q5: 配置全局 .gitignore

不想某些文件出现在任何仓库：
```bash
git config --global core.excludesfile ~/.gitignore_global
```

---

## 第七部分：推荐学习资源

- **官方文档**: https://git-scm.com/doc
- **可视化学习**: https://learngitbranching.js.org/
- **常用命令速查**: https://training.github.com/downloads/github-git-cheat-sheet/
- **VSCode Git 集成**: Ctrl+Shift+G 直接用

---

## 🎯 今天你的 Git 任务清单

- [ ] 安装 Git
- [ ] 配置 user.name 和 user.email
- [ ] 创建 GitHub 仓库
- [ ] 初始化本地仓库
- [ ] 复制我准备的所有文件
- [ ] 第一次 commit + push 成功
- [ ] 在仓库里看到 README.md 渲染正常

完成后回来告诉我，我会接着帮你推进。
