import { createApp } from 'vue'
import App from './App.vue'
import './assets/style.css'
import './assets/modal.css'
import router from './router/router'
import { createPinia } from 'pinia'
import { useUserStore } from '@/stores/userStore' // Убедитесь, что путь к store указан правильно

const pinia = createPinia()
const app = createApp(App)

app.use(pinia)
app.use(router)




app.mount('#app')
