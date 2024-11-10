import { createRouter, createWebHistory } from 'vue-router';
import Login from '@/components/Glavnaya/login.vue';
import { useUserStore } from '@/stores/userStore';

const routes = [
    { path: '/admin', component: Login },
    {
        path: '/',
        component: () => import('../pages/Main.vue'),
    },
    {
        path: '/dp',
        component: () => import('../pages/DrPages/DoctorPage.vue'),
        meta: { requiresAuth: true },
    },
    {
        path: '/pp',
        component: () => import('../pages/Pacient/Pacient.vue'),
        meta: { requiresAuth: true },
    },
    {
        path: '/pz',
        component: () => import('../pages/DrPages/PacZap.vue'),
        meta: { requiresAuth: true },
    },
    {
        path: '/docGr',
        component: () => import('../pages/DrPages/drGr.vue'),
        meta: { requiresAuth: true },
    },
    {
        path: '/spCard',
        component: () => import('../pages/DrPages/spCard.vue'),
        meta: { requiresAuth: true },
    },
    {
        path: '/zp',
        component: () => import('../pages/Pacient/ZapPrim.vue'),
        meta: { requiresAuth: true },
    },
    {
        path: '/MyCard',
        component: () => import('../pages/Pacient/MyCard.vue'),
        meta: { requiresAuth: true },
    },
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

// Проверка авторизации перед каждым переходом
router.beforeEach((to, from, next) => {
    const userStore = useUserStore();
    if (to.meta.requiresAuth && !userStore.isAuthenticated) {
        next('/'); 
    } else {
        next(); 
    }
});



export default router;
