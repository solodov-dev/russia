<template>
  <div id="app">
    <top-navigation></top-navigation>
    <russia-map></russia-map>
  </div>
</template>

<script>
import RussiaMap from './components/RussiaMap.vue'
import TopNavigation from './components/TopNavigation.vue'


export default {
  name: 'app',
  components: {
    RussiaMap,
    TopNavigation,
  }
}
</script>

<style>
* {
  box-sizing: border-box;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
