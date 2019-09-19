<template>
<svg   
   width="1225" height="760" viewBox="0 0 1225 760"
   preserveAspectRatio="xMidYMid meet"
   class="map" id="russia-map">
   <path 
      v-for="region in mapRussia"
      :key="region.name"
      :d="region.d"
      :title="region.name"
      class="map-region"
   />
</svg>
</template>
<script>
import { mapData } from "../assets/regions.js";

export default {
   data: function() {
      return {
         mapRussia: mapData,
      }
   },
}
</script>
<style scoped>
    .map {
        height: 80vh;
        display: block;
        margin: 10px auto;
    }

    .map-region {
        fill: #54f389;
    }

    .map-region:hover {
        fill: #218b45;
    }
</style>