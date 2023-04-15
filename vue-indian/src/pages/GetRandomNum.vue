<template>
<div class="w-full flex">
    <div class="m-auto">
        <h1 class="text-2xl text-center">ranList {{itemCount}}</h1>
        <ul>
            <li class="flex justify-between" v-for="(value,index) in ranList" :key="value.name">
            <div>
            {{value.id}} {{value.name}} {{index}}
            </div>
            <button class="text-2xl text-red-600" @click="removeItem(index)">x</button>
            </li> 
        </ul>

        <form class="mt-10" @submit.prevent="addHandle">   
            <input  class="border rounded"
            placeholder="type new item" v-model="newItem">
            <button class="border rounded bg-gradient-to-r from-red-700 to-pink-400 text-white">Add Item</button>
        </form>  
    </div>
</div>
</template>

<script>
export default {
    name:'GetRandomNum',
    data(){
        return{
            msg:"开始抽奖",
            ranNum:" ",
            ranList:[
                {"id":1,"name":'下次再来'},
                {"id":2,"name":'恭喜你中100万'},
                {"id":3,"name":'迪斯尼门票一张'},
                 
                 ],

            isShowing:true,
            randI:" ",
            isActive:false,
            newItem:'',

        }
    },
    computed:{
        itemCount(){
            return this.ranList.length
        }
    },
    methods:{
        addHandle(){
                if (this.newItem !== ''){

                    this.ranList.push({name:this.newItem});
                    this.newItem = '';
                }
        
        },
        randM(){
            return Math.floor(Math.random()*1000)
        },
        removeItem(index){
            this.ranList = this.ranList.filter((a, i) => i !== index)
    
        },

    }
}
</script>

<style scoped>
    .wraper{
        width:80%;
        margin: 0 auto;
    }
</style>