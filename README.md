# 极简技术个人主页

一个极简风格的个人主页/作品集官网，基于 VitePress 和 TailwindCSS 构建。

## 功能特性

- ✅ 深色/浅色主题切换
- ✅ 响应式布局
- ✅ 文章搜索功能
- ✅ 极简设计风格
- ✅ 纯静态页面，部署简单

## 技术栈

- VitePress
- Vue 3
- TailwindCSS 4
- Lucide Icons

## 快速开始

```bash
# 安装依赖
npm install

# 启动开发服务器
npm run dev

# 构建生产版本
npm run build
```

## 项目结构

```
project-root/
├── docs/                      # VitePress 默认根目录
│   ├── .vitepress/            # 配置目录
│   │   ├── config.mjs         # 站点配置
│   │   └── theme/             # 主题目录
│   ├── public/                # 静态资源
│   ├── posts/                 # 文章目录
│   ├── index.md               # 首页
│   ├── story.md               # 故事页
│   ├── projects.md            # 作品集
│   ├── tools.md               # 工具推荐
│   └── about.md               # 关于页
├── tailwind.config.js         # TailwindCSS 配置
├── package.json
└── README.md
```

## 页面说明

1. **首页** - 个人名片展示
2. **故事** - 职业履历时间轴
3. **作品集** - 项目卡片展示
4. **文章** - 技术文章列表（带搜索）
5. **工具** - 实用工具推荐
6. **关于** - 联系信息与商务对接

## 部署

参考 `DEPLOY.md` 文件了解部署详情。

## License

MIT
