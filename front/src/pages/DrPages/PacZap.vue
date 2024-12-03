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
            <!-- Передаём appointment_id для удаления записи -->
            <button @click="removeAppointment(patient.appointment_id)">Завершить запись</button>
            <!-- Передаём patient_id для просмотра профиля пациента -->
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
import axios from 'axios';

export default {
    data() {
      return {
        patients: [], // Список пациентов
        doctorId: '', // ID доктора
      };
    },
    methods: {
      // Получение списка пациентов
      async fetchPatients() {
        this.doctorId = this.$route.params.id || localStorage.getItem('doctorId'); // ID доктора
        if (!this.doctorId) {
            alert('ID доктора отсутствует. Пожалуйста, войдите в систему.');
            return;
        }

        try {
            const response = await axios.get(`/api/appoint/appointments/${this.doctorId}/patients/`);
            this.patients = response.data; // Сохраняем список пациентов
            console.log(this.patients); // Проверяем структуру данных
        } catch (error) {
            console.error('Ошибка при загрузке пациентов:', error);
            alert('Не удалось загрузить список пациентов.');
        }
      },

      // Удаление записи
      async removeAppointment(appointmentId) {
        if (confirm("Вы уверены, что хотите удалить эту запись?")) { // Подтверждение удаления
            try {
                console.log("Удаляем запись с ID:", appointmentId); // Для отладки
                await axios.delete(`/api/appoint/appointments/${appointmentId}/remove/`);
                alert('Запись удалена!');
                this.fetchPatients(); // Обновляем список после удаления
            } catch (error) {
                console.error('Ошибка при удалении записи:', error);
                alert('Не удалось удалить запись');
            }
        }
      },

      // Переход на страницу профиля пациента
      viewPatientProfile(patientId) {
        this.$router.push(`/patient/${patientId}`);
      },
    },
  
    mounted() {
      this.fetchPatients(); // Загружаем список пациентов при загрузке компонента
    },
};
</script>
  