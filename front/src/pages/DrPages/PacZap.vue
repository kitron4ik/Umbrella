<template>
  <div class="doctor-page">
    <component :is="headerComponent"></component>
    <div class="page-content">
      <h1>Пациенты, записанные к вам</h1>
      <div v-if="patients.length > 0" class="patient-list">
        <ul>
          <li v-for="patient in patients" :key="patient.appointment_id" class="patient-item">
            <span class="patient-info">
              <strong>{{ patient.patient_name }}</strong> 
              ({{ patient.appointment_date }} в {{ patient.appointment_time }})
            </span>
            <div class="buttons">
              <button @click="removeAppointment(patient.appointment_id)" class="btn btn-danger">Завершить запись</button>
              <button @click="viewPatientProfile(patient.patient_id)" class="btn btn-primary">Открыть профиль</button>
            </div>
          </li>
        </ul>
      </div>
      <div v-else>
        <p>Нет записей на приём.</p>
      </div>
    </div>
  </div>
</template>

<script>
import { useUserStore } from '@/stores/UserStore';
import axios from 'axios';
import HeaderDoc from '../../components/Headers/HeaderDoc.vue'; // Импорт компонента для доктора

export default {
  data() {
    return {
      patients: [],
      doctorId: '',
      headerComponent: HeaderDoc, // Устанавливаем компонент заголовка для доктора
    };
  },
  methods: {
    async fetchPatients() {
      const userStore = useUserStore();
      if (!userStore.isLoggedIn) {
        this.$router.push('/'); // Перенаправление на главную страницу, если не авторизован
        return;
      }

      this.doctorId = this.$route.params.id || localStorage.getItem('doctorId');
      if (!this.doctorId) {
        alert('ID доктора отсутствует. Пожалуйста, войдите в систему.');
        return;
      }

      try {
        const response = await axios.get(`/api/appoint/appointments/${this.doctorId}/patients/`);
        this.patients = response.data;
        console.log(this.patients);
      } catch (error) {
        console.error('Ошибка при загрузке пациентов:', error);
        alert('Не удалось загрузить список пациентов.');
      }
    },

    async removeAppointment(appointmentId) {
      const userStore = useUserStore();
      if (!userStore.isLoggedIn) {
        this.$router.push('/'); // Перенаправление на главную страницу, если не авторизован
        return;
      }

      if (confirm("Вы уверены, что хотите удалить эту запись?")) {
        try {
          console.log("Удаляем запись с ID:", appointmentId);
          await axios.delete(`/api/appoint/appointments/${appointmentId}/remove/`);
          alert('Запись удалена!');
          this.fetchPatients();
        } catch (error) {
          console.error('Ошибка при удалении записи:', error);
          alert('Не удалось удалить запись');
        }
      }
    },

    viewPatientProfile(patientId) {
      const userStore = useUserStore();
      if (!userStore.isLoggedIn) {
        this.$router.push('/'); // Перенаправление на главную страницу, если не авторизован
        return;
      }

      userStore.setPatientId(patientId); // Сохраняем patient_id в Pinia
      this.$router.push(`/patient/${patientId}`);
    },
  },

  mounted() {
    this.fetchPatients();
  },
};
</script>

<style scoped>
.doctor-page {
  padding: 20px;
  background-color: #f4f7fb;
}

.page-content {
  margin-top:75px;
  background-color: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

h1 {
  font-size: 24px;
  color: #333;
  margin-bottom: 20px;
}

.patient-list {
  margin-top: 20px;
}

.patient-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #f9f9f9;
  padding: 15px;
  border-radius: 6px;
  margin-bottom: 15px;
  box-shadow: 0 1px 5px rgba(0, 0, 0, 0.1);
}

.patient-info {
  font-size: 16px;
  color: #555;
}

.buttons {
  display: flex;
  gap: 10px;
}

.btn {
  padding: 10px 15px;
  font-size: 14px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.btn-primary {
  background-color: #089274;
  color: white;
}

.btn-primary:hover {
  background-color: #015e59;
}

.btn-danger {
  background-color: #a3a3a3;
  color: white;
}

.btn-danger:hover {
  background-color: #4e4e4e;
}

@media (max-width: 768px) {
  .patient-item {
    flex-direction: column;
    align-items: flex-start;
  }

  .buttons {
    flex-direction: column;
    align-items: flex-start;
  }
}
</style>
