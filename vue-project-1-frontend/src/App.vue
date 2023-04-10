<template>
  <VModel :toVModel=msg />

</template>

<script>
import VModel from './VModel.vue'
export default {
  name: 'App',
  components: {
    VModel
  },
  data(){
    return {
      msg:'to VModel page!'
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
