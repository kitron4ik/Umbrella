<template>
  <div class="doctor-page">
    <h1>Пациенты, записанные к вам</h1>
    <div v-if="patients.length > 0">
      <ul>
        <li v-for="patient in patients" :key="patient.appointment_id" class="patient-item">
          <span>
            {{ patient.patient_name }} 
            ({{ patient.appointment_date }} в {{ patient.appointment_time }})
          </span>
          <button @click="removeAppointment(patient.appointment_id)">Завершить запись</button>
          <button @click="viewPatientProfile(patient.patient_id)">Открыть профиль</button>
        </li>
      </ul>
    </div>
    <div v-else>
      <p>Нет записей на приём.</p>
    </div>
  </div>
</template>

<script>
import { useUserStore } from '@/stores/UserStore';
import axios from 'axios';

export default {
  data() {
    return {
      patients: [],
      doctorId: '',
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
