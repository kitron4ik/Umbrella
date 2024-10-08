<template>
  <div class="modal" v-if="isVisible">
    <div class="modal-content">
      <span class="close" @click="closePopUp">&times;</span>

      <div v-if="isRegister" class="PopReg">
        <h2>Регистрация</h2>
        <form @submit.prevent="handleSubmit">
          <input type="text" class="group" v-model="name" placeholder="ФИО" required />
          <input type="email" class="group" v-model="email" placeholder="Email" required />
          <input type="text" class="group" v-model="buildingCode" placeholder="Код здания" required />
          <input type="text" class="group" v-model="roleCode" placeholder="Код роли" required />
          <input type="text" class="group" v-model="role" placeholder="Роль" required />
          <input type="password" class="group" v-model="password" placeholder="Пароль" required />
          <button type="submit" class="button-48" role="button"><span class="text">Зарегистрироваться</span></button>
        </form>
      </div>

      <div v-else class="PopLog">
        <h2>Вход</h2>
        <form @submit.prevent="handleSubmit">
          <input type="email" class="group" v-model="email" placeholder="Email" required />
          <input type="password" class="group" v-model="password" placeholder="Пароль" required />
          <button type="submit" class="button-48"><span class="text">Войти</span></button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    isVisible: Boolean,
    isRegister: Boolean,
  },
  data() {
    return {
      name: '',
      email: '',
      buildingCode: '',
      roleCode: '',
      role: '',
      password: '',
    };
  },
  methods: {
    closePopUp() {
      this.$emit('close');
    },
    handleSubmit() {
      // Логика обработки формы
      this.closePopUp();
    },
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;500;700&display=swap');

.modal {
  display: flex;
  position: fixed;
  z-index: 1000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.6);
  justify-content: center;
  align-items: center;
}

.modal-content {
  background-color: #f9f9f9;
  padding: 20px;
  border-radius: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  max-width: 400px;
  width: 90%;
  position: relative;
  text-align: center;
}

.close {
  position: absolute;
  top: 10px;
  right: 15px;
  font-size: 24px;
  font-weight: bold;
  color: #333;
  cursor: pointer;
}

h2 {
  font-family: 'Montserrat', sans-serif;
  font-weight: 500;
  margin-bottom: 20px;
}

.group {
  width: 100%;
  margin: 10px 0;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
}

.button-48 {
  display: inline-block;
  padding: 10px 20px;
  background-color: #00f7ff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-family: 'Montserrat', sans-serif;
  font-weight: 500;
  transition: background-color 0.3s ease;
}

.button-48:hover {
  background-color: #00adb3;
}

.PopReg,
.PopLog {
  font-family: 'Montserrat', sans-serif;
}

button span.text {
  font-size: 16px;
}

@media (max-width: 768px) {
  .modal-content {
    width: 95%;
  }
}
</style>
