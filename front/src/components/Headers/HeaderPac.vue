<template>
    <header class="header">
      <div class="wrapper">
        <div class="header_wrapper">
          <div class="header_logo">
            <a href="/" class="header_logo_link">
              <img src="../../assets/png/logo.png" alt="logo" class="Logo">
            </a>
          </div>
          <nav class="header_nav">
            <ul class="header_list">
              <li class="header_item">
                <a href="/login" class="header_link">Мой профиль</a>
              </li>
              <li class="header_item">
                <a href="/zp" class="header_link">Записаться на приём</a>
              </li>
            </ul>
          </nav>
        </div>
      </div>
    </header>
  </template>
  
  <script>
  export default {
  }
  </script>
  
  <style>
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
      margin: 0 30px; /* Увеличиваем расстояние между элементами навигации */
  }
  
  .header_link {
      text-decoration: none; /* Убираем подчеркивание */
      color: #333; /* Цвет текста ссылок */
      transition: color 0.3s; /* Плавный переход цвета */
  }
  
  .header_link:hover {
      color: #007BFF; /* Цвет при наведении */
  }
  </style>