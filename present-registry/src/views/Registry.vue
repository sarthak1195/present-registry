<template>
    <div class="Registry">
        <HeroImage v-bind:HeroImageData="registry"/>
        <section class="PresentList">
            <PresentCard
                v-for="presentCard in registry.presentsList"
                :key="presentCard.PresentName"
                :presentCard="presentCard"
                v-on:delete-presentCard="deletePresentCard"
            />
            <AddCard />
        </section>
    </div>
</template>

<script>
import HeroImage from '../components/HeroImage.vue'
import PresentCard from '../components/PresentCard.vue'
import store from '@/store.js'
import AddCard from '../components/AddCard.vue'

export default {
    name: 'Registry',
    components: {
        HeroImage,
        PresentCard,
        AddCard
    },
    methods: {
        deletePresentCard(id) {
            this.PresentList = this.PresentList.filter(presentCard => presentCard.presentID != id);
        }
    },
    data(){
        return {
            registryID:this.$route.params.registryID
        }
    },
    computed:{
        registry(){
            return store.RegistryList.find(
                registry => registry.registryID === this.registryID
            )
        }
    }
}
</script>

<style>
    .PresentList {
        display: flex;
        flex-wrap: wrap;
        padding: 25px;
    }
</style>