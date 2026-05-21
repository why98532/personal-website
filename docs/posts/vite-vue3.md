---
title: '使用 Vite + Vue3 构建现代化前端项目'
date: '2025-01-10'
summary: '从零开始搭建一个现代化的 Vue3 项目，涵盖路由、状态管理、组件库等配置'
tags: ['Vue3', 'Vite', '前端']
---

# 使用 Vite + Vue3 构建现代化前端项目

Vue3 已经成为前端开发的主流框架之一，结合 Vite 的快速开发体验，可以极大提升开发效率。本文将详细介绍如何从零开始搭建一个现代化的 Vue3 项目。

## 一、初始化项目

首先，使用 Vite 初始化一个 Vue3 项目：

```bash
npm create vite@6.5.0 . -- --template vue
```

或者使用 pnpm：

```bash
pnpm create vite@6.5.0 . --template vue
```

## 二、安装依赖

初始化完成后，安装必要的依赖：

```bash
npm install
npm install vue-router@4 pinia tailwindcss @tailwindcss/vite lucide-vue-next
```

## 三、配置 TailwindCSS

在 `vite.config.js` 中添加 TailwindCSS 插件：

```javascript
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [vue(), tailwindcss()],
})
```

创建 `src/style.css` 文件：

```css
@import "tailwindcss";

@theme {
  --color-primary: #3b82f6;
  --color-secondary: #6366f1;
}
```

## 四、配置路由

创建 `src/router/index.js`：

```javascript
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
```

## 五、配置状态管理

创建 `src/stores/counter.js`：

```javascript
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', {
  state: () => ({
    count: 0
  }),
  actions: {
    increment() {
      this.count++
    },
    decrement() {
      this.count--
    }
  }
})
```

## 六、创建组件

创建一个简单的计数器组件：

```vue
<script setup>
import { useCounterStore } from '../stores/counter'

const counter = useCounterStore()
</script>

<template>
  <div class="flex items-center gap-4">
    <button 
      @click="counter.decrement"
      class="px-4 py-2 bg-gray-200 rounded-lg hover:bg-gray-300"
    >
      -
    </button>
    <span class="text-2xl font-bold">{{ counter.count }}</span>
    <button 
      @click="counter.increment"
      class="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600"
    >
      +
    </button>
  </div>
</template>
```

## 七、运行项目

启动开发服务器：

```bash
npm run dev
```

构建生产版本：

```bash
npm run build
```

## 总结

通过以上步骤，你已经创建了一个现代化的 Vue3 项目，包含了路由、状态管理和样式框架。接下来可以根据需要添加更多功能和组件。
