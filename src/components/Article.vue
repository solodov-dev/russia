<template>
    <transition name="fade">
        <article>
            <img :src="getSvg()">
            <h1>{{ title }}</h1>
            <p>{{ text }}</p>
            <button @click="backToMap()">&times;</button>
        </article>
    </transition>
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
        z-index: 2;
        background: white;
        position: absolute;
        padding: 50px;
        top: 10%;
        left: 20%;
        width: 60%;
        border-radius: 10px;
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
    }
    img {
        height: 20vh;
    }

    p {
        text-align: justify;
        font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    }

    button {
        position: absolute;
        top: 10px;
        right: 10px;
        font-size: 30px;
        border-radius: 50px;
        border: none;
        background: none;
    }
</style>