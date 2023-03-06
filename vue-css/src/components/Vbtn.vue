<template>
   <div class="container border">
        <div class="row">
            <div class="col-md-8">col 1</div>
            <div class="col-md-4">col 2</div>
      
        </div>
   </div>

   <div class="container text-center border" >
  <div class="row justify-content" >
    <div class="col">
      1
    </div>
    <div class="col">
      2
    </div>
  </div>
</div>

<div class="container px-4 text-center border" style="height:500px">
  <div class="row gx-5">
    <div class="col">
     <div class="p-3">Custom column padding</div>
    </div>
    <div class="col">
      <div class="p-3">Custom column padding</div>
    </div>
  </div>
</div>
    
</template>


<script>
export default {
    data:()=>{
        return {
            
        }

    }
}

</script>
<style>
   [class*='col'] {
        padding: 1rem;
        background: #33b5e5;
        border: 2px solid white;
        color:#fff;
    }
</style>
