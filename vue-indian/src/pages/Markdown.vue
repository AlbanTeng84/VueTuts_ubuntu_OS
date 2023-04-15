<template>
<div class="flex flex-wrap w-full">
  <h1 class="w-full text-center text-3xl my-4">Markdown App</h1>
  <section  class="flex m-auto w-10/12 h-screen">
    <article class="w-1/2 border">
        <textarea class="w-full h-full" v-model="text"></textarea>
    </article>
    <article class="w-1/2 border bg-gray-100">
    {{text}}
    </article>
  </section>
</div>
</template>

<script>

export default {
  // beforeCreate(){
  //   console.log('before created')
  // },
  // created(){
  //   console.log('created')
  // },
  // beforeMount(){
  //   console.log('before mount')
  // },
  // mounted(){
  //   console.log('mounted')
  // },
  // beforeUnmount(){
  //   console.log('before unmount')
  // },
  // unmounted(){
  //   console.log('unmounted')
  // },
  beforeUpdate(){
    console.log('before update')
  },
  updated(){
    console.log('updated')
  },

    data(){
        return{
            text:""
        }
    }
}
</script>

<style>

</style>