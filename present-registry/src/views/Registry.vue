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
import axios from 'axios'

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
        },

        getRegistryInfo(RID) {
            axios
            .get(this.serviceURL + '/registry/' + RID)
            .then(function (response) {
                this.registryInfo = response.data.RegistryList
                this.getPresentsInRegistryInfo(RID);
            })
            .catch(function (error) {
                alert(error)
            })
        },

        getPresentsInRegistryInfo(RID) {
            axios
            .get(this.serviceURL + '/registry/' + RID + '/presents')
            .then(function (response) {
                this.presentsInRegistryInfo = response.data.presentsInRegistry
            })
            .catch(function (error) {
                alert(error)
            })
        }

    },

    data(){
        return {
            registryID:this.$route.params.registryID,
            // Changes
            serviceURL: 'http://info3103.cs.unb.ca:8040',
            registryInfo: '',
            presentsInRegistryInfo: '',
            RID: Number
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