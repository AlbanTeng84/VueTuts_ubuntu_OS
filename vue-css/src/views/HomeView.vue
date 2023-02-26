<template>
  <h1>This is home page</h1>
  <test2 :title="title"/>
</template>

<script>
import test2 from '../components/test2.vue'

export default {
  name: 'HomeView',
  components: {test2},
  data(){
    return{
      title:{
        name:'Ping',
        company:'Zhao'
        }
    }
  }

}

</script>
