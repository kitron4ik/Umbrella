import { createApp } from 'vue'
import App from './App.vue'
import './assets/style.css'
import './assets/modal.css'
import router from './router/router'
import { createPinia } from 'pinia';

const pinia = createPinia(); 
const app = createApp(App)



app.use(router).mount('#app')

app.use(pinia)


