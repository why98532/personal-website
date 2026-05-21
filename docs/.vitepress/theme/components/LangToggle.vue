<template>
  <button
    @click="toggleLang"
    class="lang-toggle"
    title="切换语言 / Switch language"
  >
    <span class="lang-option" :class="{ active: isZh }">中</span>
    <span class="lang-option" :class="{ active: !isZh }">EN</span>
  </button>
</template>

<script setup>
import { useLang } from '../composables/useLang'

const { isZh, toggleLang } = useLang()
</script>

<style scoped>
.lang-toggle {
  display: flex;
  align-items: center;
  padding: 2px;
  border-radius: 7px;
  border: 1px solid rgba(255,255,255,0.1);
  background: rgba(255,255,255,0.04);
  cursor: pointer;
  transition: background 0.2s, border-color 0.2s;
}
html.light .lang-toggle {
  border-color: #d5cfc8;
  background: rgba(0,0,0,0.02);
}
.lang-toggle:hover {
  border-color: rgba(255,255,255,0.2);
}
html.light .lang-toggle:hover {
  border-color: #b0a89e;
}

.lang-option {
  font-size: 12px;
  font-weight: 500;
  padding: 2px 6px;
  border-radius: 5px;
  color: #777;
  transition: all 0.2s;
}
html.light .lang-option {
  color: #8c8279;
}

.lang-option.active {
  color: #e0e0e0;
  background: rgba(255,255,255,0.1);
}
html.light .lang-option.active {
  color: #fff;
  background: #7c3aed;
}
</style>
