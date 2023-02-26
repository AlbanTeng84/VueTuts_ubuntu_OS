<template>
  <h1>{{ msg }} - {{ title.company }}</h1>
</template>

<script>
export default {
    data(){
        return{
            msg:"This is test2 page"
        }
    },
    props:['title']

}
</script>

<style>

</style>
