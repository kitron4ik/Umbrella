<template>
    <div>
      <h1>{{ isEditMode ? 'Редактировать МедКарту' : 'Создать МедКарту' }}</h1>
  
      <form @submit.prevent="handleSubmit">
        <div>
          <label for="diagnosis">Диагноз</label>
          <textarea v-model="form.diagnosis" id="diagnosis" required></textarea>
        </div>
  
        <div>
          <label for="recommendations">Рекомендации</label>
          <textarea v-model="form.recommendations" id="recommendations"></textarea>
        </div>
  
        <button type="submit">{{ isEditMode ? 'Обновить' : 'Создать' }}</button>
      </form>
    </div>
  </template>
  
  <script>
  import { useMedCardStore } from '../stores/medcards';
  
  export default {
    props: {
      medcardId: {
        type: Number,
        required: false,
        default: null,
      },
    },
  
    data() {
      return {
        form: {
          diagnosis: '',
          recommendations: '',
        },
        isEditMode: false,
      };
    },
  
    setup() {
      const medCardStore = useMedCardStore();
      return { medCardStore };
    },
  
    created() {
      if (this.medcardId) {
        this.isEditMode = true;
        const medCard = this.medCardStore.medcards.find((med) => med.id === this.medcardId);
        if (medCard) {
          this.form.diagnosis = medCard.diagnosis;
          this.form.recommendations = medCard.recommendations;
        }
      }
    },
  
    methods: {
      async handleSubmit() {
        if (this.isEditMode) {
          await this.medCardStore.updateMedCard(this.medcardId, this.form);
        } else {
          await this.medCardStore.createMedCard(this.form);
        }
        this.$router.push('/dashboard'); // Перенаправить пользователя после сохранения
      },
    },
  };
  </script>
  