<template>
  <AppHeader />
  <div class="w-full flex">
    <!-- <GetRandomNum /> -->
    <Calendar />
      
  </div>
  
</template>

<script>
import GetRandomNum from './components/GetRandomNum.vue'
import AppHeader from './components/AppHeader.vue'
import Calendar from './components/Calendar.vue'

export default {
  name: 'App',
  components: {
    GetRandomNum,
    AppHeader,
    Calendar,
  }

}
</script>

<style>

</style>
