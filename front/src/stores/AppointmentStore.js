// stores/AppointmentStore.js
import { defineStore } from 'pinia';

export const useAppointmentStore = defineStore('appointment', {
  state: () => ({
    appointmentId: null, // ID последней созданной записи
  }),
  actions: {
    setAppointmentId(id) {
      this.appointmentId = id; // Сохраняем ID записи
    },
    clearAppointmentId() {
      this.appointmentId = null; // Очищаем ID
    },
  },
  getters: {
    getAppointmentId: (state) => state.appointmentId, // Геттер для получения ID
  },
});
