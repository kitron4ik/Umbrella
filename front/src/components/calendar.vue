<template>
  <section>
        <div class="form-group">
          <label>Select a date range</label>
          <div class="input-group">
            <flat-pickr
              v-model="dateRange"
              :config="config"
              class="form-control"
              placeholder="Select date range"
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
        <pre>Дата вашего отпуска: {{ dateRange }}</pre>
      </section>
</template>

<script>
import { ref } from 'vue';
import 'bootstrap/dist/css/bootstrap.css';
import flatPickr from 'vue-flatpickr-component';
import 'flatpickr/dist/flatpickr.css';
import 'flatpickr/dist/themes/material_blue.css';
import { Russian } from 'flatpickr/dist/l10n/ru.js';

export default {
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

    return {
      dateRange,
      config,
    };
  },
};
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