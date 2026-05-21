<template>
  <button
    @click="toggleTheme"
    class="theme-toggle"
    :title="isDark ? '切换到浅色模式' : '切换到深色模式'"
  >
    <Sun v-if="isDark" :size="16" />
    <Moon v-else :size="16" />
  </button>
</template>

<script setup>
import { Sun, Moon } from 'lucide-vue-next'
import { useTheme } from '../composables/useTheme'

const { isDark, toggleTheme } = useTheme()
</script>

<style scoped>
.theme-toggle {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 30px;
  height: 30px;
  border-radius: 6px;
  border: none;
  background: transparent;
  color: #999;
  cursor: pointer;
  transition: color 0.2s, background 0.2s;
}
html.light .theme-toggle {
  color: #8c8279;
}
.theme-toggle:hover {
  color: #e0e0e0;
  background: rgba(255,255,255,0.08);
}
html.light .theme-toggle:hover {
  color: #2d2822;
  background: rgba(0,0,0,0.05);
}
</style>
