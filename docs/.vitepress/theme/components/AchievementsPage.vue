<template>
  <div class="w-full animate-in">
    <!-- Header -->
    <section class="px-6 pt-20 pb-12 md:pt-28 md:pb-16">
      <div class="max-w-2xl mx-auto">
        <div class="section-eyebrow">
          <div class="dot"></div>
          <span>{{ t('title') }}</span>
        </div>
        <p class="text-neutral-500 dark:text-neutral-400 text-sm">{{ t('subtitle') }}</p>
      </div>
    </section>

    <!-- Achievements list -->
    <section class="px-6 py-12 md:py-16 bg-raised border-y border-neutral-200 dark:border-white/[0.05]">
      <div class="max-w-2xl mx-auto">
        <div class="space-y-4">
          <a v-for="(item, i) in achievements" :key="i" :href="withBase(item.link)"
            class="card-accent p-6 block group cursor-pointer">
            <div class="flex items-start gap-4">
              <div class="w-12 h-12 rounded-xl bg-emerald-500/10 flex items-center justify-center flex-shrink-0 group-hover:bg-emerald-500/20 transition-colors">
                <Trophy class="w-6 h-6 text-emerald-400" />
              </div>
              <div class="min-w-0 flex-1">
                <div class="flex items-center justify-between mb-1.5">
                  <h3 class="font-semibold text-neutral-800 dark:text-neutral-200 group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition-colors">{{ isZh ? item.title.zh : item.title.en }}</h3>
                  <ArrowRight class="w-4 h-4 flex-shrink-0 text-neutral-300 dark:text-neutral-600 group-hover:text-emerald-500 dark:group-hover:text-emerald-400 transition-colors ml-2" />
                </div>
                <p class="text-sm text-neutral-400 dark:text-neutral-500 mb-4 leading-relaxed">{{ isZh ? item.desc.zh : item.desc.en }}</p>
                <div class="flex flex-wrap items-center gap-3">
                  <span v-for="tag in item.tags" :key="tag" class="tag text-[11px]">{{ tag }}</span>
                  <span class="text-xs text-neutral-400 dark:text-neutral-500 ml-auto">{{ item.date }}</span>
                </div>
              </div>
            </div>
          </a>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { withBase } from 'vitepress'
import { Trophy, ArrowRight } from 'lucide-vue-next'
import { useLang } from '../composables/useLang'

const { isZh } = useLang()

const messages = {
  title: { zh: '成果', en: 'Achievements' },
  subtitle: { zh: '项目成果与产出', en: 'Project achievements and deliverables' },
}

function t(key) { return isZh.value ? messages[key].zh : messages[key].en }

const achievements = [
  {
    title: { zh: '公众号内容舆情监控', en: 'WeChat Official Account Content Sentiment Monitor' },
    desc: { zh: '实时监控公众号内容舆情，自动化舆情分析与预警系统。支持多公众号同时监控、关键词告警、情感分析、趋势追踪等功能。', en: 'Real-time content sentiment monitoring and automated alerting system for WeChat official accounts. Supports multi-account monitoring, keyword alerts, sentiment analysis, and trend tracking.' },
    tags: ['Python', 'NLP', 'WeChat API', 'Sentiment Analysis'],
    date: '2025',
    link: '/achievements/monitor',
  },
]
</script>
