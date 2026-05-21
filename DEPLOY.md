# 项目部署指南

本文档介绍如何将项目部署到不同的平台。

## 前置条件

确保已安装 Node.js（推荐版本 >= 18）和 npm/yarn/pnpm。

## 本地开发

```bash
# 安装依赖
npm install

# 启动开发服务器
npm run dev

# 构建生产版本
npm run build

# 预览生产版本
npm run preview
```

## 部署到 Vercel

1. 访问 [Vercel](https://vercel.com/) 并登录
2. 点击 "Add New Project"
3. 导入你的 GitHub/GitLab/Bitbucket 仓库
4. Vercel 会自动识别 VitePress 项目
5. 点击 "Deploy" 完成部署

## 部署到 GitHub Pages

1. 在仓库设置中启用 GitHub Pages
2. 设置源为 `gh-pages` 分支
3. 运行以下命令：

```bash
# 构建项目
npm run build

# 将 dist 目录推送到 gh-pages 分支
cd docs/.vitepress/dist
git init
git add -A
git commit -m 'deploy'
git push -f git@github.com:<username>/<repo>.git master:gh-pages
```

## 部署到自己的服务器

1. 构建项目：

```bash
npm run build
```

2. 将 `docs/.vitepress/dist` 目录上传到服务器
3. 配置 Nginx：

```nginx
server {
  listen 80;
  server_name your-domain.com;
  
  root /var/www/html/dist;
  index index.html;
  
  location / {
    try_files $uri $uri/ /index.html;
  }
}
```

## 配置自定义域名

部署完成后，在对应平台的域名设置中添加你的自定义域名即可。
