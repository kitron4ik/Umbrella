import { createRouter, createWebHistory } from 'vue-router';
import { useUserStore } from '@/stores/UserStore'; // Импортируем Pinia Store

const routes = [
  { path: '/admin', component: () => import('@/components/Glavnaya/login.vue') },
  {
    path: '/',
    component: () => import('../pages/Main.vue'),
  },
  {
    path: '/login/:id',
    component: () => import('../pages/LogPage.vue'),
    props: true,
  },
  {
    path: '/pz/:id',
    component: () => import('../pages/DrPages/PacZap.vue'),
    props: true,
  },
  {
    path: '/docGr/:id',
    component: () => import('../pages/DrPages/drGr.vue'),
    props: true,
  },
  {
    path: '/spCard/:id',
    component: () => import('../pages/DrPages/spCard.vue'),
    props: true,
  },
  {
    path: '/zp/:id',
    component: () => import('../pages/Pacient/ZapPrim.vue'),
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  const userStore = useUserStore();
  const userId = localStorage.getItem('userId') || userStore.userId;

  if (!userId && to.path !== '/login') {
    console.warn(`🚫 Доступ запрещен к ${to.path}. Пользователь не авторизован.`);
    return next('/admin'); // Важно: return next() останавливает выполнение
  }

  next(); // Вызов next() только если авторизация пройдена
});

export default router;
