<template>
  <h1>{{ title }}</h1>
  <Button text="Add Task" color="green"/>
</template>

<script>
import Button from "./Button.vue"
export default {
    name:"Header",
    components:{Button},
    data(){
        return {
            msg:"this is Header"
        }
    },
    props:{
        title:String
    }
        
}
</script>

<style scoped>
header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
    }
</style>