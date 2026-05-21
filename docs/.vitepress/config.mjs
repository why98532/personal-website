import { defineConfig } from 'vitepress'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  title: 'WHY',
  description: 'Personal website of WHY — builder, thinker, collector',
  appearance: false,
  base: '/',
  head: [
    ['meta', { name: 'viewport', content: 'width=device-width, initial-scale=1.0' }],
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' }],
    ['script', {}, `(function(){var t=localStorage.getItem('theme');if(t==='light'){document.documentElement.classList.add('light');document.documentElement.classList.remove('dark')}else{document.documentElement.classList.add('dark');document.documentElement.classList.remove('light')}})()`]
  ],
  themeConfig: {
    nav: [
      { text: '首页', link: '/' },
      { text: '故事', link: '/story' },
      { text: '作品', link: '/projects' },
      { text: '文章', link: '/posts' },
      { text: '关于', link: '/about' }
    ],
  },
  vite: {
    plugins: [tailwindcss()]
  }
})
