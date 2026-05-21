<template>
  <div class="w-full animate-in">
    <!-- Header -->
    <section class="px-6 pt-20 pb-12 md:pt-28 md:pb-16">
      <div class="max-w-2xl mx-auto">
        <div class="section-eyebrow">
          <div class="dot"></div>
          <span>{{ t('title') }}</span>
        </div>
        <p class="text-neutral-500 dark:text-purple-500 text-sm">{{ t('subtitle') }}</p>
      </div>
    </section>

    <!-- Timeline -->
    <section class="px-6 py-16 md:py-20 bg-raised border-y border-neutral-200 dark:border-white/[0.05]">
      <div class="max-w-2xl mx-auto">
        <h2 class="text-xs font-semibold uppercase tracking-wider text-purple-500 dark:text-neutral-500 mb-10">{{ t('career') }}</h2>
        <div class="relative">
          <div class="absolute left-[15px] top-2 bottom-2 w-px bg-neutral-200 dark:bg-white/[0.08]" />
          <div class="space-y-14">
            <div v-for="(item, i) in timeline" :key="i" class="flex gap-5 group">
              <div
                class="relative z-10 w-[30px] h-[30px] rounded-full flex items-center justify-center flex-shrink-0 text-[10px] font-bold text-white shadow-lg"
                :class="item.color"
              >
                {{ item.year }}
              </div>
              <div class="pt-0.5">
                <h3 class="font-semibold text-neutral-800 dark:text-neutral-200">{{ isZh ? item.role.zh : item.role.en }}</h3>
                <p class="text-sm text-neutral-500 dark:text-purple-500 mt-0.5">{{ isZh ? item.company.zh : item.company.en }}</p>
                <p class="text-sm text-purple-500 dark:text-neutral-500 mt-1.5 leading-relaxed">{{ isZh ? item.desc.zh : item.desc.en }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Growth -->
    <section class="px-6 py-16 md:py-20">
      <div class="max-w-2xl mx-auto">
        <h2 class="text-xs font-semibold uppercase tracking-wider text-purple-500 dark:text-neutral-500 mb-6">{{ t('growth') }}</h2>
        <div class="flex flex-wrap items-center gap-2.5 text-sm">
          <template v-for="(step, i) in growthPath" :key="i">
            <span class="tag-accent">{{ isZh ? step.zh : step.en }}</span>
            <ArrowRight v-if="i < growthPath.length - 1" class="w-3.5 h-3.5 text-neutral-300 dark:text-neutral-600 flex-shrink-0" />
          </template>
        </div>
      </div>
    </section>

    <!-- Strengths -->
    <section class="px-6 py-16 md:py-20 bg-raised border-y border-neutral-200 dark:border-white/[0.05]">
      <div class="max-w-2xl mx-auto">
        <h2 class="text-xs font-semibold uppercase tracking-wider text-purple-500 dark:text-neutral-500 mb-8">{{ t('strengths') }}</h2>
        <div class="grid sm:grid-cols-3 gap-4">
          <div v-for="s in strengths" :key="s.title.en" class="card-accent p-5">
            <component :is="s.icon" class="w-5 h-5 text-purple-500 mb-3" />
            <h3 class="font-semibold text-sm text-neutral-800 dark:text-neutral-200 mb-1.5">{{ isZh ? s.title.zh : s.title.en }}</h3>
            <p class="text-xs text-purple-500 dark:text-neutral-500 leading-relaxed">{{ isZh ? s.desc.zh : s.desc.en }}</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ArrowRight, Rocket, Zap, Layers } from 'lucide-vue-next'
import { useLang } from '../composables/useLang'

const { isZh } = useLang()

const messages = {
  title: { zh: '我的故事', en: 'My Story' },
  subtitle: { zh: '从全栈工程师到 AI 独立开发者', en: 'From full-stack engineer to AI independent developer' },
  career: { zh: '职业履历', en: 'Career' },
  growth: { zh: '能力升级路径', en: 'Growth Path' },
  strengths: { zh: '核心优势', en: 'Strengths' },
}

function t(key) { return isZh.value ? messages[key].zh : messages[key].en }

const timeline = [
  { year: '24', role: { zh: 'AI 独立开发者', en: 'AI Independent Developer' }, company: { zh: '自由职业', en: 'Freelance' }, desc: { zh: '专注于 AI 应用开发和技术咨询，服务多个行业客户', en: 'Building AI applications and providing technical consulting for clients across multiple industries.' }, color: 'bg-purple-500' },
  { year: '21', role: { zh: '高级技术专家', en: 'Senior Tech Lead' }, company: { zh: '某大厂', en: 'Big Tech' }, desc: { zh: '负责核心系统架构设计和团队管理，主导了多个重要项目的技术方案', en: 'Led core system architecture design and team management. Drove technical strategy for key projects.' }, color: 'bg-emerald-500' },
  { year: '18', role: { zh: '技术主管', en: 'Tech Lead' }, company: { zh: '某互联网公司', en: 'Internet Company' }, desc: { zh: '带领团队完成多个核心项目交付，推动前端工程化落地', en: 'Delivered multiple core projects and established frontend engineering practices across the team.' }, color: 'bg-purple-500' },
  { year: '15', role: { zh: '全栈工程师', en: 'Full-stack Engineer' }, company: { zh: '创业公司', en: 'Startup' }, desc: { zh: '从 0 到 1 搭建产品技术体系，覆盖前后端和基础架构', en: 'Built product and technical infrastructure from zero to one, covering frontend, backend, and DevOps.' }, color: 'bg-amber-500' },
]

const growthPath = [
  { zh: '编程基础', en: 'Engineering' },
  { zh: '全栈开发', en: 'Full-stack' },
  { zh: '技术管理', en: 'Tech Leadership' },
  { zh: 'AI 工程化', en: 'AI Engineering' },
]

const strengths = [
  { icon: Rocket, title: { zh: '从 0 到 1 搭建 AI 应用', en: '0 to 1 AI Products' }, desc: { zh: '丰富的项目经验，独立完成 AI 应用的设计、开发和部署', en: 'Proven track record of independently designing, building, and deploying AI applications end to end.' } },
  { icon: Zap, title: { zh: '快速迭代交付', en: 'Fast Iteration' }, desc: { zh: '敏捷开发理念，快速响应需求变化，确保项目按时交付', en: 'Agile mindset with rapid prototyping. Quick to respond to changing requirements without sacrificing quality.' } },
  { icon: Layers, title: { zh: '全栈技术能力', en: 'Full-stack Capability' }, desc: { zh: '前端、后端、AI 模型、部署运维，一站式解决问题', en: 'Frontend, backend, AI models, deployment — I handle the entire stack.' } },
]
</script>
