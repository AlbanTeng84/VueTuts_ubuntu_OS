<template>
    <div class="m-auto">
        <h1 class="text-2xl my-2 text-center">Vue Calendar</h1>
        <section class="mx-2 font-bold flex justify-between">
         <h2>{{currentMonthName}}</h2>
         <button @click="clickToday">Today</button>
         
         <h2>{{currentYear}}</h2>
         
        </section>
        <section class="flex my-2">
            <p class="text-center" style="width:14.28%" v-for="day in days" :key="day">{{day}}</p>
        </section>
        <section class="flex flex-wrap">
            <p class="text-center" style="width:14.28%" v-for="num in startDay()" :key="num"></p>
            <p class="text-center" style="width:14.28%" v-for="num in daysInMonth()" 
            :key="num" 
            :class="num === currentDate ? 'text-yellow-800' : ''">{{num}}</p>
        </section>
        <section class="flex justify-between my-4">
            <button class="px-2 border rounded" @click="pre">Pre</button>
            <button class="px-2 border rounded" @click="next">Next</button>
        </section>
    </div>
</template>

<script> 
export default {
    data(){
        return{
            currentDate: new Date().getUTCDate(),
            currentMonth: new Date().getMonth(),
            currentYear: new Date().getFullYear(),
            currentDays:"",
            days:['Sun','Mon','Tue','Wed','Thu','Fri','Sat'],
        }
    },
    methods:{
        daysInMonth(){
            return new Date(this.currentYear, this.currentMonth+1,0).getDate()
        },
        startDay(){
            return new Date(this.currentYear,this.currentMonth+3,1).getDay()
        },
        pre(){
            if(this.currentMonth === 0){
                this.currentMonth = 11;
                this.currentYear--;
            } else{

                this.currentMonth--
            }
        },
        next(){
            if(this.currentMonth === 11){
                this.currentMonth = 0;
                this.currentYear++;
            }else{

                this.currentMonth++;
            }
        },
        
    },
    computed:{
        currentMonthName(){
            return new Date(this.currentYear,this.currentMonth).toLocaleString("default",{month:'long'});
        }
    }
}
</script>

<style>

</style>