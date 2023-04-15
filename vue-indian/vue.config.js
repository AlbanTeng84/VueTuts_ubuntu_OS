const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  // devServer:{
  //   proxy:{
      
  //     '/api/':{
  //       target: baseUrl,
  //       changeOrigin:true,
  //       ['/api/']:'',
  //     },
  //     '/code/':{
  //       target: baseUrl,
  //       changeOrigin:true,
  //       ['code']:'',
  //     },
  //     '/image/':{
  //       target: baseUrl,
  //       changeOrigin:true,
  //       ['image']:'',
  //     },
  //   },
  //   host: 'localhost',
  //   localhost:8080,
  //   client:{
  //     WebSocketURL: 'ws://localhost/ws'
  //   },
  //   headers:{
  //     'Access-Control-Allow-Origin':'*',
  //   }
  // },
  transpileDependencies: true,
})
