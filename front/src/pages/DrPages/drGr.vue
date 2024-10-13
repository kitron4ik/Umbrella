<template>
    <div class="calendar-container">
      <HeaderDoc />
      <Calendar />
    </div>
  </template>
  
  <script>
  import HeaderDoc from '@/components/Headers/HeaderDoc.vue';
  import Calendar from '@/components/calendar.vue';

  
  export default {
    components: {
      HeaderDoc,
      Calendar,
    },
  }
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
  