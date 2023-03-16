<template>
  <form @submit.prevent="onSubmit">
    <label>Task</label><br>
    <input type="text" placeholder="Add Task" size="60" v-model="text"><br>{{text}}<br>
    
    <label>Day & Time</label><br>
    <input type="text" placeholder="Add Day & Time" size="60" v-model="day"><br>{{day}}<br>
    <label>Set Reminder&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</label>
    <input type="checkbox" v-model="reminder"><br>
    <input type="submit">
  </form>

</template>
 
<script>
export default {
    data(){
        return{
            text:'',
            day:'',
            reminder:false
        }
    },
    methods:{
        onSubmit(){
            if(!this.text){
                alert('Please add a task')
                return
            }
            const newTask = {
                // id: Math.floor(Math.random() * 100000),
                text: this.text,
                day: this.day,
                reminder: this.reminder,
            }
            
            this.$emit('add-task',newTask)

            this.text=''
            this.day=''
            this.reminder=false
        }
    }

}
</script>

<style>
  
</style>