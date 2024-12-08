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
    <div v-if="showModal" class="modal">
      <div class="modal-content">
        <h2>Запись к доктору: {{ selectedDoctor.regname }}</h2>
        
        <div v-if="step === 1" class="calendar">
          <div class="calendar-header">
            <button @click="prevMonth">←</button>
            <div class="month-year">
              <div class="month">{{ currentMonthName }}</div>
              <div class="year">{{ currentYear }}</div>
            </div>
            <button @click="nextMonth">→</button>
          </div>
          <div class="calendar-grid">
            <div class="day-name" v-for="day in daysOfWeek" :key="day">{{ day }}</div>
            <div class="day" 
              v-for="day in daysInMonth" 
              :key="day.date" 
              :class="{ 'today': day.isToday, 'disabled': day.isDisabled, 'selected': day.isSelected }"
              @click="selectDate(day)">
              {{ day.day }}
            </div>
          </div>
          <button v-if="appointment.date" @click="goToNextStep">Далее</button>
        </div>

        <div v-if="step === 2" class="time-grid">
          <div 
            v-for="time in availableTimes" 
            :key="time" 
            class="time-block" 
            :class="{ selected: time === appointment.time }" 
            @click="selectTime(time)"
          >
            {{ time }}
          </div>
          <button v-if="appointment.time" @click="submitAppointment">Записаться</button>
          <button @click="goBackToStep1">Назад</button>
        </div>

        <button type="button" @click="closeModal">Отмена</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { useAppointmentStore } from "@/stores/AppointmentStore";
import { useUserStore } from "@/stores/UserStore"; // Импортируем Pinia UserStore

export default {
  data() {
    return {
      userId: null, // id пользователя
      doctors: [],
      showModal: false,
      selectedDoctor: null,
      appointment: {
        date: "",
        time: "",
        patient: null, // Сюда будет записан id пациента
        doctor: null,
      },
      step: 1, // Текущий шаг (1 - выбор даты, 2 - выбор времени)
      currentMonth: new Date().getMonth(),
      currentYear: new Date().getFullYear(),
      daysOfWeek: ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'],
      availableTimes: this.generateTimeSlots(), 
    };
  },
  computed: {
    currentMonthName() {
      const monthNames = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 
                          'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'];
      return monthNames[this.currentMonth];
    },
    daysInMonth() {
      const days = [];
      const firstDay = new Date(this.currentYear, this.currentMonth, 1).getDay();
      const daysInCurrentMonth = new Date(this.currentYear, this.currentMonth + 1, 0).getDate();
      const shift = firstDay === 0 ? 6 : firstDay - 1;

      for (let i = 0; i < shift; i++) {
        days.push({ day: '', isDisabled: true });
      }

      for (let i = 1; i <= daysInCurrentMonth; i++) {
        const date = new Date(this.currentYear, this.currentMonth, i);
        days.push({ day: i, date: this.formatDate(date) });
      }
      return days;
    },
  },
  methods: {
    formatDate(date) {
      const year = date.getFullYear();
      const month = (date.getMonth() + 1).toString().padStart(2, '0');
      const day = date.getDate().toString().padStart(2, '0');
      return `${year}-${month}-${day}`;
    },
    generateTimeSlots() {
      const times = [];
      for (let hour = 9; hour < 18; hour++) {
        for (let minute of [0, 15, 30, 45]) {
          times.push(`${hour.toString().padStart(2, '0')}:${minute.toString().padStart(2, '0')}`);
        }
      }
      return times;
    },
    async fetchDoctors() {
      try {
        const response = await axios.get("/api/appoint/doctors/");
        this.doctors = response.data;
      } catch (error) {
        console.error("Ошибка при загрузке списка докторов:", error);
      }
    },
    openModal(doctor) {
      this.selectedDoctor = doctor;
      this.appointment.doctor = doctor.id;
      this.showModal = true;
    },
    closeModal() {
      this.showModal = false;
      this.selectedDoctor = null;
    },
    async submitAppointment() {
      try {
        this.appointment.patient = this.userId; // Устанавливаем id текущего пациента
        const response = await axios.post("/api/appoint/appointments/", this.appointment);
        alert("Запись успешно создана!");
        this.closeModal();
      } catch (error) {
        console.error("Ошибка при создании записи:", error);
      }
    },
    selectDate(day) {
      if (!day.isDisabled) {
        this.appointment.date = day.date;
      }
    },
    selectTime(time) {
      this.appointment.time = time;
    },
    goToNextStep() {
      if (this.appointment.date) this.step = 2;
    },
    goBackToStep1() {
      this.step = 1;
    }
  },
  mounted() {
    const userStore = useUserStore();
    this.userId = localStorage.getItem('userId') || userStore.userId;
    if (!this.userId) {
      alert("Пользователь не авторизован");
      window.location.href = '/admin';
    }
    this.fetchDoctors();
  },
};
</script>


<style scoped>
.calendar .day.disabled {
  color: #a0a0a0; /* Серый цвет */
  cursor: not-allowed; /* Запрещённый курсор */
  pointer-events: none; /* Полностью блокируем события клика */
}

.day.selected {
  background: #4caf50;
  color: white;
}

.time-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 10px;
  margin-top: 20px;
}

.time-block {
  background: #f4f4f9;
  padding: 10px;
  border-radius: 5px;
  text-align: center;
  cursor: pointer;
  transition: background 0.3s;
}

.time-block:hover {
  background: #d1e8ff;
}

.time-block.selected {
  background: #4caf50;
  color: white;
}
.modal {
  position: fixed;
  top: 0; left: 0; width: 100%; height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex; justify-content: center; align-items: center;
}

.modal-content {
  background: #fff;
  padding: 20px;
  border-radius: 10px;
  width: 500px;
}

.calendar {
  display: flex;
  flex-direction: column;
}

.calendar-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.month-year {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.month, .year {
  font-size: 20px;
  font-weight: bold;
}

.calendar-grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 5px;
}

.day-name {
  font-weight: bold;
  text-align: center;
}

.day {
  background: #f4f4f9;
  border-radius: 5px;
  text-align: center;
  padding: 10px;
  cursor: pointer;
}

.day:hover {
  background: #d1e8ff;
}

.day.today {
  background: #f0a500;
  color: white;
}

.day.disabled {
  background: #e0e0e0;
  pointer-events: none;
}

.day:not(.disabled):hover {
  background: #8eb4f2;
}
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
  margin-bottom: 10px;
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
