import { defineStore } from 'pinia';
import axios from 'axios';

export const useUserStore = defineStore('user', {
  state: () => ({
    regname: '',
    email: '',
    role_code: '',
    role: '',
    building_code: '',
    password: '',
    token: localStorage.getItem('token') || null,
    isAuthenticated: !!localStorage.getItem('token'), // true, если есть токен
  }),
  actions: {
    setUserData(userData) {
      this.regname = userData.regname;
      this.email = userData.email;
      this.role_code = userData.role_code;
      this.role = userData.role;
      this.building_code = userData.building_code;
      this.password = userData.password;
      this.token = userData.token;
      this.isAuthenticated = true; // Помечаем пользователя как авторизованного

      // Сохраняем токен и данные в localStorage
      localStorage.setItem('token', userData.token);
    },
    clearUserData() {
      this.regname = '';
      this.email = '';
      this.role_code = '';
      this.role = '';
      this.building_code = '';
      this.password = '';
      this.token = null;
      this.isAuthenticated = false; // Помечаем пользователя как не авторизованного

      // Удаляем данные из localStorage
      localStorage.removeItem('token');
    },
    async login(payload) {
      try {
        const response = await axios.post('http://localhost:8000/api/login/', payload, {
          headers: {
            'Content-Type': 'application/json',
          },
        });

        // Сохранение данных пользователя и токена в хранилище
        this.setUserData({
          ...response.data.userData,
          token: response.data.token,
        });

        return response.data;
      } catch (error) {
        console.error('Ошибка при входе:', error);
        throw error;
      }
    },
    async register(payload) {
      try {
        const response = await axios.post('http://localhost:8000/api/register/', payload, {
          headers: {
            'Content-Type': 'application/json',
          },
        });

        // Сохранение данных пользователя и токена в хранилище
        this.setUserData({
          ...response.data.userData,
          token: response.data.token,
        });

        return response.data;
      } catch (error) {
        console.error('Ошибка при регистрации:', error);
        throw error;
      }
    },
  },
});
