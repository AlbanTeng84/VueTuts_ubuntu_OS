<template>

    <div>
    </div>
      
        <input class="num" type="text" placeholder="Number" size="2" v-model="n1">
        <input class="num" type="text" placeholder="Number" size="2" v-model="n2"> <br><br>
        <button @click="handlesum">Sum click</button>
        <h3 >{{n1}} + {{n2}} = {{sum}}</h3>
    <div>

    </div>  
</template>

<script>

export default {
  name: 'App',
  components: {
  
  },
  data(){
    return{
      n1:'',
      n2:'',
      sum:'',

    }
  },
 
  methods:{
    handlesum(){
        this.sum = parseFloat(this.n1) + parseFloat(this.n2)
     }
  },

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
.num{
  margin:10px;
}


</style>

