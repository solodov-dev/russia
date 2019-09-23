<template>
    <nav>
        <ul class="menu">
            <li class="menu-item" v-for="(category, index) in categories" :key="index">
                <a href="#" class="btn" @click="showLocations(category)">{{category}}</a>
            </li>
        </ul>
    </nav>
</template>
<script>
import {eventBus} from '../main'

export default {
    data: function() {
        return {
            categories: ['people', 'places', 'animals', 'economy']
        }
    },
    methods: {
        showLocations(category) {
            eventBus.$emit('categoryChanged', category)
        }
    }
}
</script>
<style scoped>
    .menu {
        list-style: none;
    }

    .menu-item {
        display: inline;
    }
    
    .btn {
        background-color: coral;
        color: white;
        border-radius: 50px;
        padding: 10px;
        margin: 1em;
        text-decoration: none;
        cursor: pointer;
    }

    .btn:hover {
        background-color: chocolate;
    }

</style>