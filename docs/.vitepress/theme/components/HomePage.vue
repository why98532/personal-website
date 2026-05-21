<template>
  <div class="w-full">
    <!-- ==================== HERO ==================== -->
    <section class="hero-glow relative px-6 pt-28 pb-20 md:pt-40 md:pb-28 overflow-hidden">
      <!-- Background dot pattern -->
      <div class="absolute inset-0 bg-dots pointer-events-none"></div>

      <div class="max-w-2xl mx-auto text-center relative z-10">
        <!-- Avatar with glow ring -->
        <div
          class="inline-block mb-10 md:mb-12 animate-in"
          style="animation-delay: 0s"
        >
          <div class="w-28 h-28 md:w-32 md:h-32 rounded-full bg-white/[0.03] border-2 border-white/[0.06] flex items-center justify-center mx-auto animate-pulse-glow">
            <span class="text-4xl md:text-5xl font-black text-neutral-400">W</span>
          </div>
        </div>

        <h1
          class="text-4xl md:text-5xl lg:text-6xl font-extrabold tracking-tight mb-5 leading-[1.1] animate-in"
          style="animation-delay: 0.1s"
        >
          <span class="gradient-text">{{ t('hero.greeting') }}</span>
        </h1>

        <p
          class="text-lg md:text-xl text-neutral-500 dark:text-neutral-400 max-w-lg mx-auto mb-3 animate-in leading-relaxed"
          style="animation-delay: 0.2s"
        >
          {{ t('hero.title') }}
        </p>

        <p
          class="text-sm text-neutral-400 dark:text-neutral-500 mb-12 animate-in"
          style="animation-delay: 0.3s"
        >
          {{ t('hero.subtitle') }}
        </p>

        <!-- CTA buttons -->
        <div
          class="flex flex-wrap justify-center gap-3 animate-in"
          style="animation-delay: 0.4s"
        >
          <a href="/projects" class="btn-primary work-btn">
            <FolderGit2 class="w-4 h-4" />
            {{ t('nav.work') }}
          </a>
          <a href="/story" class="btn-ghost hero-nav-link">
            <ArrowRight class="w-3.5 h-3.5" />
            {{ t('nav.story') }}
          </a>
          <a href="/posts" class="btn-ghost hero-nav-link">
            <FileText class="w-3.5 h-3.5" />
            {{ t('nav.writing') }}
          </a>
        </div>
      </div>
    </section>

    <!-- ==================== STATS ==================== -->
    <section class="px-6 py-14 bg-raised border-y border-neutral-200 dark:border-white/[0.05]">
      <div class="max-w-2xl mx-auto">
        <div class="grid grid-cols-3 gap-8 text-center">
          <div
            v-for="(stat, i) in stats"
            :key="i"
            class="animate-in"
            :style="`animation-delay: ${i * 0.1}s`"
          >
            <div class="stat-number mb-2">{{ stat.number }}</div>
            <div class="text-xs text-neutral-400 dark:text-neutral-500 font-medium uppercase tracking-wider">{{ isZh ? stat.label.zh : stat.label.en }}</div>
          </div>
        </div>
      </div>
    </section>

    <!-- ==================== ABOUT ==================== -->
    <section class="px-6 py-20 md:py-28">
      <div class="max-w-2xl mx-auto">
        <div class="section-eyebrow animate-in" style="animation-delay: 0s">
          <div class="dot"></div>
          <span>{{ t('about.heading') }}</span>
        </div>

        <p
          class="text-xl md:text-2xl text-neutral-700 dark:text-neutral-300 leading-relaxed mb-8 animate-in"
          style="animation-delay: 0.1s"
        >
          {{ t('about.bio') }}
        </p>

        <div
          class="flex flex-wrap gap-2.5 animate-in"
          style="animation-delay: 0.2s"
        >
          <span class="tag-accent">{{ t('about.tag1') }}</span>
          <span class="tag-accent">{{ t('about.tag2') }}</span>
          <span class="tag-accent">{{ t('about.tag3') }}</span>
          <span class="tag-accent">{{ t('about.tag4') }}</span>
        </div>
      </div>
    </section>

    <!-- ==================== SELECTED WORK ==================== -->
    <section class="px-6 py-20 md:py-28 bg-raised border-y border-neutral-200 dark:border-white/[0.05]">
      <div class="max-w-2xl mx-auto">
        <div class="flex items-center justify-between mb-10 animate-in" style="animation-delay: 0s">
          <h2 class="text-sm font-semibold uppercase tracking-widest text-neutral-400 dark:text-neutral-500">
            {{ t('work.heading') }}
          </h2>
          <a
            href="/projects"
            class="text-xs font-medium text-neutral-400 dark:text-neutral-500 hover:text-neutral-600 dark:hover:text-neutral-300 transition-colors flex items-center gap-1"
          >
            {{ t('work.viewAll') }} <ArrowRight class="w-3 h-3" />
          </a>
        </div>

        <div class="space-y-3">
          <a
            v-for="(project, i) in projects"
            :key="i"
            :href="project.link"
            class="block group py-4 px-5 -mx-5 rounded-xl hover:bg-white/[0.03] dark:hover:bg-white/[0.03] transition-colors animate-in"
            :style="`animation-delay: ${0.1 + i * 0.08}s`"
          >
            <div>
              <h3 class="font-semibold text-neutral-800 dark:text-neutral-200 mb-1">
                {{ project.title }}
              </h3>
              <p class="text-sm text-neutral-400 dark:text-neutral-500 leading-relaxed">
                {{ projectDesc(i) }}
              </p>
            </div>
            <div class="flex items-center gap-2 flex-shrink-0">
              <span v-for="tag in project.tags" :key="tag" class="tag text-[11px]">{{ tag }}</span>
            </div>
          </a>
        </div>
      </div>
    </section>

    <!-- ==================== LATEST WRITING ==================== -->
    <section class="px-6 py-20 md:py-28">
      <div class="max-w-2xl mx-auto">
        <div class="flex items-center justify-between mb-10 animate-in" style="animation-delay: 0s">
          <div class="section-eyebrow" style="margin-bottom:0">
            <div class="dot"></div>
            <span>{{ t('writing.heading') }}</span>
          </div>
          <a
            href="/posts"
            class="text-xs font-medium text-neutral-400 dark:text-neutral-500 hover:text-neutral-600 dark:hover:text-neutral-300 transition-colors flex items-center gap-1"
          >
            {{ t('writing.allPosts') }} <ArrowRight class="w-3 h-3" />
          </a>
        </div>

        <div class="space-y-2">
          <a
            v-for="(post, i) in posts"
            :key="i"
            :href="post.link"
            class="card p-5 flex items-center justify-between gap-4 animate-in group cursor-pointer"
            :style="`animation-delay: ${0.1 + i * 0.08}s`"
          >
            <div class="min-w-0 flex items-center gap-4">
              <div class="w-10 h-10 rounded-lg bg-purple-500/10 flex items-center justify-center flex-shrink-0 group-hover:bg-purple-500/20 transition-colors">
                <FileText class="w-4 h-4 text-purple-400" />
              </div>
              <div class="min-w-0">
                <h3 class="font-medium text-sm text-neutral-800 dark:text-neutral-200 truncate group-hover:text-purple-600 dark:group-hover:text-purple-400 transition-colors">
                  {{ postTitle(i) }}
                </h3>
                <p class="text-xs text-neutral-400 dark:text-neutral-500 mt-0.5 line-clamp-1">
                  {{ postSummary(i) }}
                </p>
              </div>
            </div>
            <span class="text-xs text-neutral-400 dark:text-neutral-600 flex-shrink-0 hidden sm:block">{{ post.date }}</span>
          </a>
        </div>
      </div>
    </section>

    <!-- ==================== CONNECT ==================== -->
    <section class="px-6 py-20 md:py-28 bg-raised border-t border-neutral-200 dark:border-white/[0.05]">
      <div class="max-w-2xl mx-auto text-center">
        <div class="section-eyebrow justify-center animate-in" style="animation-delay: 0s">
          <div class="dot"></div>
          <span>{{ t('connect.heading') }}</span>
        </div>

        <p
          class="text-neutral-500 dark:text-neutral-400 mb-10 max-w-sm mx-auto leading-relaxed animate-in"
          style="animation-delay: 0.1s"
        >
          {{ t('connect.text') }}
        </p>

        <div
          class="flex flex-wrap justify-center gap-3 mb-12 animate-in"
          style="animation-delay: 0.2s"
        >
          <a href="mailto:hello@example.com" class="btn-primary work-btn">
            <Mail class="w-4 h-4" />
            hello@example.com
          </a>
          <a href="/about" class="btn-ghost">
            {{ t('connect.more') }} <ArrowRight class="w-3.5 h-3.5" />
          </a>
        </div>

        <div
          class="flex justify-center gap-3 animate-in"
          style="animation-delay: 0.3s"
        >
          <a
            v-for="social in socials"
            :key="social.label"
            :href="social.url"
            target="_blank"
            rel="noopener noreferrer"
            class="w-10 h-10 flex items-center justify-center rounded-xl border border-neutral-200 dark:border-white/[0.06] text-neutral-400 dark:text-neutral-500 hover:text-neutral-600 dark:hover:text-neutral-300 hover:border-neutral-300 dark:hover:border-white/[0.15] hover:bg-neutral-50 dark:hover:bg-white/[0.03] transition-all"
            :title="social.label"
          >
            <component :is="social.icon" class="w-4 h-4" />
          </a>
        </div>
      </div>
    </section>

    <!-- ==================== FOOTER ==================== -->
    <footer class="px-6 py-8 text-center">
      <p class="text-xs text-neutral-400 dark:text-neutral-600">
        &copy; 2026 WHY
      </p>
    </footer>
  </div>
</template>

<script setup>
import {
  ArrowRight, FolderGit2, FileText, Mail, Github, PenLine, MessageCircle
} from 'lucide-vue-next'
import { useLang } from '../composables/useLang'

const { isZh } = useLang()

const messages = {
  hero: {
    greeting: { zh: 'Hi，我是 数字收藏家', en: 'Hi, I\'m a Digital Collector' },
    title: { zh: 'AI 工程师 · 独立开发者', en: 'AI Engineer & Independent Builder' },
    subtitle: { zh: '上海 · 构建 AI 产品 · 技术写作', en: 'Shanghai · Building AI products · Writing about tech' },
  },
  nav: {
    story: { zh: '我的故事', en: 'My Story' },
    work: { zh: '作品集', en: 'Work' },
    writing: { zh: '文章', en: 'Writing' },
  },
  about: {
    heading: { zh: '关于我', en: 'About' },
    bio: { zh: '数据分析师，现 AI 领域独立开发者。我构建实用的 AI 应用，撰写技术文章，帮助团队在 AI 浪潮中找到方向。', en: 'Data analyst, now an independent AI developer. I build practical AI applications, write about technology, and help teams navigate the AI landscape.' },
    tag1: { zh: 'AI 工程化', en: 'AI Engineering' },
    tag2: { zh: '全栈开发', en: 'Full-stack Development' },
    tag3: { zh: '产品思维', en: 'Product Thinking' },
    tag4: { zh: '技术咨询', en: 'Technical Consulting' },
  },
  work: {
    heading: { zh: '精选作品', en: 'Selected Work' },
    viewAll: { zh: '查看全部', en: 'View all' },
  },
  writing: {
    heading: { zh: '最新文章', en: 'Latest Writing' },
    allPosts: { zh: '全部文章', en: 'All posts' },
  },
  connect: {
    heading: { zh: '联系我', en: 'Connect' },
    text: { zh: '有兴趣合作或只是想打个招呼？欢迎随时联系。', en: 'Interested in working together or just want to say hi? Feel free to reach out.' },
    more: { zh: '更多方式', en: 'More ways' },
  },
}

const stats = [
  { number: '2', label: { zh: '年经验', en: 'Years Exp' } },
  { number: '10+', label: { zh: '完成项目', en: 'Projects' } },
  { number: '20+', label: { zh: '技术文章', en: 'Articles' } },
]

const projectDescs = [
  { zh: '基于大语言模型的智能助手，支持多轮对话、文档理解和任务执行', en: 'LLM-powered assistant with multi-turn dialogue, document understanding, and task execution.' },
  { zh: '企业级实时数据分析仪表盘，支持交互式图表和自定义报表', en: 'Real-time enterprise analytics dashboard with interactive charts and custom reporting.' },
  { zh: '全功能订单管理、库存和数据分析平台', en: 'Full-featured order management, inventory, and analytics platform.' },
]

const postContents = [
  { title: { zh: '2025 年 AI 工具推荐：10 款开发效率神器', en: '2025 AI Tools: 10 Essential Picks for Developers' }, summary: { zh: '精选最实用的 AI 工具，涵盖编程、设计、写作等多个领域', en: 'A curated list of the most practical AI tools covering coding, design, writing, and more.' } },
  { title: { zh: 'LLM 应用开发实战：从概念到落地', en: 'Building LLM Applications: From Concept to Production' }, summary: { zh: '使用 LangChain 和 OpenAI API 构建 LLM 应用的实战指南', en: 'A hands-on guide to building LLM-powered apps with LangChain and OpenAI.' } },
  { title: { zh: '现代前端开发：Vite + Vue 3 实践', en: 'Modern Frontend with Vite + Vue 3' }, summary: { zh: '从零搭建 Vue 3 项目，涵盖路由、状态管理和 Tailwind CSS', en: 'Set up a modern Vue 3 project with routing, state management, and Tailwind CSS.' } },
]

const projects = [
  { title: 'AI Assistant Platform', tags: ['LLM', 'RAG', 'Agent'], link: '/projects' },
  { title: 'Data Visualization Dashboard', tags: ['D3.js', 'React', 'WebSocket'], link: '/projects' },
  { title: 'E-commerce Backend System', tags: ['Vue', 'Node.js', 'Postgres'], link: '/projects' },
]

const posts = [
  { date: '2025-01-15', link: '/posts/ai-tools-2025' },
  { date: '2025-01-05', link: '/posts/llm-app-dev' },
  { date: '2024-12-10', link: '/posts/vite-vue3' },
]

const socials = [
  { label: 'GitHub', icon: Github, url: 'https://github.com' },
  { label: 'Xiaohongshu', icon: PenLine, url: 'https://xiaohongshu.com' },
  { label: 'WeChat', icon: MessageCircle, url: '#' },
]

function t(path) {
  const keys = path.split('.')
  let result = messages
  for (const k of keys) result = result[k]
  return isZh.value ? result.zh : result.en
}

function projectDesc(i) { return isZh.value ? projectDescs[i].zh : projectDescs[i].en }
function postTitle(i) { return isZh.value ? postContents[i].title.zh : postContents[i].title.en }
function postSummary(i) { return isZh.value ? postContents[i].summary.zh : postContents[i].summary.en }
</script>
