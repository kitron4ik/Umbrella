// stores/UserStore.js
import { defineStore } from 'pinia';

export const useUserStore = defineStore('user', {
  state: () => ({
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
      this.isLoggedIn = true; // Установите флаг входа
    },
    clearUser() {
      this.regname = '';
      this.role = '';
      this.token = '';
      this.isLoggedIn = false; // Сбросьте флаг входа
    },
    logout() {
      this.clearUser(); // Очистите данные пользователя при выходе
      localStorage.removeItem('token');
      localStorage.removeItem('regname');
      localStorage.removeItem('role');
    },
  },
});