<script>
import login from '../Glavnaya/login.vue'

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
              <img src="../../assets/png/logo.png" alt="logo" className="Logo">
            </a>
          </div>
          <nav class="header_nav">
            <ul class="header_list">
              <li class="header_item">
                <a href="#" class="header_link Onas">О НАС</a>
              </li>
              <li class="header_item">
                <a href="#" class="header_link funcc">ФУНКЦИОНАЛ</a>
              </li>
              <div className="authButton">
                <li class="header_item">
                <button class="header_link registerButton" @click="openRegister">РЕГИСТРАЦИЯ</button>
              </li>
              <li class="header_item">
                <button class="header_link loginButton" @click="openLogin">ВХОД</button>
              </li>
              </div>
              
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
.Logo {
    margin:0 auto;
    max-width: 75px;
    max-height: 75px;
}

.authButton {
  display: flex;
  margin-right: 150px;
  margin-top:18px;

}

.header_link.funcc {
  margin-top: 22px;
  position:absolute;
  right: 40%;
}

.header_link.Onas {
  position:absolute;
  right: 60%;
  margin-top: 22px;
}
.header {
  position: relative;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000; /* ставим высокое значение, чтобы панель оставалась выше остальных элементов */
  
}

.wrapper {
  padding-top: 30; /* добавьте отступ сверху, чтобы компенсировать высоту фиксированной панели */
}

.header_link.registerButton {
  margin: 0 auto;
  padding:5px;
  border: 1px solid #00C9AD;
  background: rgb(255, 255, 255);
  font-family: 'Montserrat', light;
  border-radius: 10px;
}
.header_link.loginButton {
  padding:5px;
  border: 1px solid #00C9AD;
  background: #00C9AD;
  font-family: 'Montserrat', light;
  border-radius: 10px;
  color: white;
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

