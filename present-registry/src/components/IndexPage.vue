<template>
    <div class="IndexPage">
        <HeroImage v-bind:HeroImageData="indexData"/>
        <RegistryList v-bind:registries="registries"/>
    </div>
</template>

<script>

import HeroImage from './HeroImage.vue'
import RegistryList from './RegistryList'

export default {
    name: "IndexPage",
    components: {
        HeroImage, RegistryList
    },
    props:["indexData","registries"]
}
</script>

<style>
</style>