// stores/UserStore.js
import { defineStore } from 'pinia';

export const useUserStore = defineStore('user', {
  state: () => ({
    userId: null, // id пользователя
    patientId: null, // Добавляем состояние для patient_id
    regname: '',
    role: '',
    token: '',
    isLoggedIn: false,
  }),
  actions: {
    setUser(user) {
      this.regname = user.regname;
      this.role = user.role;
      this.token = user.token;
      this.userId = user.userId; // Сохраняем id пользователя
      this.isLoggedIn = true; // Устанавливаем флаг входа
    },
    setPatientId(patientId) {
      this.patientId = patientId; // Сохраняем patient_id
    },
    clearUser() {
      this.regname = '';
      this.role = '';
      this.token = '';
      this.userId = null; // Очищаем id пользователя
      this.patientId = null; // Очищаем patient_id
      this.isLoggedIn = false; // Сбрасываем флаг входа
    },
    logout() {
      this.clearUser(); // Очистить данные пользователя при выходе
      localStorage.removeItem('token');
      localStorage.removeItem('regname');
      localStorage.removeItem('role');
      localStorage.removeItem('userId'); // Очищаем id из localStorage
    },
  },
  getters: {
    getUserId: (state) => state.userId,
    getPatientId: (state) => state.patientId, // Геттер для получения patient_id
  },
});
