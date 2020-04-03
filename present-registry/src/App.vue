<template>
  <div id="app">
    <HeaderContainer/>
    <Modal/>
    <section class="PresentList">
      <PresentCard
        v-for="presentCard in PresentList"
        :key="presentCard.PresentName"
        :presentCard="presentCard"
        v-on:delete-presentCard="deletePresentCard"
      />
    </section>

  </div>
</template>

<script>
import HeaderContainer from './components/HeaderContainer.vue'
import PresentCard from './components/PresentCard.vue'
// import PresentList from './components/PresentList.vue'

export default {
  name: 'App',
  components: {
    HeaderContainer,
    PresentCard
    // PresentList
  },
  data() {
        return {
            PresentList: [
                {
                    presentID: 1,
                    presentName: "Stuffed Tiger",
                    presentDescription: "Fluffy and great for cuddling!" ,
                    src: require("./assets/images/presents/tiger.jpg")
                },
                {
                    presentID: 2,
                    presentName: "Cutlery",
                    presentDescription: "Silverware to impress you guests!" ,
                    src: require("./assets/images/presents/cutlery.webp")
                },
                {
                    presentID: 3,
                    presentName: "Spice Rack",
                    presentDescription: "Make you kitchen functional with this spice rack!" ,
                    src: require("./assets/images/presents/spiceRack.jpg")
                },
                {
                    presentID: 4,
                    presentName: "Nose Rings",
                    presentDescription: "Silverware to impress you guests!" ,
                    src: require("./assets/images/presents/noseRings.jpg")
                },
                {
                    presentID: 5,
                    presentName: "Insta-Pot",
                    presentDescription: "Cook any meal in atleast half the time!" ,
                    src: require("./assets/images/presents/instapot.jpg")
                },
                {
                    presentID: 6,
                    presentName: "500 lbs of Raw Meat",
                    presentDescription: "Great to feed your tigers!" ,
                    src: require("./assets/images/presents/rawMeat.jpg")
                },
            ]
        }
    },
    methods: {
      deletePresentCard(id) {
        this.PresentList = this.PresentList.filter(presentCard => presentCard.presentID != id);
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

  .PresentList {
    display: flex;
    flex-wrap: wrap;
    padding: 25px;
  }
</style>
