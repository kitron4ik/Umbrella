<template>
  <header class="header">
    <div class="wrapper">
      <div class="header_wrapper">
        <div class="header_logo">
          <a href="/" class="header_logo_link">
            <img src="../../assets/png/logo.png" alt="logo" class="Logo" />
          </a>
        </div>
        <nav class="header_nav">
          <ul class="header_list" v-if="isAuthenticated">
            <li class="header_item">
              <a href="/login" class="header_link">Мой профиль</a>
            </li>
            <li class="header_item">
              <a href="/pz" class="header_link">Пациенты на запись</a>
            </li>
            <li class="header_item">
              <a href="/spCard" class="header_link">Список карт</a>
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
      padding: 0; /* Убираем отступы у списка */
      list-style: none; /* Убираем маркеры списка */
      display: flex; /* Используем flexbox для горизонтального расположения */
  }
  
  .header_item {
      margin: 0 20px; /* Увеличиваем расстояние между элементами навигации */
  }
  
  .header_link {
      text-decoration: none; /* Убираем подчеркивание */
      color: #007BFF; /* Цвет текста ссылок */
      transition: color 0.3s; /* Плавный переход цвета */
  }
  
  .header_link:hover {
      color: #007BFF; /* Цвет при наведении */
  }
  </style>