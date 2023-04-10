<template>
  <Actions :btn1= btnAction />
</template>

<script>
import Actions from './components/Actions.vue'
export default {
  name: 'App',
  components: {
    Actions,
  },
  data(){
    return {
        btnAction:'Click Me'
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
