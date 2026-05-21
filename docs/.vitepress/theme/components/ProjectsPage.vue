<template>
  <div class="w-full animate-in">
    <!-- Header -->
    <section class="px-6 pt-20 pb-12 md:pt-28 md:pb-16">
      <div class="max-w-4xl mx-auto">
        <div class="section-eyebrow">
          <div class="dot"></div>
          <span>{{ t('title') }}</span>
        </div>
        <p class="text-neutral-500 dark:text-neutral-400 text-sm">{{ t('subtitle') }}</p>
      </div>
    </section>

    <!-- Projects grid -->
    <section class="px-6 py-12 md:py-16 bg-raised border-y border-neutral-200 dark:border-white/[0.05]">
      <div class="max-w-4xl mx-auto">
        <div class="grid md:grid-cols-2 gap-5">
          <div v-for="(project, i) in projects" :key="i" class="card-accent overflow-hidden">
            <div class="aspect-video bg-white/[0.02] dark:bg-white/[0.02] flex items-center justify-center relative overflow-hidden">
              <div class="absolute inset-0 bg-dots"></div>
              <FolderGit2 class="w-8 h-8 text-neutral-300 dark:text-neutral-600 relative z-10" />
            </div>
            <div class="p-5">
              <h3 class="font-semibold text-neutral-800 dark:text-neutral-200 mb-1">{{ isZh ? project.title.zh : project.title.en }}</h3>
              <p class="text-sm text-neutral-400 dark:text-neutral-500 mb-4 leading-relaxed">{{ isZh ? project.desc.zh : project.desc.en }}</p>
              <div class="flex flex-wrap gap-1.5 mb-4">
                <span v-for="tag in project.tags" :key="tag" class="tag text-[11px]">{{ tag }}</span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-xs text-neutral-400 dark:text-neutral-500">{{ project.date }}</span>
                <a :href="project.link" target="_blank" class="text-xs font-medium text-neutral-400 dark:text-neutral-500 hover:text-purple-600 dark:hover:text-purple-400 flex items-center gap-1 transition-colors">
                  {{ t('view') }} <ExternalLink class="w-3 h-3" />
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { FolderGit2, ExternalLink } from 'lucide-vue-next'
import { useLang } from '../composables/useLang'

const { isZh } = useLang()

const messages = {
  title: { zh: '作品集', en: 'Work' },
  subtitle: { zh: '精选项目展示', en: 'Selected projects' },
  view: { zh: '查看', en: 'View' },
}

function t(key) { return isZh.value ? messages[key].zh : messages[key].en }

const projects = [
  { title: { zh: 'AI 智能助手平台', en: 'AI Assistant Platform' }, desc: { zh: '基于大语言模型的智能助手，支持多轮对话、文档理解和任务执行', en: 'LLM-powered assistant with multi-turn dialogue, document understanding, and task execution capabilities.' }, tags: ['LLM', 'RAG', 'Agent', 'Vue'], date: '2025', link: '#' },
  { title: { zh: '数据可视化仪表盘', en: 'Data Visualization Dashboard' }, desc: { zh: '企业级实时数据分析仪表盘，支持交互式图表、自定义报表和权限控制', en: 'Enterprise-grade real-time analytics with interactive charts, custom reporting, and role-based access.' }, tags: ['D3.js', 'React', 'WebSocket', 'Python'], date: '2024', link: '#' },
  { title: { zh: '电商后台管理系统', en: 'E-commerce Management System' }, desc: { zh: '完整的订单、库存和数据分析平台，日均服务 10k+ 活跃商家', en: 'Complete order, inventory, and analytics platform serving 10k+ daily active merchants.' }, tags: ['Vue', 'Node.js', 'Postgres', 'Redis'], date: '2024', link: '#' },
  { title: { zh: '在线教育平台', en: 'Online Learning Platform' }, desc: { zh: '一站式在线学习方案，支持视频课程、直播教学和学习进度追踪', en: 'One-stop learning solution with video courses, live streaming, and progress tracking.' }, tags: ['WebRTC', 'Next.js', 'AWS'], date: '2023', link: '#' },
  { title: { zh: '智能客服系统', en: 'Intelligent Customer Service' }, desc: { zh: '基于 NLP 的智能客服系统，支持自动问答和人工无缝转接', en: 'NLP-based customer service system with auto-answering and seamless human handoff.' }, tags: ['NLP', 'Python', 'FastAPI'], date: '2023', link: '#' },
  { title: { zh: '物联网数据平台', en: 'IoT Data Platform' }, desc: { zh: '物联网设备数据采集和分析平台，支持海量设备接入和实时监控', en: 'Device data collection and analytics platform supporting massive device connections and real-time monitoring.' }, tags: ['IoT', 'MQTT', 'TimescaleDB'], date: '2022', link: '#' },
]
</script>
