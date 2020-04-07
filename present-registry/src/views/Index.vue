<template>
  <div >
    <IndexPage 
      class = "show"
      v-bind:indexData="IndexPageData"
      v-bind:registries="RegistryList"
    />
  </div>
</template>

<script>
import store from "@/store.js"
import IndexPage from '../components/IndexPage.vue'

export default {
  name: 'Index',
  components: {
    IndexPage
  },
  data() {
        return {
            IndexPageData: store.IndexPageData,
            RegistryList: store.RegistryList
        }
    }
}
</script>

<style>
  * {
    margin:0;
    padding: 0;
    box-sizing: border-box;
  }

  main {
    width: 100vw;
    min-height: 100vh;
    overflow: hidden;

    display: flex;
    justify-content: center;
    align-items: center;
  }

  .hide {
    margin: 0;
    padding: 0;
    display: none;
  }
</style>
