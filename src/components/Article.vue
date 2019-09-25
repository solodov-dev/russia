<template>
    <article>
        <img :src="getSvg()">
        <h1>{{ title }}</h1>
        <p>{{ text }}</p>
        <button @click="backToMap()">Back</button>
    </article>
</template>
<script>
import { eventBus } from "../main";
import { articleData } from "../assets/articleData"

export default {
    data: function() {
        return {
            currentImage: "tolstoy",
            text: "Hello",
        }
    },
    methods: {
    getSvg() {
      let images = require.context('../assets/', false, /\.svg$/);
      return images('./' + this.currentImage + ".svg")
    },
    backToMap() {
        eventBus.$emit("articleClosed");
    }
  },
  created() {
        eventBus.$on("articleOpened", article => {
            this.title = articleData[article].title;
            this.text = articleData[article].text;
            this.currentImage = article;
        });
    }
}
</script>
<style scoped>
    article {
        margin: 0 auto;
        width: 80vw;
    }
    img {
        height: 20vh;
    }

    p {
        text-align: justify;
        font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    }
</style>