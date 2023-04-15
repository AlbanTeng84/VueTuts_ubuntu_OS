<template>
     <div class="flex flex-wrap w-full">
       <div class="w-full" v-for="(color,index) in sliders" :key="color">

         
            <div 
                v-if="currentSlide == index" 
                :class="color" 
                style="height:350px"></div>
            
        

        
        </div>
    <div class="my-10 flex w-full">
                <div class="m-auto">
                    <h1 v-if="isToggle">Slider Carousel</h1>
                    <button class="px-2 roudned border" @click="hideToggle">Toggle Text</button>
                </div>
            </div>
    </div>
</template>


<script>
export default {
    data(){
        return{
            currentSlide: 1,
            sliders:['bg-teal-600','bg-blue-600','bg-yellow-600'],
            interval:"",
            isToggle:true,
        }
    },
    mounted(){
        this.interval = setInterval(() => {
            this.currentSlide = this.currentSlide === 2 ? 0 : this.currentSlide++
            
        },2000)
    },
    beforeUnmount(){
        clearInterval(this.interval)
    },
    methods:{
        hideToggle(){
            this.isToggle = !this.isToggle
        }
    },

}
</script>

<style>
    .fade-enter-active,
    .fade-leave-active{
        transition: all 1s ease;
    }

    .fade-enter-from,
    .fade-leave-to {
        opacity: 0;
        transform:translate(30px)
    }
</style>
