<script>
import Headers from '@/components/Headers/Headers.vue';
import intro from '@/components/Glavnaya/intro.vue';
import twoutro from '@/components/Glavnaya/twoutro.vue';
import triutro from '@/components/Glavnaya/triutro.vue';

  export default {
  components: {Headers, intro, twoutro, triutro},
}
</script>


<template>
  <div>
    <headers />
    <intro />
    <twoutro/>
    <triutro/>
  </div>
</template>

<style scoped>

</style>
