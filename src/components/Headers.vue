<script>
import login from './login.vue'

export default {
  components: {
    login
  },
  data() {
    return {
      isPopUpVisible: false,
      isRegister: false
    };
  },
  methods: {
    openRegister() {
      this.isRegister = true;
      this.isPopUpVisible = true;
    },
    openLogin() {
      this.isRegister = false;
      this.isPopUpVisible = true;
    },
    closePopUp() {
      this.isPopUpVisible = false;
    }
  }
};
</script>

<template>
    <header class="header">
      <div class="wrapper">
        <div class="header_wrapper">
          <div class="header_logo">
            <a href="/" class="header_logo_link">
              <img src="../assets/png/logo.png" alt="logo">
            </a>
          </div>
          <nav class="header_nav">
            <ul class="header_list">
              <li class="header_item">
                <a href="#" class="header_link">о нас</a>
              </li>
              <li class="header_item">
                <a href="#" class="header_link">функционал</a>
              </li>
              <li class="header_item">
                <button class="header_link" @click="openRegister">Регистрация</button>
              </li>
              <li class="header_item">
                <button class="header_link" @click="openLogin">Вход</button>
              </li>
            </ul>
          </nav>
        </div>
      </div>
  
      <!-- Компонент login, который отображает pop-up -->
      <login 
        v-if="isPopUpVisible" 
        :isVisible="isPopUpVisible" 
        :isRegister="isRegister" 
        @close="closePopUp"
      />
    </header>
</template>

<style scoped>

    button {
        font-family: 'Montserrat', light;
        border-radius: 5px 5px 5px 5px;
        border:0px;
        background: rgb(200, 247, 210);
    }
    button:hover {
        opacity:0.7;
        transform:scale(1.1);
        cursor: pointer;
    }
    button:active {
        opacity: 1;
        transform: scale(0.9);
    }
</style>

