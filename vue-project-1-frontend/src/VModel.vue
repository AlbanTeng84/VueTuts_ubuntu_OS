<template>
  <h1>{{toVModel}}</h1>
  <form @submit.prevent="postUser" method="post">
    <label>ID</label>
    <input v-model.number=id> <br><br>
    <label>Name</label>
    <input type="text" v-model=name> <br><br>
    <label>Position</label>
    <input type="text" v-model=position><br><br>
    <input type="submit">

  </form>

    <h1>
        {{id}}
    </h1>

    <h1>
        {{name}}
    </h1>
    <h1>
        {{position}}    
    </h1>
    <h3>{{getData}}</h3>

</template>

<script>
export default {
    name:'VModel',
    props:{
        'toVModel':String
    },
    data(){
        return{
            id:" ",
            name:" ",
            position:" ",
            getData:" ",
            postData:" ",
        }
    },
    // mounted(){
    //     fetch('http://localhost:5000',{
    //             method: 'get'

    //         })
    //         .then(response=>response.json())
    //         .then(data => this.getData = data)

    //     },

    methods:{
        postUser(e){
            fetch('http://localhost:5000',{
                method: 'POST',
                headers: {
                    'content-type': 'application/json',
                    
                },
                mode: 'no-cors', 
                body: JSON.stringify({
                      id:this.id,
                      name:this.name,
                      position:this.position,
                   })
                        
            })
            .then(response => response.json())
            .then(data => this.postData = data)
        }
    }

       
    

    
}
</script>

<style>

</style>