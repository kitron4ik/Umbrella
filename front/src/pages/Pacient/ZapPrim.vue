<template>
    <div>
      <header class="header">
          <div class="wrapper">
              <div class="header_wrapper">
                  <div class="header_logo">
                      <a href="/" class="header_logo_link">
                          <img src="../../assets/png/logo.png" alt="logo">
                      </a>
                  </div>
                  <nav class="header_nav">
                      <ul class="header_list">
                          <li class="header_item">
                              <a href="/pp" class="header_link">Мой профиль</a>
                          </li>
                          <li class="header_item">
                              <a href="/zp" class="header_link">Записаться на приём</a>
                          </li>
                          <li class="header_item">
                              <a href="/MyCard" class="header_link" id="openRegister">Моя карточка</a>
                          </li>
                      </ul>
                  </nav>
              </div>
          </div>
      </header>
  
      <!-- Form for selecting date and time -->
      <div class="appointment-form">
        <form @submit.prevent="submitForm">
          <label for="appointment-date">Выберите день:</label>
          <input type="date" id="appointment-date" v-model="appointmentDate" required>
  
          <label for="appointment-time">Выберите время:</label>
          <input type="time" id="appointment-time" v-model="appointmentTime" required>
  
          <button type="submit">Записаться</button>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        appointmentDate: '',
        appointmentTime: ''
      };
    },
    methods: {
      submitForm() {
        // Submit form logic
        console.log('Дата:', this.appointmentDate);
        console.log('Время:', this.appointmentTime);
      }
    }
  }
  </script>
  
  <style scoped>
  /* margin: 30vh Вниз 30vh 30vh 30vh вправо; */
  .appointment-form {
    margin: 30vh 0vh 0vh 100vh;
    display:block;
  }
  label {
    display: block;
    margin: 10px 0 5px;
  }
  input {
    margin-bottom: 10px;
    padding: 5px;
  }
  button {
    padding: 10px 20px;
    background-color: #00d5ff;
    color: white;
    border: none;
    cursor: pointer;
  }
  button:hover {
    background-color: #1ea2df;
  }
  </style>
  