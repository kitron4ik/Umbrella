<template>
    <div class="patient-profile">
      <h1>Профиль пациента</h1>
      <p v-if="patientDetails">Имя пациента: {{ patientDetails.regname }}</p>
  
      <!-- История болезни -->
      <div v-if="patientDetails">
        <h2>История болезни</h2>
        <div v-if="medicalConditions && medicalConditions.length > 0">
          <ul>
            <li v-for="condition in medicalConditions" :key="condition.id">
              {{ condition.condition }} ({{ condition.date_added }})
            </li>
          </ul>
        </div>
        <div v-else>
          <p>История болезни отсутствует.</p>
        </div>
  
        <!-- Форма для добавления заболевания -->
        <h3>Добавить диагноз</h3>
        <textarea v-model="newCondition" placeholder="Введите диагноз пациента..." rows="4"></textarea>
        <button @click="saveCondition">Сохранить</button>
      </div>
    </div>
  </template>
  
  <script>
  import { useUserStore } from '@/stores/UserStore'; 
  import axios from 'axios'; 

  export default {
    data() {
      return {
        patientDetails: null,
        medicalConditions: [],
        newCondition: '',
      };
    },
    computed: {
      patientId() {
        const userStore = useUserStore();
        return userStore.patientId;  
      },
    },
    watch: {
      patientId(newPatientId) {
        if (newPatientId) {
          this.fetchPatientDetails(newPatientId);
          this.fetchMedicalConditions(newPatientId);
        }
      },
    },
    methods: {
      async fetchPatientDetails(patientId) {
        try {
          if (!this.isUserLoggedIn()) return; // Проверка авторизации
          const response = await axios.get(`/api/login/?id=${patientId}`);
          console.log(patientId);
          this.patientDetails = response.data;
          console.log(this.patientDetails);
        } catch (error) {
          console.error('Ошибка при загрузке данных пациента:', error);
        }
      },
      async fetchMedicalConditions(patientId) {
        try {
          if (!this.isUserLoggedIn()) return; // Проверка авторизации
          const response = await axios.get(`/api/medcard/medcard/conditions/${patientId}/`);
          this.medicalConditions = response.data;
        } catch (error) {
          console.error('Ошибка при загрузке истории болезни:', error);
        }
      },
      async saveCondition() {
        if (!this.newCondition.trim()) {
          alert('Пожалуйста, введите диагноз');
          return;
        }
  
        try {
          if (!this.isUserLoggedIn()) return; // Проверка авторизации
          const response = await axios.post('/api/medcard/medcard/save-condition/', {
            patientId: this.patientId,
            condition: this.newCondition,
          });
          alert('Диагноз успешно сохранен');
          this.newCondition = ''; 
          this.fetchMedicalConditions(this.patientId);  // Обновляем историю болезни
        } catch (error) {
          console.error('Ошибка при сохранении диагноза:', error);
          alert('Не удалось сохранить диагноз');
        }
      },
      isUserLoggedIn() {
        const userStore = useUserStore();
        if (!userStore.isLoggedIn) {
          this.$router.push('/'); // Перенаправление на главную страницу, если не авторизован
          return false;
        }
        return true;
      },
    },
    mounted() {
      const userStore = useUserStore();
      if (userStore.isLoggedIn && this.patientId) {
        this.fetchPatientDetails(this.patientId);
        this.fetchMedicalConditions(this.patientId);
      } else if (!userStore.isLoggedIn) {
        this.$router.push('/'); // Перенаправление на главную страницу, если не авторизован
      }
    },
  };
  </script>
  
  <style scoped>
.patient-profile {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: 'Arial', sans-serif;
}

h1 {
  font-size: 2.5em;
  text-align: center;
  margin-bottom: 20px;
  color: #333;
}

p {
  font-size: 1.2em;
  color: #555;
}

h2 {
  font-size: 2em;
  margin-top: 30px;
  color: #2a9d8f;
}

h3 {
  font-size: 1.8em;
  margin-top: 20px;
  color: #e76f51;
}

ul {
  list-style-type: none;
  padding-left: 0;
}

li {
  background-color: #f4f4f4;
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

li:hover {
  background-color: #e9e9e9;
}

textarea {
  width: 100%;
  padding: 10px;
  font-size: 1.2em;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-top: 10px;
  resize: vertical;
}

button {
  display: inline-block;
  margin-top: 10px;
  padding: 12px 20px;
  font-size: 1.1em;
  background-color: #2a9d8f;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #21867a;
}

button:active {
  background-color: #1a6b65;
}

p {
  font-size: 1.1em;
  color: #666;
  text-align: center;
}

textarea::placeholder {
  font-style: italic;
  color: #aaa;
}
</style>
