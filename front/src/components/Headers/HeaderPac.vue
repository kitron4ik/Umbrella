<template>
  <header class="header">
    <div class="wrapper">
      <div class="header_wrapper">
        <div class="header_logo">
          <router-link to="/" class="header_logo_link">
            <img src="@/assets/png/logo.png" alt="logo" class="Logo" />
          </router-link>
        </div>
        <nav class="header_nav">
          <ul class="header_list" v-if="isAuthenticated">
            <li class="header_item">
              <!-- Используем строковые шаблоны для динамического пути -->
              <router-link :to="`/login/${userId}`" class="header_link">Мой профиль</router-link>
            </li>
            <li class="header_item">
              <!-- Используем строковые шаблоны для динамического пути -->
              <router-link :to="`/zp/${userId}`" class="header_link">Записаться на приём</router-link>
            </li>
          </ul>
        </nav>
      </div>
    </div>
  </header>
</template>

<script>
import { useUserStore } from "@/stores/UserStore";

export default {
  computed: {
    isAuthenticated() {
      const userStore = useUserStore();
      return localStorage.getItem('userId') || userStore.userId;
    },
    // Получаем userId из localStorage или из userStore
    userId() {
      const userStore = useUserStore();
      return localStorage.getItem('userId') || userStore.userId;
    },
  },
};
</script>

<style scoped>
.Logo {
  margin: 0 auto;
  max-width: 75px;
  max-height: 75px;
}

.header_list {
  padding: 0;
  list-style: none;
  display: flex;
}

.header_item {
  margin: 0 30px;
}

.header_link {
  text-decoration: none;
  color: #333;
  transition: color 0.3s;
}

.header_link:hover {
  color: #007BFF;
}
</style>
