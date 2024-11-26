<template>
  <div>
    <component :is="headerComponent"></component>

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
import axios from 'axios';
import { useUserStore } from '@/stores/UserStore';
import { computed } from 'vue';
import HeaderPac from '@/components/Headers/HeaderPac.vue';

export default {
  data() {
    return {
      appointmentDate: '',
      appointmentTime: '',
      HeaderPac,
    };
  },
  setup() {
    const userStore = useUserStore();
    
    // Используем computed для получения userId
    const userId = computed(() => userStore.userId);
    
    return {
      userId,
    };
  },
  methods: {
    async submitForm() {
      if (!this.appointmentDate || !this.appointmentTime) {
        alert('Пожалуйста, выберите дату и время.');
        return;
      }

      console.log('userId:', this.userId); // Отладочная информация

      const payload = {
        date: this.appointmentDate,
        time: this.appointmentTime,
        reg_id: this.userId, // Используем id пользователя в payload
      };

      console.log('Stored userId:', localStorage.getItem('userId')); // Проверка localStorage

      try {
        const response = await axios.post('/api/appointments/', payload, {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`,
            'Content-Type': 'application/json',
          },
        });

        if (response.status === 200) {
          alert('Запись успешно создана!');
          this.appointmentDate = '';
          this.appointmentTime = '';
        }
      } catch (error) {
        console.error('Ошибка при записи:', error);
        console.log(payload);
        alert('Не удалось создать запись. Попробуйте снова.');
      }
    }
  },
  computed: {
    headerComponent() {
      return HeaderPac;
    }
  }
}
</script>

<style scoped>
.appointment-form {
  margin: 30vh 0vh 0vh 100vh;
  display: block;
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