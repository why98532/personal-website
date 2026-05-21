import { ref, onMounted } from 'vue'

const isDark = ref(true)

export function useTheme() {
  onMounted(() => {
    const saved = localStorage.getItem('theme')
    if (saved === 'light') {
      isDark.value = false
      document.documentElement.classList.remove('dark')
      document.documentElement.classList.add('light')
    } else {
      document.documentElement.classList.add('dark')
      document.documentElement.classList.remove('light')
    }
  })

  function toggleTheme() {
    isDark.value = !isDark.value
    if (isDark.value) {
      document.documentElement.classList.remove('light')
      document.documentElement.classList.add('dark')
      localStorage.setItem('theme', 'dark')
    } else {
      document.documentElement.classList.remove('dark')
      document.documentElement.classList.add('light')
      localStorage.setItem('theme', 'light')
    }
  }

  return { isDark, toggleTheme }
}
