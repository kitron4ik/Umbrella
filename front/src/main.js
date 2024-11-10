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

// Настройка маршрутизатора с проверками авторизации
router.beforeEach((to) => {
    const userStore = useUserStore(pinia);  // Инициализация userStore

    // Если пользователь авторизован, перенаправляем его на страницу в зависимости от роли
    if (userStore.isAuthenticated) {
        if (to.path === '/' || to.path === '/login') {  // Проверка если путь - главная или логин
            if (userStore.role === 'пациент') {
                return { path: '/pp' };  // Переход на страницу пациента
            } else if (userStore.role === 'доктор') {
                return { path: '/dp' };  // Переход на страницу доктора
            }
        }
    } else if (to.meta.requiresAuth && !userStore.isAuthenticated) {
        // Если страница требует авторизации, но пользователь не авторизован
        return { path: '/' };  // Перенаправляем на главную страницу
    }
});


app.mount('#app')
