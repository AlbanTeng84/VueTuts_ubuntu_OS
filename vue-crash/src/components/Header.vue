<template>
  <h1>{{ title }}</h1>
  <Button 
  @btn-click="$emit('toggle-add-task')" :text="showAddTask ? 'Close' : 'Add Task'" 
  :color="showAddTask ? 'red' : 'green'"/>
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
        title:String,
        showAddTask:Boolean
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