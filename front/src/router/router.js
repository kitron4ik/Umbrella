import { createRouter, createWebHistory } from "vue-router"
import Login from "@/components/Glavnaya/login.vue";

const routes = [
    {path:'/admin',component: Login},
    {
        path: '/',
        component: () => import('../pages/Main.vue'),
    },
    {
        path: '/login',
        component:() => import('../pages/LogPage.vue')
    },
    {
        path: '/dp',
        component: () => import('../pages/DrPages/DoctorPage.vue'),
    },
    {
        path: '/pp',
        component: () => import('../pages/Pacient/Pacient.vue'),
    },
    {
        path: '/pz',
        component: () => import('../pages/DrPages/PacZap.vue'),
    },
    {
        path: '/docGr',
        component: () => import('../pages/DrPages/drGr.vue'),
    },
    {
        path: '/spCard',
        component: () => import('../pages/DrPages/spCard.vue'),
    },
    {
        path: '/zp',
        component: () => import('../pages/Pacient/ZapPrim.vue'),
    },
    {
        path: '/MyCard',
        component: () => import('../pages/Pacient/MyCard.vue'),
    }
]

const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL),
})

export default router;