import { createApp } from 'vue'
import App from './App.vue'
import './assets/style.css'
import './assets/modal.css'
import router from './router/router'


const app = createApp(App)



app
    .use(router)
    .mount('#app')

