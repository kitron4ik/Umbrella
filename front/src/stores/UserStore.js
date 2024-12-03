// stores/UserStore.js
import { defineStore } from 'pinia';

export const useUserStore = defineStore('user', {
  state: () => ({
    userId: null, // id пользователя
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
    clearUser() {
      this.regname = '';
      this.role = '';
      this.token = '';
      this.userId = null; // Очищаем id пользователя
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
    // Геттер для получения id пользователя
    getUserId: (state) => state.userId,
  },
});


