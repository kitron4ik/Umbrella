import { defineStore } from 'pinia';
import axios from 'axios';
import { useUserStore } from './UserStore'; // Импортируем UserStore

export const useMedCardStore = defineStore('medcard', {
  state: () => ({
    medcards: [],
  }),

  getters: {
    getMedCards: (state) => state.medcards,
  },

  actions: {
    async fetchMedCards() {
      try {
        const userStore = useUserStore(); // Получаем доступ к UserStore
        const accessToken = userStore.getToken; // Получаем токен из UserStore

        const response = await axios.get('/api/medcard/medcards/', {
          headers: {
            'Authorization': `Bearer ${accessToken}` // Передаем токен в заголовке
          }
        });

        this.medcards = response.data;
      } catch (error) {
        console.error('Ошибка при загрузке медкарт:', error);
      }
    },

    async createMedCard(payload) {
      try {
        const userStore = useUserStore(); // Получаем доступ к UserStore
        const accessToken = userStore.getToken; // Получаем токен из UserStore

        const response = await axios.post('/api/medcard/medcards/', payload, {
          headers: {
            'Authorization': `Bearer ${accessToken}` // Передаем токен в заголовке
          }
        });

        this.medcards.push(response.data);
      } catch (error) {
        console.error('Ошибка при создании медкарты:', error);
      }
    },

    async updateMedCard(id, payload) {
      try {
        const userStore = useUserStore(); // Получаем доступ к UserStore
        const accessToken = userStore.getToken; // Получаем токен из UserStore

        const response = await axios.put(`/api/medcard/medcards/${id}/`, payload, {
          headers: {
            'Authorization': `Bearer ${accessToken}` // Передаем токен в заголовке
          }
        });

        const index = this.medcards.findIndex((medcard) => medcard.id === id);
        if (index !== -1) {
          this.medcards[index] = response.data;
        }
      } catch (error) {
        console.error('Ошибка при обновлении медкарты:', error);
      }
    },

    async deleteMedCard(id) {
      try {
        const userStore = useUserStore(); // Получаем доступ к UserStore
        const accessToken = userStore.getToken; // Получаем токен из UserStore

        await axios.delete(`/api/medcard/medcards/${id}/`, {
          headers: {
            'Authorization': `Bearer ${accessToken}` // Передаем токен в заголовке
          }
        });

        this.medcards = this.medcards.filter((medcard) => medcard.id !== id);
      } catch (error) {
        console.error('Ошибка при удалении медкарты:', error);
      }
    },
  },
});
