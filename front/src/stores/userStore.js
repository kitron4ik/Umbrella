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
    inactivityTimeout:600000,
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
      this.lastActivity = Date.now();
      localStorage.setItem('token', userData.token);
      console.log("Данные пользователя установлены:", this.role, this.token);
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
      this.lastActivity = null;
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
