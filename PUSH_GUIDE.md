# 推送仓库到 GitHub 完整操作

## 当前状态
- ✅ 本地仓库已初始化
- ✅ 第一次 commit 完成 (15文件, 1218行)
- ✅ 远程 origin 已关联: https://github.com/jiajinze/VLA-Adverse-Weather.git
- ⏳ 等待推送

## 推送步骤

### Step 1: 创建 Personal Access Token (PAT)
1. 打开 https://github.com/settings/tokens
2. 点击 "Generate new token" → "Generate new token (classic)"
3. Note: 填 "vscode-laptop"
4. Expiration: 选 "90 days" 或 "No expiration"
5. 勾选 "repo" (这个 scope 必选)
6. 点击 "Generate token"
7. **复制 token** (只显示一次！页面关了就看不到了)

### Step 2: 在 VSCode 终端推送
打开 VSCode 终端 (Ctrl+`), 然后运行:
```bash
cd F:\Cursor_vla\VLA-Adverse-Weather
git push -u origin master
```

> 注意：我本地用的分支是 master (Git 默认)，如果 GitHub 仓库默认是 main，可能会需要：
> ```bash
> git branch -M main
> git push -u origin main
> ```

### Step 3: 凭据输入
- Username: jiajinze
- Password: 粘贴刚才复制的 token (不是密码！)

### Step 4: 验证
- 打开 https://github.com/jiajinze/VLA-Adverse-Weather
- 刷新页面，应该看到 15 个文件

## 推送命令备选 (我帮你执行)

如果想我帮你直接推送，告诉我:
1. 你已生成 PAT token
2. 把 token 告诉我 (我会立刻推送然后建议你删除 token)

## 推送失败常见原因
- 403 / authentication failed → token 失效或粘贴错
- repository not found → 仓库 URL 错或仓库是私有的需要权限
- failed to push some refs → 远程有文件，先 `git pull --rebase`
