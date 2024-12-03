import { createRouter, createWebHistory } from 'vue-router';
import Login from '@/components/Glavnaya/login.vue';

const routes = [
  { path: '/admin', component: Login },
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
    path: '/pz',
    component: () => import('../pages/DrPages/PacZap.vue'),
    props: true,
  },
  {
    path: '/docGr',
    component: () => import('../pages/DrPages/drGr.vue'),
    props: true,
  },
  {
    path: '/spCard',
    component: () => import('../pages/DrPages/spCard.vue'),
    props: true,
  },
  {
    path: '/zp',
    component: () => import('../pages/Pacient/ZapPrim.vue'),
    props: true,
  },
];

const router = createRouter({
  routes,
  history: createWebHistory(process.env.BASE_URL),
});

// Глобальный хук для передачи id во все маршруты
router.beforeEach((to, from, next) => {
  const userId = localStorage.getItem('userId'); // Берем id из localStorage
  if (userId) {
    to.params.id = userId; // Добавляем id в параметры маршрута
  }
  next();
});

export default router;
