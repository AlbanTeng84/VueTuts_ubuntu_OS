<template>
    <h1>{{msg}}</h1>
    <div class="container">
        <button class="btn btn-success">Click me</button>
        <button>Click me</button>
    </div>
    <div class="container">
        <div class="row">
            <div class="col-8">
                <div class="card">
                    <img src="https://fastly.picsum.photos/id/276/200/300.jpg?hmac=5VSJJxPMnu25ukKlrNc0y2KxLtG_jF7BfA13IlTm0uo" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">Card title</h5>
                        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                        <a href="#" class="btn btn-primary">Go somewhere</a>
                    </div>
                </div>
            </div>
        
        </div>
        
    </div>

    <div class="contiainer">
        <div class="row" style="width:1000px">
            <div class="col align-self-end">
                <div id="carouselExample" class="carousel slide">
        <div class="carousel-inner">
                <div class="carousel-item active">
                <img src="https://picsum.photos/id/237/200/300" class="d-block w-30" alt="...">
                </div>
                <div class="carousel-item">
                <img src="https://picsum.photos/seed/picsum/200/300" class="d-block w-20" alt="...">
                </div>
                <div class="carousel-item">
                <img src="https://picsum.photos/200/300?grayscale" class="d-block w-20" alt="...">
                </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
        </button>
    </div>
            </div>
        </div>
    </div>

   
    <div class="container">
        <div class="position-relat">
            <div class="position-absolute top-0 end-0">
                <table class="table">
                <tr>
                    <th scope="col" :href="Player">{{Player}}</th>
                    <th scope="col">Googles</th>
                    <th scope="col">ZA</th>
                </tr>
                </table>
            </div>
        </div>
        

    </div>

    <div class="position-relative">
            <div class="position-absolute bottom-0 end-0">
                <a :href="Player"></a>
            </div>
    </div>
  </template>
  
  <script>
  export default {
    data(){
        return{
            msg:"this is testing Button",
            Player:"https://picsum.photos/200/300?grayscale"
            
        }
    }
  }
  </script>
  
  <style>
  
  </style>