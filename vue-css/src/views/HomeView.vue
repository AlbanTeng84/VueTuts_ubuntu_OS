<template>
  <v-app app>
    <Vbtn />
  </v-app>
  
  
</template>

<script>
import { defineComponent } from 'vue';

// Components
import Vbtn from '../components/Vbtn.vue';

export default defineComponent({
  name: 'HomeView',

  components: {
    Vbtn,
  },
});
</script>
