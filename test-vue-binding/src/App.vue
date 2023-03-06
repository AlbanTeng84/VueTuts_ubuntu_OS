<template>
  <img alt="Vue logo" src="https://picsum.photos/200/300">
  <HelloWorld msg="Welcome to Your Vue.js App"/>
  <a :href="URL">Labrary</a>
  <Emit @customer-change="handleCustomChange"/>
  <p>Uppercase: {{ uppercase }}</p>
</template>

<script>

import Emit from "./components/Emit.vue"
export default {
  name: 'App',
  components: {Emit
  },
  data(){
    return{
      URL:"https://picsum.photos/200/300",
      uppercase: ''

    }
  },
  methods: {
    handleCustomChange (s) {
      this.uppercase = s
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
