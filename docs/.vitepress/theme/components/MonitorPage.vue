<template>
  <div class="w-full animate-in">
    <!-- Header -->
    <section class="px-6 pt-20 pb-12 md:pt-28 md:pb-16">
      <div class="max-w-4xl mx-auto">
        <div class="section-eyebrow">
          <div class="dot"></div>
          <span>{{ t('title') }}</span>
        </div>
        <div class="flex flex-wrap items-start justify-between gap-4 mt-4">
          <div>
            <h1 class="text-2xl md:text-3xl font-bold text-neutral-800 dark:text-neutral-200 mb-2">{{ t('heading') }}</h1>
            <div class="flex flex-wrap items-center gap-4 text-sm text-neutral-400 dark:text-neutral-500">
              <span class="flex items-center gap-1.5">
                <Clock class="w-3.5 h-3.5" />
                {{ report.meta.generated_at }}
              </span>
              <span class="tag text-[11px]">{{ report.meta.data_source }}</span>
              <span class="tag text-[11px]">v{{ report.meta.version }}</span>
            </div>
          </div>
          <button
            @click="refreshData"
            :disabled="loading"
            class="btn-primary flex items-center gap-2 flex-shrink-0"
            :class="{ 'opacity-60 cursor-not-allowed': loading }"
          >
            <RefreshCw :class="['w-4 h-4', loading && 'animate-spin']" />
            {{ loading ? t('refreshing') : t('refresh') }}
          </button>
        </div>
      </div>
    </section>

    <!-- Part 1: Market Events -->
    <section class="px-6 py-12 md:py-16 bg-raised border-y border-neutral-200 dark:border-white/[0.05]">
      <div class="max-w-4xl mx-auto">
        <div class="flex items-center gap-3 mb-6">
          <div class="w-8 h-8 rounded-lg bg-amber-500/10 flex items-center justify-center">
            <Newspaper class="w-4 h-4 text-amber-400" />
          </div>
          <h2 class="font-semibold text-sm text-neutral-800 dark:text-neutral-200">{{ isZh ? '近一周市场重大事件摘要' : 'Weekly Market Events' }}</h2>
          <span class="tag-accent text-[11px]">{{ report.part1_market_events.overall_sentiment }}</span>
        </div>
        <div v-if="report.part1_market_events.events.length > 0" class="card px-4 py-2 divide-y divide-neutral-100 dark:divide-white/[0.06]">
          <div v-for="(e, i) in report.part1_market_events.events" :key="i"
            class="flex items-center gap-3 py-2.5 first:pt-0 last:pb-0 text-xs">
            <span class="font-mono text-neutral-400 dark:text-neutral-500 w-14 flex-shrink-0">{{ e.date.slice(5) }}</span>
            <span class="w-1.5 h-1.5 rounded-full flex-shrink-0"
              :class="{'bg-emerald-400': e.sentiment === '看涨', 'bg-red-400': e.sentiment === '看跌', 'bg-neutral-400': e.sentiment === '中性'}"></span>
            <span class="flex-1 text-neutral-700 dark:text-neutral-300 truncate">{{ e.event }}</span>
            <span class="flex-shrink-0 font-medium" :class="{'text-emerald-500': e.sentiment === '看涨', 'text-red-400': e.sentiment === '看跌', 'text-neutral-400': e.sentiment === '中性'}">{{ e.sentiment }}</span>
          </div>
        </div>
        <div v-else class="card p-6 text-center">
          <p class="text-xs text-neutral-400 dark:text-neutral-500">{{ isZh ? '近期无重大市场事件' : 'No recent market events.' }}</p>
        </div>
      </div>
    </section>

    <!-- Part 2: Hot Sectors -->
    <section class="px-6 py-12 md:py-16">
      <div class="max-w-4xl mx-auto">
        <div class="flex items-center gap-3 mb-6">
          <div class="w-8 h-8 rounded-lg bg-purple-500/10 flex items-center justify-center">
            <TrendingUp class="w-4 h-4 text-purple-400" />
          </div>
          <h2 class="font-semibold text-sm text-neutral-800 dark:text-neutral-200">{{ isZh ? '当前热度前10大板块及其标的现状' : 'Top 10 Hot Sectors & Stocks' }}</h2>
        </div>
        <div class="card px-4 py-2 divide-y divide-neutral-100 dark:divide-white/[0.06]">
          <div v-for="s in report.part2_hot_sectors.sectors" :key="s.rank"
            class="flex items-center gap-3 py-2.5 first:pt-0 last:pb-0 text-xs">
            <span class="text-neutral-400 dark:text-neutral-500 w-5 flex-shrink-0 font-mono">#{{ s.rank }}</span>
            <span class="font-medium text-neutral-700 dark:text-neutral-300 w-20 flex-shrink-0 truncate">{{ s.sector_name }}</span>
            <span class="flex-1 text-neutral-400 dark:text-neutral-500 truncate">
              <template v-for="(st, si) in s.representative_stocks" :key="st.code">
                {{ st.name }}<span :class="st.change_pct >= 0 ? 'text-emerald-400' : 'text-red-400'">({{ st.change_pct >= 0 ? '+' : '' }}{{ st.change_pct }}%)</span>{{ si < s.representative_stocks.length - 1 ? '  ' : '' }}
              </template>
            </span>
            <span class="flex-shrink-0 font-mono w-16 text-right" :class="s.avg_change_pct >= 0 ? 'text-emerald-400' : 'text-red-400'">
              {{ s.avg_change_pct >= 0 ? '+' : '' }}{{ s.avg_change_pct }}%
            </span>
          </div>
        </div>
      </div>
    </section>

    <!-- Part 3: Author Opinions -->
    <section class="px-6 py-12 md:py-16 bg-raised border-y border-neutral-200 dark:border-white/[0.05]">
      <div class="max-w-4xl mx-auto">
        <div class="flex items-center gap-3 mb-6">
          <div class="w-8 h-8 rounded-lg bg-emerald-500/10 flex items-center justify-center">
            <Users class="w-4 h-4 text-emerald-400" />
          </div>
          <h2 class="font-semibold text-sm text-neutral-800 dark:text-neutral-200">{{ isZh ? '按公众号作者汇总观点' : 'Opinions by Author' }}</h2>
        </div>
        <div class="space-y-3">
          <div v-for="a in report.part3_author_opinions.authors" :key="a.author_name" class="card p-4">
            <div class="flex items-center gap-2.5 mb-3">
              <span class="w-6 h-6 rounded-full bg-emerald-500/10 flex items-center justify-center text-[10px] font-bold text-emerald-400">{{ a.author_name.charAt(0) }}</span>
              <span class="font-medium text-xs text-neutral-800 dark:text-neutral-200">{{ a.author_name }}</span>
              <span class="text-[11px] text-neutral-400 dark:text-neutral-500">{{ isZh ? `共${a.article_count}篇` : `${a.article_count} articles` }}</span>
              <span class="flex-shrink-0 text-[11px] ml-auto font-medium" :class="{'text-emerald-500': a.dominant_sentiment === '看多', 'text-red-400': a.dominant_sentiment === '看空', 'text-neutral-400': a.dominant_sentiment === '中性'}">{{ a.dominant_sentiment }}</span>
            </div>
            <div class="space-y-2.5 pl-8">
              <div v-for="art in a.articles" :key="art.article_title" class="text-xs">
                <div class="flex items-center gap-2 mb-0.5">
                  <span class="text-neutral-700 dark:text-neutral-300 font-medium truncate">{{ art.article_title }}</span>
                  <a v-if="art.source_link" :href="art.source_link" target="_blank" rel="noopener noreferrer"
                    class="text-neutral-400 dark:text-neutral-500 hover:text-purple-500 transition-colors flex-shrink-0">
                    <ExternalLink class="w-2.5 h-2.5" />
                  </a>
                  <span class="flex-shrink-0 text-[11px] font-medium" :class="{'text-emerald-500': art.sentiment === '看多', 'text-red-400': art.sentiment === '看空', 'text-neutral-400': art.sentiment === '中性'}">{{ art.sentiment }}</span>
                </div>
                <p class="text-neutral-400 dark:text-neutral-500 leading-relaxed line-clamp-2">
                  <span class="text-neutral-300 dark:text-neutral-600 mr-1">"</span>{{ art.core_opinion }}<span class="text-neutral-300 dark:text-neutral-600 ml-1">"</span>
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Part 4: Sector Recommendations -->
    <section class="px-6 py-12 md:py-16">
      <div class="max-w-4xl mx-auto">
        <div class="flex items-center gap-3 mb-6">
          <div class="w-8 h-8 rounded-lg bg-blue-500/10 flex items-center justify-center">
            <Target class="w-4 h-4 text-blue-400" />
          </div>
          <h2 class="font-semibold text-sm text-neutral-800 dark:text-neutral-200">{{ isZh ? '前五大细分板块建议' : 'Top 5 Sub-sector Recommendations' }}</h2>
          <span class="text-[11px] text-neutral-400 dark:text-neutral-500">{{ isZh ? '标注作者一致性' : 'with author consistency' }}</span>
        </div>
        <div class="card px-4 py-2 divide-y divide-neutral-100 dark:divide-white/[0.06]">
          <div v-for="r in report.part4_sector_advice.recommendations" :key="r.rank"
            class="flex items-center gap-3 py-2.5 first:pt-0 last:pb-0 text-xs">
            <span class="w-4 flex-shrink-0 font-mono text-neutral-400 dark:text-neutral-500">#{{ r.rank }}</span>
            <span class="font-medium text-neutral-700 dark:text-neutral-300 w-16 flex-shrink-0 truncate">{{ r.name }}</span>
            <span class="flex-1 text-neutral-400 dark:text-neutral-500 truncate">{{ r.reason }}</span>
            <span v-if="r.consistency_note" class="tag-accent text-[10px] flex-shrink-0 inline-flex items-center gap-0.5">
              <Link2 class="w-2.5 h-2.5" />
              {{ r.consistency_note.replace(/\[与作者(.+)一致\]/, '$1') }}
            </span>
            <span class="w-9 flex-shrink-0 text-right font-medium" :class="{'text-emerald-500': r.advice_icon === 'BUY', 'text-amber-400': r.advice_icon === 'HOLD', 'text-red-400': r.advice_icon === 'SELL'}">{{ r.advice }}</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <section class="px-6 py-12 bg-raised border-t border-neutral-200 dark:border-white/[0.05]">
      <div class="max-w-4xl mx-auto text-center">
        <p class="text-xs text-neutral-400 dark:text-neutral-500">
          {{ isZh ? '此页面展示公众号舆情监控系统的实际运行输出。点击「刷新数据」可重新加载最新报告。' : 'This page shows the actual output of the WeChat Public Account Sentiment Monitor. Click "Refresh" to reload the latest report.' }}
        </p>
      </div>
    </section>

    <!-- Toast -->
    <Transition name="toast">
      <div v-if="toast.show"
        class="fixed top-20 left-1/2 -translate-x-1/2 z-50 flex items-center gap-2 px-5 py-3 rounded-xl shadow-lg border text-sm font-medium"
        :class="toast.type === 'success'
          ? 'bg-emerald-500/10 border-emerald-500/30 text-emerald-400'
          : 'bg-red-500/10 border-red-500/30 text-red-400'"
      >
        <CheckCircle v-if="toast.type === 'success'" class="w-4 h-4" />
        <AlertCircle v-else class="w-4 h-4" />
        {{ toast.message }}
      </div>
    </Transition>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { withBase } from 'vitepress'
import {
  Newspaper, TrendingUp, Users, Target, Clock,
  Link2, ExternalLink, RefreshCw, CheckCircle, AlertCircle,
} from 'lucide-vue-next'
import { useLang } from '../composables/useLang'

const { isZh } = useLang()

const API_BASE = 'http://localhost:8765'

const messages = {
  title: { zh: '成果详情', en: 'Achievement Detail' },
  heading: { zh: '公众号舆情监控', en: 'WeChat Official Account Sentiment Monitor' },
  refresh: { zh: '刷新数据', en: 'Refresh Data' },
  refreshing: { zh: '查询中...', en: 'Fetching...' },
  done: { zh: '查询完成', en: 'Query completed' },
  error: { zh: '查询失败，请重试', en: 'Query failed, please retry' },
}

function t(key) { return isZh.value ? messages[key].zh : messages[key].en }

const loading = ref(false)
const toast = ref({ show: false, message: '', type: 'success' })

const fallbackReport = {
  meta: { title: "", version: "0.1.0", generated_at: "", data_source: "" },
  part1_market_events: { title: "", events: [], overall_sentiment: "" },
  part2_hot_sectors: { title: "", sectors: [] },
  part3_author_opinions: { title: "", authors: [] },
  part4_sector_advice: { title: "", recommendations: [] },
}

const report = ref(JSON.parse(JSON.stringify(fallbackReport)))

let toastTimer = null

function showToast(message, type = 'success') {
  clearTimeout(toastTimer)
  toast.value = { show: true, message, type }
  toastTimer = setTimeout(() => {
    toast.value.show = false
  }, 3000)
}

async function loadStaticReport(silent) {
  try {
    const url = withBase('/report.json')
    const resp = await fetch(url)
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`)
    const data = await resp.json()
    report.value = data
    return true
  } catch (err) {
    console.error('Failed to load static report:', err)
    if (!silent) showToast(t('error'), 'error')
    return false
  }
}

async function refreshData() {
  loading.value = true
  try {
    // 调用后端 API 实际运行监控脚本
    const resp = await fetch(`${API_BASE}/api/run`, { method: 'POST' })
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`)
    const data = await resp.json()
    if (data.error) throw new Error(data.error)
    report.value = data
    showToast(t('done'), 'success')
  } catch (err) {
    console.error('API call failed, falling back to static report:', err)
    // API 不可用时回退到静态文件
    const ok = await loadStaticReport(true)
    if (ok) {
      showToast(t('done'), 'success')
    } else {
      showToast(t('error'), 'error')
    }
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadStaticReport(true)
})
</script>

<style scoped>
@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
.animate-spin { animation: spin 1s linear infinite; }

.toast-enter-active { transition: all 0.3s ease; }
.toast-leave-active { transition: all 0.25s ease; }
.toast-enter-from { opacity: 0; transform: translate(-50%, -12px); }
.toast-leave-to { opacity: 0; transform: translate(-50%, -8px); }
</style>
