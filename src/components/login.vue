<template>
    <div class="modal" v-if="isVisible">
      <div class="modal-content">
        <span class="close" @click="closePopUp">&times;</span>
        
        <div v-if="isRegister">
          <h2>Регистрация</h2>
          <form @submit.prevent="handleSubmit">
            <input type="text" v-model="name" placeholder="ФИО" required>
            <input type="email" v-model="email" placeholder="Email" required>
            <input type="text" v-model="buildingCode" placeholder="Код здания" required>
            <input type="text" v-model="roleCode" placeholder="Код роли" required>
            <input type="text" v-model="role" placeholder="Роль" required>
            <input type="password" v-model="password" placeholder="Пароль" required>
            <button type="submit">Зарегистрироваться</button>
          </form>
        </div>
        
        <div v-else>
          <h2>Вход</h2>
          <form @submit.prevent="handleSubmit">
            <input type="email" v-model="email" placeholder="Email" required>
            <input type="password" v-model="password" placeholder="Пароль" required>
            <button type="submit">Войти</button>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      isVisible: Boolean,
      isRegister: Boolean
    },
    data() {
      return {
        name: '',
        email: '',
        buildingCode: '',
        roleCode: '',
        role: '',
        password: ''
      };
    },
    methods: {
      closePopUp() {
        this.$emit('close');
      },
      handleSubmit() {
        // Логика обработки формы
        this.closePopUp();
      }
    }
  };
  </script>
  
  <style scoped>
  /* Добавьте стили для pop-up */
  .modal {
    display: block;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 999;
  }
  
  .modal-content {
    background-color: #fff;
    margin: 15% auto;
    padding: 20px;
    border: 1px solid #888;
    width: 80%;
    max-width: 500px;
  }
  
  .close {
    float: right;
    font-size: 28px;
    font-weight: bold;
    cursor: pointer;
  }
  </style>
  