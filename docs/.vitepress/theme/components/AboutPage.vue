<template>
  <div class="w-full animate-in">
    <!-- Header -->
    <section class="px-6 pt-20 pb-12 md:pt-28 md:pb-16">
      <div class="max-w-2xl mx-auto">
        <div class="section-eyebrow">
          <div class="dot"></div>
          <span>{{ t('about') }}</span>
        </div>
      </div>
    </section>

    <!-- Profile card -->
    <section class="px-6 pb-12 md:pb-16">
      <div class="max-w-2xl mx-auto">
        <div class="card p-6">
          <div class="flex items-center gap-4 mb-5">
            <div class="w-14 h-14 rounded-full bg-white/[0.03] border-2 border-white/[0.06] flex items-center justify-center flex-shrink-0">
              <span class="text-xl font-black text-neutral-500">W</span>
            </div>
            <div>
              <h2 class="font-semibold text-neutral-800 dark:text-neutral-200">WHY</h2>
              <p class="text-sm text-neutral-500 dark:text-purple-500">{{ t('role') }}</p>
            </div>
          </div>
          <div class="grid sm:grid-cols-3 gap-3 text-sm text-neutral-600 dark:text-neutral-300">
            <div class="flex items-center gap-2.5">
              <MapPin class="w-4 h-4 text-purple-500 flex-shrink-0" />
              <span>{{ t('location') }}</span>
            </div>
            <div class="flex items-center gap-2.5">
              <Mail class="w-4 h-4 text-purple-500 flex-shrink-0" />
              <a href="mailto:hello@example.com" class="text-purple-500 hover:text-purple-600 dark:hover:text-purple-400 transition-colors">hello@example.com</a>
            </div>
            <div class="flex items-center gap-2.5">
              <Briefcase class="w-4 h-4 text-purple-500 flex-shrink-0" />
              <span>{{ t('experience') }}</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Services -->
    <section class="px-6 py-16 md:py-20 bg-raised border-y border-neutral-200 dark:border-white/[0.05]">
      <div class="max-w-2xl mx-auto">
        <h2 class="text-xs font-semibold uppercase tracking-wider text-purple-500 dark:text-neutral-500 mb-6">{{ t('services') }}</h2>
        <div class="grid sm:grid-cols-2 gap-4">
          <div v-for="s in services" :key="s.title.en" class="card-accent p-5">
            <h3 class="font-semibold text-sm text-neutral-800 dark:text-neutral-200 mb-1.5">{{ isZh ? s.title.zh : s.title.en }}</h3>
            <p class="text-xs text-purple-500 dark:text-neutral-500 leading-relaxed">{{ isZh ? s.desc.zh : s.desc.en }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Process -->
    <section class="px-6 py-16 md:py-20">
      <div class="max-w-2xl mx-auto">
        <h2 class="text-xs font-semibold uppercase tracking-wider text-purple-500 dark:text-neutral-500 mb-6">{{ t('process') }}</h2>
        <div class="flex flex-wrap items-center gap-2.5 text-sm">
          <template v-for="(step, i) in processList" :key="i">
            <span class="tag-accent">{{ isZh ? step.zh : step.en }}</span>
            <ArrowRight v-if="i < processList.length - 1" class="w-3.5 h-3.5 text-neutral-300 dark:text-neutral-600 flex-shrink-0" />
          </template>
        </div>
      </div>
    </section>

    <!-- Social -->
    <section class="px-6 py-16 md:py-20 bg-raised border-t border-neutral-200 dark:border-white/[0.05]">
      <div class="max-w-2xl mx-auto">
        <h2 class="text-xs font-semibold uppercase tracking-wider text-purple-500 dark:text-neutral-500 mb-6">{{ t('findMe') }}</h2>
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">
          <a v-for="link in socials" :key="link.label" :href="link.url" target="_blank" rel="noopener noreferrer" class="card p-4 text-center">
            <component :is="link.icon" class="w-5 h-5 mx-auto text-purple-500 mb-2" />
            <p class="text-xs font-medium text-neutral-700 dark:text-neutral-300">{{ link.label }}</p>
          </a>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ArrowRight, MapPin, Mail, Briefcase, MessageCircle, BookOpen, Github, PenLine } from 'lucide-vue-next'
import { useLang } from '../composables/useLang'

const { isZh } = useLang()

const messages = {
  about: { zh: '关于', en: 'About' },
  role: { zh: 'AI 工程师 · 独立开发者', en: 'AI Engineer · Independent Developer' },
  location: { zh: '中国 · 上海', en: 'Shanghai, China' },
  experience: { zh: '10+ 年技术经验', en: '10+ years in tech' },
  services: { zh: '可提供服务', en: 'What I offer' },
  process: { zh: '合作流程', en: 'How we work together' },
  findMe: { zh: '找到我', en: 'Find me on' },
}

function t(key) { return isZh.value ? messages[key].zh : messages[key].en }

const services = [
  { title: { zh: 'AI 应用开发', en: 'AI Application Development' }, desc: { zh: '从需求分析到产品落地，一站式 AI 应用开发服务，涵盖 LLM 集成、RAG、Agent 等方向', en: 'End-to-end AI product development — from requirements to deployment. LLM integration, RAG, agents.' } },
  { title: { zh: '技术咨询', en: 'Technical Consulting' }, desc: { zh: '提供技术架构设计、代码审查、性能优化建议，帮助企业做出更好的技术决策', en: 'Architecture design, code review, performance optimization. Helping teams make better technical decisions.' } },
  { title: { zh: '方案梳理与架构设计', en: 'Solution Architecture' }, desc: { zh: '针对业务需求梳理技术方案，设计可扩展的系统架构', en: 'Translating business requirements into scalable, maintainable technical architectures.' } },
  { title: { zh: '团队 AI 培训', en: 'Team AI Training' }, desc: { zh: '面向技术团队的 AI 通识与实战培训，帮助团队快速掌握 AI 开发能力', en: 'Hands-on AI workshops for engineering teams. From fundamentals to production-ready systems.' } },
]

const processList = [
  { zh: '邮件简介', en: 'Email intro' },
  { zh: '预约沟通', en: 'Discovery call' },
  { zh: '方案输出', en: 'Proposal' },
  { zh: '合作落地', en: 'Engagement' },
]

const socials = [
  { label: 'GitHub', icon: Github, url: 'https://github.com' },
  { label: '小红书', icon: PenLine, url: 'https://xiaohongshu.com' },
  { label: '微信', icon: MessageCircle, url: '#' },
  { label: '博客', icon: BookOpen, url: '/posts' },
]
</script>
