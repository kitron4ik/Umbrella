<template>
  <div class="container">
    <component :is="headerComponent"></component>
    <h1>МОЙ ПРОФИЛЬ</h1>
    <div class="card" v-if="isLoggedIn">
      <h2>Информация о {{ role }}е</h2>
      <p>{{ regname }}</p>
      <p class="desc">В данном поле будет отображаться то, чем вы были и какие лекарства вам выписал ваш доктор</p>
    </div>
    <div class="image-container">
      <img src="../assets/png/IntroShest/Bolshoi.png" alt="Bolshoi" class="fade-up__text-1000"/>
      <img src="../assets/png/IntroShest/srednii.png" alt="Srednii" class="fade-up__text-1100"/>
      <img src="../assets/png/IntroShest/Malenkii.png" alt="Malenkii" class="fade-up__text-1200"/>
      <img src="../assets/png/IntroShest/verhnii.png" alt="verhnii" class="fade-up__text-1300"/>
    </div>
  </div>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@100;700&display=swap');


.container {
  background: linear-gradient(135.00deg, rgba(31, 166, 219, 0.2),rgba(0, 0, 0, 0) 37.405%,rgba(0, 0, 0, 0) 69.975%,rgba(31, 181, 219, 0.2) 100%),rgba(255, 255, 255, 0);

  font-family: 'Montserrat', light;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  height: 100vh;
  padding-top: 100px;
  text-align: center; /* Центрирование текста */
  position: relative; /* Для корректного позиционирования дочерних элементов */
}

.card {
  background-color: #a4fff0;
  border: 1px solid #2fe08d;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 500px;
  height: 600px;
  margin: 20px 0;
  z-index: 1; /* Убедимся, что карточка выше остальных элементов */
}

h1 {
  font-size: 50px;
  color: rgb(31, 197, 219);
  border-bottom: 1px solid rgb(31, 197, 219);
}

h2, p {
  font-size: 25px;
  color:rgb(46, 99, 90);
}

.desc {
  padding-top: 50px;
  text-align: left;
}

.image-container {
  position: absolute; /* Изображения будут размещены абсолютно */
  top: 0;
  left: 0;
  right: 0;
  bottom: 0; /* Заполняем весь контейнер */
  pointer-events: none; /* Избежать взаимодействия с изображениями */
}

.image-container img {
  position: absolute; /* Абсолютное позиционирование для хаотичного размещения */
  opacity: 0.8; /* Полупрозрачные изображения */
  transition: transform 0.3s ease; /* Плавный переход для эффекта */
}

.image-container img:nth-child(1) {
  top: 15%; /* Положение первого изображения */
  left: 5%;
  transform: rotate(10deg);
}

.image-container img:nth-child(2) {
  top: 70%; /* Положение второго изображения */
  left: 5%;
  transform: rotate(-15deg);
}

.image-container img:nth-child(3) {
  top: 60%; /* Положение третьего изображения */
  left: 24%;
  transform: rotate(5deg);
}

.image-container img:nth-child(4) {
  top: 40%; /* Положение четвертого изображения */
  left: 70%;
  transform: rotate(-10deg);
}
</style>

<script>
import { useUserStore } from '@/stores/UserStore';
import { useRouter } from 'vue-router';
import HeaderPac from '../components/Headers/HeaderPac.vue';
import HeaderDoc from '../components/Headers/HeaderDoc.vue';

export default {
  components: {
    HeaderPac,
    HeaderDoc,
  },
  setup() {
    const userStore = useUserStore();
    const router = useRouter();

    if (localStorage.getItem('token')) {
      userStore.setUser({
        regname: localStorage.getItem('regname'),
        role: localStorage.getItem('role'),
        token: localStorage.getItem('token'),
      });
    }

    if (!userStore.isLoggedIn) {
      router.push('/');
    }

    return {
      regname: userStore.regname,
      role: userStore.role,
      isLoggedIn: userStore.isLoggedIn,
      email: '',
      password: '',
      logout: userStore.logout,
    };
  },
  computed: {
    headerComponent() {
      return this.role === 'пациент' ? 'HeaderPac' : 'HeaderDoc';
    },
  },
};
</script>