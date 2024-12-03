<template>
  <div class="doctor-list">
    <h1>Список докторов</h1>
    <ul>
      <li v-for="doctor in doctors" :key="doctor.id">
        <button @click="openModal(doctor)">
          {{ doctor.regname }}
        </button>
      </li>
    </ul>

    <!-- Модальное окно для записи -->
    <div v-if="showModal" class="modal">
      <div class="modal-content">
        <h2>Запись к доктору: {{ selectedDoctor.regname }}</h2>
        <form @submit.prevent="submitAppointment">
          <label for="date">Дата:</label>
          <input type="date" v-model="appointment.date" required />

          <label for="time">Время:</label>
          <input type="time" v-model="appointment.time" required />

          <button type="submit">Записаться</button>
          <button type="button" @click="closeModal">Отмена</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { useAppointmentStore } from "@/stores/AppointmentStore"; // Импорт хранилища

export default {
  data() {
    return {
      doctors: [], // Список докторов
      showModal: false, // Показ модального окна
      selectedDoctor: null, // Выбранный доктор
      appointment: {
        date: "",
        time: "",
        patient: 1, // ID текущего пациента (можно заменить на динамическое)
        doctor: null,
      },
    };
  },
  methods: {
    // Получение списка докторов
    async fetchDoctors() {
      try {
        const response = await axios.get("/api/appoint/doctors/");
        this.doctors = response.data;
      } catch (error) {
        console.error("Ошибка при загрузке списка докторов:", error);
      }
    },
    // Открытие модального окна
    openModal(doctor) {
      this.selectedDoctor = doctor;
      this.appointment.doctor = doctor.id;
      this.showModal = true;
    },
    // Закрытие модального окна
    closeModal() {
      this.showModal = false;
      this.selectedDoctor = null;
      this.appointment.date = "";
      this.appointment.time = "";
    },
    // Отправка записи на сервер
    async submitAppointment() {
      try {
        const response = await axios.post("/api/appoint/appointments/", this.appointment);

        // Сохранение ID записи в Pinia
        const appointmentStore = useAppointmentStore();

// Сохраняем ID записи
        appointmentStore.setAppointmentId(response.data.appointment.id);

        // Получаем ID записи
        console.log('Appointment ID из Pinia:', appointmentStore.getAppointmentId);

        appointmentStore.setAppointmentId("id: ",response.data.appointment.id); // Предполагается, что API возвращает ID записи в ответе
        console.log(response.data.appointment.id)
        alert("Запись успешно создана!");
        this.closeModal();
      } catch (error) {
        console.error("Ошибка при создании записи:", error);
        alert("На данное время запись есть");
      }
    },
  },
  mounted() {
    this.fetchDoctors(); // Загрузка списка докторов при инициализации
  },
};
</script>


<style scoped>
.doctor-list {
  font-family: 'Arial', sans-serif;
  padding: 20px;
  background: linear-gradient(to bottom, #f0f7ff, #e0efff);
  border-radius: 10px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

h1 {
  font-size: 2rem;
  text-align: center;
  color: #333;
  margin-bottom: 20px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 15px;
}

button {
  background-color: #149c86;
  color: white;
  border: none;
  border-radius: 8px;
  padding: 12px 25px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.3s ease;
  width: 100%;
}

button:hover {
  background-color: #149c86;
  transform: translateY(-3px);
}

button:active {
  transform: translateY(1px);
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background: #ffffff;
  padding: 30px;
  border-radius: 10px;
  text-align: center;
  width: 100%;
  max-width: 500px;
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
  animation: modalIn 0.3s ease-in-out;
}

h2 {
  font-size: 1.5rem;
  margin-bottom: 20px;
  color: #333;
}

form {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

label {
  font-size: 1.1rem;
  color: #555;
  text-align: left;
}

input[type="date"],
input[type="time"] {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 1rem;
  width: 100%;
}

input[type="date"]:focus,
input[type="time"]:focus {
  border-color: #14ac92;
  outline: none;
}

button[type="submit"] {
  background-color: #16bea2;
  color: white;
  border: none;
  padding: 12px 20px;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

button[type="submit"]:hover {
  background-color: #16bea2;
}

button[type="submit"]:active {
  transform: translateY(1px);
}

button[type="button"] {
  background-color: #797979;
  color: white;
  border: none;
  padding: 12px 20px;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

button[type="button"]:hover {
  background-color: #797979;
}

button[type="button"]:active {
  transform: translateY(1px);
}

@keyframes modalIn {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}
</style>
