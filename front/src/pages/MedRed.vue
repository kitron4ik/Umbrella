<template>
    <div class="patient-profile">
      <component :is="headerComponent"></component>
      <div class="profile-container">
        <h1 class="profile-title">Профиль пациента</h1>
        <p v-if="patientDetails" class="patient-info">Имя пациента: {{ patientDetails.regname }}</p>
  
        <div class="profile-content">
          <!-- Область для сброса (слева) -->
          <div class="drop-area-container">
            <div
              class="drop-area"
              @dragover="onDragOver"
              @drop="onDrop"
            >
              <h3>Перетащите сюда диагнозы</h3>
              <ul>
                <li v-for="(condition, index) in droppedConditions" :key="index">
                  <input
                    v-model="droppedConditions[index].condition"
                    placeholder="Введите или отредактируйте диагноз"
                  />
                </li>
              </ul>
              <button @click="saveDroppedConditions">Сохранить</button>
            </div>
          </div>
  
          <!-- Блоки с перетаскиваемыми болезнями (справа) -->
          <div class="disease-blocks">
            <div
              class="disease-block"
              draggable="true"
              @dragstart="onDragStart($event, 'ОРВИ')"
              @dragend="onDragEnd"
            >
              ОРВИ
            </div>
            <div
              class="disease-block"
              draggable="true"
              @dragstart="onDragStart($event, 'Грипп')"
              @dragend="onDragEnd"
            >
              Грипп
            </div>
            <div
              class="disease-block"
              draggable="true"
              @dragstart="onDragStart($event, 'Диабет')"
              @dragend="onDragEnd"
            >
              Диабет
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { useUserStore } from '@/stores/UserStore';
  import axios from 'axios';
  import HeaderDoc from '../components/Headers/HeaderDoc.vue'; // Импорт компонента для доктора
  
  export default {
    data() {
      return {
        patientDetails: null,
        medicalConditions: [],
        draggedCondition: null, // Хранит перетаскиваемый диагноз
        droppedConditions: [], // Диагнозы, которые были сброшены
        headerComponent: HeaderDoc, // Устанавливаем компонент заголовка для доктора
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
          if (!this.isUserLoggedIn()) return;
          const response = await axios.get(`/api/login/?id=${patientId}`);
          this.patientDetails = response.data;
        } catch (error) {
          console.error('Ошибка при загрузке данных пациента:', error);
        }
      },
      async fetchMedicalConditions(patientId) {
        try {
          if (!this.isUserLoggedIn()) return;
          const response = await axios.get(`/api/medcard/medcard/conditions/${patientId}/`);
          this.medicalConditions = response.data;
        } catch (error) {
          console.error('Ошибка при загрузке истории болезни:', error);
        }
      },
      async saveDroppedConditions() {
        const conditions = this.droppedConditions.map(condition => ({
          condition: condition.condition,
          date_added: new Date().toISOString(),
        }));
  
        const data = {
          patientId: this.patientId,
          conditions,
        };
  
        console.log('Данные, отправляемые на сервер (saveDroppedConditions):', data);
  
        try {
          if (!this.isUserLoggedIn()) return;
          await axios.post('/api/medcard/medcard/save-condition/', data);
          alert('Диагнозы успешно сохранены');
          this.fetchMedicalConditions(this.patientId);
        } catch (error) {
          console.error('Ошибка при сохранении диагнозов:', error);
          alert('Не удалось сохранить диагнозы');
        }
      },
      isUserLoggedIn() {
        const userStore = useUserStore();
        if (!userStore.isLoggedIn) {
          this.$router.push('/');
          return false;
        }
        return true;
      },
      onDragStart(event, condition) {
        this.draggedCondition = condition;
        event.dataTransfer.effectAllowed = 'move';
        event.dataTransfer.setData('text/plain', condition);
        event.target.classList.add('dragging');
      },
      onDragOver(event) {
        event.preventDefault();
        event.dataTransfer.dropEffect = 'move';
      },
      onDrop(event) {
        event.preventDefault();
        const condition = event.dataTransfer.getData('text/plain');
        this.droppedConditions.push({ condition });
      },
      onDragEnd(event) {
        event.target.classList.remove('dragging');
      },
    },
    mounted() {
      const userStore = useUserStore();
      if (userStore.isLoggedIn && this.patientId) {
        this.fetchPatientDetails(this.patientId);
        this.fetchMedicalConditions(this.patientId);
      } else if (!userStore.isLoggedIn) {
        this.$router.push('/');
      }
    },
  };
  </script>
  
  <style scoped>
  .patient-profile {
    padding: 20px;
    text-align: center;
  }
  
  .profile-container {
    margin-top: 20px;
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  }
  
  .profile-title {
    font-size: 2rem;
    margin-bottom: 20px;
    color: #333;
  }
  
  .patient-info {
    font-size: 1.2rem;
    color: #666;
    margin-bottom: 20px;
  }
  
  .profile-content {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
  }
  
  .drop-area-container {

    flex: 1;
    margin-left: 250px;
  }
  
  .drop-area {
    width: 65%;
    min-height: 150px;
    height: 500px;
    border: 2px dashed #ccc;
    border-radius: 8px;
    padding: 20px;
    text-align: center;
    background-color: #f9f9f9;
  }
  
  .drop-area h3 {
    color: #666;
  }
  
  .drop-area ul {
    list-style: none;
    padding: 0;
  }
  
  .drop-area li {
    margin-bottom: 10px;
  }
  
  input {
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  button {
    padding: 10px 20px;
    background-color: #4caf50;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    margin-top: 10px;
  }
  
  button:hover {
    background-color: #45a049;
  }
  
  button:disabled {
    background-color: #ccc;
    cursor: not-allowed;
  }
  
  .disease-blocks {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }
  
  .disease-block {
    width: 100px;
    padding: 10px;
    background-color: #4caf50;
    color: #fff;
    text-align: center;
    border-radius: 4px;
    cursor: grab;
    margin-bottom: 10px;
  }
  
  .disease-block.dragging {
    opacity: 0.6;
  }
  </style>
  