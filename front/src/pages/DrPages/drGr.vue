<template>
  <div>
    <div class="calendar-container">
      <HeaderDoc />
      <Calendar />
    </div>
    
  </div>
    
  </template>
  
  <script>
  import HeaderDoc from '@/components/Headers/HeaderDoc.vue';
  import Calendar from '@/components/calendar.vue';

  
  export default ({
    components: {
      HeaderDoc,
      Calendar,
    },
    
  })
  </script>
  
  <style scoped>
  .saveCallendar {
  display: flex;
  border: 1px solid #00C9AD;
  background: rgb(255, 255, 255);
  font-family: 'Montserrat', light;
  border-radius: 10px;
}
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
  