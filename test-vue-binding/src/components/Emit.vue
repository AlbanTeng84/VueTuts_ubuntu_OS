<template>
  <h1>{{ msg }}</h1>
  <input type="text" @input="handleChange">
</template>

<script>
export default {
    data(){
        return{
            msg:"this is Emit page"
        }
    },
    methods:{
        handleChange(e){
            this.$emit("customChange",e.target.value.toUpperCase())

        }
    }


}
</script>

<style>

</style>