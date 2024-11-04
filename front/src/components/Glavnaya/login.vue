<template>
  <div class="modal" v-if="isVisible">
    <div class="modal-content">
      <span class="close" @click="closePopUp">&times;</span>

      <div v-if="isRegister" class="PopReg">
        <h2>Регистрация</h2>
        <form @submit.prevent="login" method="POST">
          <input type="text" class="group" v-model="regname" placeholder="ФИО" required />
          <input type="email" class="group" v-model="email" placeholder="Email" required />
          <input
            type="text"
            class="group"
            v-model="building_Code"
            placeholder="Код здания"
            required
            @input="checkBuildingCode"
          />
          <input
            type="text"
            class="group"
            v-model="role_Code"
            placeholder="Код роли"
            :disabled="!canEnterRoleCode"
            @input="setRole"
          />
          <input
            type="text"
            class="group"
            v-model="role"
            placeholder="Роль"
            required
            readonly
          />
          <input type="password" class="group" v-model="password" placeholder="Пароль" required />
          <button type="submit" class="button-48"><span class="text">Зарегистрироваться</span></button>
        </form>
      </div>

      <div v-else class="PopLog">
        <h2>Вход</h2>
        <form @submit.prevent="login">
          <input type="email" class="group" v-model="email" placeholder="Email" required />
          <input type="password" class="group" v-model="password" placeholder="Пароль" required />
          <button type="submit" class="button-48"><span class="text">Войти</span></button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { defineComponent } from 'vue';

axios.defaults.baseURL = 'http://localhost:8000';

export default defineComponent({
  props: {
    isVisible: {
      type: Boolean,
      default: false,
    },
    isRegister: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      regname: '',
      email: '',
      building_Code: '',
      role_Code: '',
      role: '',
      password: '',
      canEnterRoleCode: false, // Флаг для активации поля role_Code
    };
  },
  methods: {
    // Метод для проверки кода здания
    checkBuildingCode() {
      // Активируем поле role_Code только если building_Code равен "001"
      this.canEnterRoleCode = this.building_Code === '001';
      if (!this.canEnterRoleCode) {
        this.role_Code = ''; // Очистка role_Code если building_Code неверный
        this.role = ''; // Очистка роли, если код здания неверный
      }
    },
    // Метод для установки роли на основе кода роли
    setRole() {
      if (this.role_Code === '001') {
        this.role = 'пациент';
      } else if (this.role_Code === '002') {
        this.role = 'доктор';
      } else {
        this.role = ''; // Очистка роли, если введен неверный код
      }
    },
    // Метод для отправки данных формы на сервер
    async login() {
      try {
        // Создаем объект с данными для отправки
        const payload = {
          regname: this.regname,
          email: this.email,
          building_code: this.building_Code,
          role_code: this.role_Code,
          role: this.role,
          password: this.password,
        };
        console.log('Отправляемый payload:', payload);

        // Отправляем POST-запрос на сервер
        const response = await axios.post('api/login/', payload, {
          headers: {
            'Content-Type': 'application/json',
          },
        });

        // Логируем ответ от сервера
        console.log(response.data);

        // Закрываем всплывающее окно после успешной отправки
        this.closePopUp();

        // Перенаправление пользователя в зависимости от его роли
        if (this.role === 'пациент') {
          this.$router.push('/pp');
        } else if (this.role === 'доктор') {
          this.$router.push('/dp');
        }
      } catch (error) {
        // Обрабатываем ошибки при отправке данных
        console.error('Ошибка при отправке данных:', error);
      }
    },
    async login() {
      try {
        const payload = {
          email: this.email,
          password: this.password,
        };

        // Отправка данных для входа
        const response = await axios.post('/api/log/', payload, {
          headers: {
            'Content-Type': 'application/json',
          },
        });

        console.log('Ответ от сервера:', response.data);
        this.closePopUp();

        // Перенаправление пользователя в зависимости от роли
        if (response.data.role === 'пациент') {
          this.$router.push('/pp');
        } else if (response.data.role === 'доктор') {
          this.$router.push('/dp');
        }
      } catch (error) {
        console.error('Ошибка при входе:', error);
      }
    },
    // Метод для закрытия всплывающего окна
    closePopUp() {
      this.$emit('close');
    },
  },
});
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