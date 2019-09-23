<template>
  <svg
    width="1225"
    height="760"
    viewBox="0 0 1225 760"
    preserveAspectRatio="xMidYMid meet"
    class="map"
    id="russia-map"
  >
    <path
      v-for="region in mapRussia"
      :key="region.id"
      :d="region.d"
      :people="region.people"
      :places="region.places"
      :animals="region.animals"
      :economy="region.economy"
      class="map-region"
      @click="getInfo(region.name)"
    />
    <circle
      v-for="(place, index) in places"
      :key="index"
      class="pin"
      :cx="place.x + place.width / 2"
      :cy="place.y + place.height / 2"
      r="30"
    />
  </svg>
</template>
<script>
import { mapData } from "../assets/regions.js";
import { eventBus } from "../main";

export default {
  data: function() {
    return {
      mapRussia: mapData,
      places: []
    };
  },
  methods: {
    getInfo(name) {
      console.log(name);
    }
  },
  created() {
    eventBus.$on("categoryChanged", category => {
      let nodes = document.querySelectorAll(
        `path[${category}]:not([${category}="null"])`
      );
      for (let node of nodes) {
        this.places.push(node.getBBox());
      }
    });
  }
};
</script>
<style scoped>
.map {
  height: 80vh;
  display: block;
  margin: 10px auto;
}

.map-region {
  fill: #5280ff;
}

.map-region:hover {
  fill: #ff6868;
}
.pin {
  fill: #ff6868;
}
.pin:hover {
  transform: scale(1.2);
}
</style>