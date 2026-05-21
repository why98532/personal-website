<template>
  <div class="w-full animate-in">
    <!-- Header -->
    <section class="px-6 pt-20 pb-12 md:pt-28 md:pb-16">
      <div class="max-w-2xl mx-auto">
        <div class="section-eyebrow">
          <div class="dot"></div>
          <span>{{ t('title') }}</span>
        </div>
        <div class="relative mt-6">
          <Search class="w-4 h-4 absolute left-3.5 top-1/2 -translate-y-1/2 text-neutral-300 dark:text-neutral-400 pointer-events-none" />
          <input
            v-model="searchQuery"
            type="text"
            :placeholder="t('search')"
            class="w-full pl-10 pr-4 py-2.5 text-sm rounded-xl bg-white dark:bg-white/[0.03] border border-neutral-200 dark:border-white/[0.08] focus:outline-none focus:ring-2 focus:ring-purple-500/20 focus:border-purple-500/40 dark:focus:ring-purple-500/20 dark:focus:border-purple-500/40 text-neutral-800 dark:text-neutral-200 placeholder:text-neutral-400 dark:placeholder:text-neutral-500 transition-colors"
          />
        </div>
      </div>
    </section>

    <!-- Post list -->
    <section class="px-6 py-12 md:py-16 bg-raised border-y border-neutral-200 dark:border-white/[0.05]">
      <div class="max-w-2xl mx-auto">
        <div class="space-y-2">
          <a
            v-for="(post, i) in filteredPosts"
            :key="i"
            :href="post.link"
            class="card p-5 flex items-start justify-between gap-4 group cursor-pointer"
          >
            <div class="min-w-0 flex gap-4">
              <div class="w-10 h-10 rounded-lg bg-amber-500/10 flex items-center justify-center flex-shrink-0 group-hover:bg-amber-500/20 transition-colors mt-0.5">
                <FileText class="w-4 h-4 text-amber-500" />
              </div>
              <div class="min-w-0">
                <h3 class="font-medium text-neutral-800 dark:text-neutral-200 group-hover:text-purple-600 dark:group-hover:text-purple-400 transition-colors">
                  {{ isZh ? post.title.zh : post.title.en }}
                </h3>
                <p class="text-sm text-neutral-400 dark:text-neutral-500 mt-1 line-clamp-2 leading-relaxed">{{ isZh ? post.summary.zh : post.summary.en }}</p>
                <div class="flex items-center gap-3 mt-3 text-xs text-neutral-400 dark:text-neutral-500">
                  <span class="flex items-center gap-1">
                    <Calendar class="w-3 h-3" />
                    {{ post.date }}
                  </span>
                  <span class="tag-accent text-[11px] px-2.5 py-0.5">{{ isZh ? post.category.zh : post.category.en }}</span>
                </div>
              </div>
            </div>
            <ArrowRight class="w-3.5 h-3.5 flex-shrink-0 mt-2 text-neutral-300 dark:text-neutral-600 group-hover:text-purple-500 dark:group-hover:text-purple-400 transition-colors" />
          </a>
        </div>

        <div v-if="filteredPosts.length === 0" class="text-center py-20">
          <Search class="w-10 h-10 mx-auto text-neutral-300 dark:text-neutral-600 mb-4" />
          <p class="text-sm text-neutral-400 dark:text-neutral-500">{{ t('noResults') }}</p>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { Search, Calendar, ArrowRight, FileText } from 'lucide-vue-next'
import { useLang } from '../composables/useLang'

const { isZh } = useLang()

const messages = {
  title: { zh: '文章', en: 'Writing' },
  search: { zh: '搜索文章...', en: 'Search articles...' },
  noResults: { zh: '没有找到匹配的文章', en: 'No articles match your search.' },
}

function t(key) { return isZh.value ? messages[key].zh : messages[key].en }

const searchQuery = ref('')

const posts = [
  { title: { zh: '2025 年 AI 工具推荐：10 款开发效率神器', en: '2025 AI Tools: 10 Essential Picks for Developers' }, summary: { zh: '精选最实用的 AI 工具，涵盖代码助手、智能文档、自动化测试等多个类别', en: 'A curated list of the most practical AI tools covering coding assistants, smart docs, automated testing, and more.' }, category: { zh: 'AI', en: 'AI' }, date: '2025-01-15', link: '/posts/ai-tools-2025' },
  { title: { zh: 'LLM 应用开发实战：从概念到落地', en: 'Building LLM Applications: From Concept to Production' }, summary: { zh: '使用 LangChain 和 OpenAI API 构建 LLM 应用的实战指南，包含完整代码示例', en: 'A hands-on guide to building LLM-powered applications with LangChain and OpenAI API. Complete with code examples.' }, category: { zh: '工程', en: 'Engineering' }, date: '2025-01-05', link: '/posts/llm-app-dev' },
  { title: { zh: '现代前端开发：Vite + Vue 3 实践', en: 'Modern Frontend with Vite + Vue 3' }, summary: { zh: '使用 Vite 和 Vue 3 搭建现代化前端项目，涵盖路由、状态管理和 Tailwind CSS', en: 'How to set up a modern Vue 3 project with Vite, covering routing, state management, and Tailwind CSS integration.' }, category: { zh: '前端', en: 'Frontend' }, date: '2024-12-10', link: '/posts/vite-vue3' },
  { title: { zh: 'AI 时代的程序员生存指南', en: 'Surviving the AI Era as a Developer' }, summary: { zh: '探讨 AI 对程序员职业的影响，以及如何提升自己的竞争力', en: 'How AI is reshaping the software engineering landscape and what you can do to stay relevant and thrive.' }, category: { zh: '职业', en: 'Career' }, date: '2024-10-05', link: '#' },
  { title: { zh: '微服务架构设计原则', en: 'Microservices Architecture Design Principles' }, summary: { zh: '深入理解微服务架构的核心设计原则和实战模式', en: 'Deep dive into the core design principles and practical patterns for building resilient microservice architectures.' }, category: { zh: '架构', en: 'Architecture' }, date: '2024-09-20', link: '#' },
  { title: { zh: '数据分析从入门到精通', en: 'Data Analytics: From Zero to Production' }, summary: { zh: '从数据采集到可视化，完整的数据分析学习路径与实战案例', en: 'A complete learning path from data collection to visualization, with real-world project examples.' }, category: { zh: '数据', en: 'Data' }, date: '2024-08-15', link: '#' },
]

const filteredPosts = computed(() => {
  if (!searchQuery.value) return posts
  const q = searchQuery.value.toLowerCase()
  return posts.filter(p =>
    (isZh.value ? p.title.zh : p.title.en).toLowerCase().includes(q) ||
    (isZh.value ? p.summary.zh : p.summary.en).toLowerCase().includes(q)
  )
})
</script>
