<template>
  <nav class="custom-nav">
    <a
      v-for="item in items"
      :key="item.key"
      :href="item.link"
      class="custom-nav-link"
    >
      {{ isZh ? item.zh : item.en }}
    </a>
  </nav>
</template>

<script setup>
import { useData } from 'vitepress'
import { useLang } from '../composables/useLang'

const { site } = useData()
const { isZh } = useLang()
const base = site.value.base

const items = [
  { key: 'home', zh: '首页', en: 'Home', link: base },
  { key: 'story', zh: '故事', en: 'Story', link: `${base}story` },
  { key: 'writing', zh: '文章', en: 'Writing', link: `${base}posts` },
  { key: 'achievements', zh: '成果', en: 'Achievements', link: `${base}achievements` },
  { key: 'about', zh: '关于', en: 'About', link: `${base}about` },
]
</script>

<style scoped>
.custom-nav {
  display: flex;
  align-items: center;
  gap: 4px;
}

.custom-nav-link {
  display: inline-flex;
  align-items: center;
  padding: 6px 12px;
  font-size: 13px;
  font-weight: 500;
  border-radius: 8px;
  color: var(--color-dark-muted);
  transition: color 0.2s, background 0.2s;
}

html.light .custom-nav-link {
  color: var(--color-light-muted);
}

.custom-nav-link:hover {
  color: var(--color-dark-text);
  background: rgba(255,255,255,0.04);
}

html.light .custom-nav-link:hover {
  color: var(--color-light-text);
  background: rgba(0,0,0,0.04);
}
</style>
