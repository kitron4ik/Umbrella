<template>
  <div>
    <h1>Добро пожаловать на главную страницу</h1>
    <div v-if="isLoggedIn">
      <p>Вы вошли как: {{ regname }}</p>
      <p>Роль: {{ role }}</p>
    </div>
    <form v-else @submit.prevent="login">
      <input type="email" v-model="email" placeholder="Email" />
      <input type="password" v-model="password" placeholder="Пароль" />
      <button type="submit">Войти</button>
    </form>
  </div>
</template>

<script>
import { useUserStore } from '@/stores/UserStore';

export default {
  setup() {
    const userStore = useUserStore();
    return {
      regname: userStore.regname,
      role: userStore.role,
      isLoggedIn: userStore.isLoggedIn,
    };
  },
  methods: {
    async login() {
      // Логика авторизации (вызов API)
    },
  },
};
</script>
