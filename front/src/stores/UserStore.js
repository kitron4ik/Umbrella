// stores/userStore.js
import { defineStore } from 'pinia';

export const useUserStore = defineStore('user', {
  state: () => ({
    regname: null,
    role: null,
    token: null,
    isLoggedIn: false,
  }),
  actions: {
    setUser(data) {
      this.regname = data.regname;
      this.role = data.role;
      this.token = data.token;
      this.isLoggedIn = true;
    },
    logout() {
      this.regname = null;
      this.role = null;
      this.token = null;
      this.isLoggedIn = false;
      localStorage.clear();
    },
  },
});
