<template>
  <section>
    <div class="form-group">
      <label>Календарь Отпусков</label>
      <div class="input-group">
        <flat-pickr
          v-model="dateRange"
          :config="config"
          class="form-control"
          placeholder="Выберите промежуток отпуска"
          name="date"
          data-input
        />
        <div class="input-group-append">
          <button class="btn btn-default" type="button" title="Toggle" data-toggle>
            <i class="fa fa-calendar" />
            <span aria-hidden="true" class="sr-only">Выбор</span>
          </button>
          <button class="btn btn-default" type="button" title="Clear" data-clear>
            <i class="fa fa-times" />
            <span aria-hidden="true" class="sr-only">Очистить</span>
          </button>
        </div>
      </div>
    </div>
    <pre>Промедуток вашего отпуска: {{ dateRange }}</pre>
    <button @click="submitDateRange" class="btn btn-primary mt-3">Отправить</button>
  </section>
</template>


<script>
import { defineComponent, ref } from 'vue';
import 'bootstrap/dist/css/bootstrap.css';
import flatPickr from 'vue-flatpickr-component';
import 'flatpickr/dist/flatpickr.css';
import 'flatpickr/dist/themes/material_blue.css';
import { Russian } from 'flatpickr/dist/l10n/ru.js';
import axios from 'axios';

export default defineComponent({
  components: {
    flatPickr,
  },
  setup() {
    const dateRange = ref(null);
    const config = ref({
      wrap: true,
      altFormat: 'M j, Y H:i', // Формат даты и времени
      altInput: true,
      enableTime: true, // Включаем выбор времени
      dateFormat: 'Y-m-d H:i', // Формат хранения даты и времени
      locale: Russian, // Устанавливаем русскую локализацию
      mode: 'range', // Режим выбора диапазона дат
      time_24hr: true, // Используем 24-часовой формат времени
    });

    const submitDateRange = async () => {
      if (!dateRange.value || dateRange.value.length < 2) {
        alert("Пожалуйста, выберите полный диапазон дат.");
        return;
      }

      const [startDate, endDate] = dateRange.value;

      try {
        // Отправка данных на backend с использованием axios
        const response = await axios.post("http://127.0.0.1:8000/api/vacation/", {
          start_date: startDate,
          end_date: endDate,
        });

        console.log("Ответ от сервера:", response.data);
        alert("Даты успешно отправлены!");
      } catch (error) {
        console.error("Ошибка при отправке дат:", error);
        alert("Произошла ошибка при отправке данных.");
      }
    };

    return {
      dateRange,
      config,
      submitDateRange,
    };
  },
});
</script>

<style scoped>
.calendar-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.Calendar {
  display: flex;
  justify-content: center;
}
</style>