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
              <!-- Динамическая ссылка на профиль пользователя с userId -->
              <router-link :to="`/login/${userId}`" class="header_link">Мой профиль</router-link>
            </li>
            <li class="header_item">
              <!-- Динамическая ссылка на страницу записи с userId -->
              <router-link :to="`/pz/${userId}`" class="header_link">Пациенты на запись</router-link>
            </li>
            <li class="header_item">
              <!-- Динамическая ссылка на список карт с userId -->
              <router-link :to="`/spCard/${userId}`" class="header_link">Список карт</router-link>
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
  margin: 0 20px;
}

.header_link {
  text-decoration: none;
  color: #007BFF;
  transition: color 0.3s;
}

.header_link:hover {
  color: #0056b3;
}
</style>
