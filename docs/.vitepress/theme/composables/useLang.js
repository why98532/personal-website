import { ref, onMounted } from 'vue'

const isZh = ref(true)

export function useLang() {
  onMounted(() => {
    const saved = localStorage.getItem('lang')
    if (saved === 'en') {
      isZh.value = false
    }
  })

  function toggleLang() {
    isZh.value = !isZh.value
    localStorage.setItem('lang', isZh.value ? 'zh' : 'en')
  }

  return { isZh, toggleLang }
}
