<template>
  <div id="app">
    <top-navigation v-show="!articleIsOpened"></top-navigation>
    <russia-map v-show="!articleIsOpened"></russia-map>
    <entry-article v-show="articleIsOpened"></entry-article>
  </div>
</template>

<script>
import RussiaMap from './components/RussiaMap.vue';
import TopNavigation from './components/TopNavigation.vue';
import Article from './components/Article.vue';
import { eventBus } from './main';


export default {
  name: 'app',
  data: function() {
    return {
      articleIsOpened: false,
    }
  },
  components: {
    TopNavigation,
    RussiaMap,
    entryArticle: Article,
  },
  created() {
    eventBus.$on('articleOpened', () => {
      this.articleIsOpened = true;
    });
    eventBus.$on('articleClosed', () => {
      this.articleIsOpened = false;
    })
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
  width: 100%;
}
</style>
