import { h } from 'vue'
import DefaultTheme from 'vitepress/theme'
import './custom.css'
import HomePage from './components/HomePage.vue'
import StoryPage from './components/StoryPage.vue'
import PostsPage from './components/PostsPage.vue'
import AboutPage from './components/AboutPage.vue'
import AchievementsPage from './components/AchievementsPage.vue'
import MonitorPage from './components/MonitorPage.vue'
import ThemeToggle from './components/ThemeToggle.vue'
import LangToggle from './components/LangToggle.vue'
import CustomNav from './components/CustomNav.vue'

export default {
  ...DefaultTheme,
  Layout: () => {
    return h(DefaultTheme.Layout, null, {
      'nav-bar-title-after': () => h(CustomNav),
      'nav-bar-content-after': () => h('div', { style: { display: 'flex', alignItems: 'center', gap: '2px' } }, [h(LangToggle), h(ThemeToggle)]),
    })
  },
  enhanceApp({ app }) {
    app.component('HomePage', HomePage)
    app.component('StoryPage', StoryPage)
    app.component('PostsPage', PostsPage)
    app.component('AboutPage', AboutPage)
    app.component('AchievementsPage', AchievementsPage)
    app.component('MonitorPage', MonitorPage)
  },
}
