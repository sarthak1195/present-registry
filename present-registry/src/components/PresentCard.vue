<template>
    <div class="PresentCard">
      <div class="presentCard-inner">
          <div class="presentCard-title">
              <h2>{{presentCard.presentName}}</h2>
          </div>
          <div class="presentCard-image-wrap">
              <img v-bind:src="presentCard.src" class="image"/>
              <!-- <img src="https://food.fnr.sndimg.com/content/dam/images/food/fullset/2009/2/23/1/LR0202-4_Excellent-Meatballs_s4x3.jpg.rend.hgtvcom.616.462.suffix/1432472001768.jpeg" class="image"/> -->
          </div>
          <div class="presentCard-detail">
              <p>{{presentCard.presentDescription}}</p>
          </div>
          <div class="presentCard-interface">
              <div class="bought-present" v-if="!bought">
                  <button @click="signOffPresent()" type="button" class="btn btn-buy">Sign on to buy</button>
              </div>
              <div v-if="bought">
                  <button type="button" disabled class="btn btn-signed-off">Present has been signed off</button>
              </div>
          </div>
      </div>
    </div>  
</template>

<script>
export default {
    name: "PresentCard",
    props: ['presentCard'],
    data() {
        return {
            bought: false
        }
    },
    methods: {
        signOffPresent(){
            this.bought = true;
        }
    }
}
</script>

<style scoped>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&display=swap');

    .PresentCard {
        flex: 1 1 10%;
        width: 100%;
        padding: 20px;
    }

    .presentCard-inner {
        position: relative;
        padding: 25px;
        box-shadow: 0px 0px 16px rgba(0, 0, 0, 0.25);
        background-color: rgb(255, 179, 217, 0.35);
        border-radius: 25px;
        max-width: 350px;
    }

    .presentCard-inner:hover {
        position: relative;
        padding: 25px;
        box-shadow: 0px 0px 100px rgba(0, 0, 0, 0.25);
        background-color: rgb(255, 179, 217, 0.35);
        border-radius: 25px;
        max-width: 350px;
    }

    .presentCard-image-wrap {
        width: 100%;
    }

    .presentCard-image-wrap img {
        max-width: 275px;
        max-height: 275px;
    }

    .image{
        margin: 10px auto;
    }
    .presentCard-detail {
        padding: 10px;
        margin: 10px;
        background-color: rgb(255, 255, 255, .30);
    }

    .btn-buy {
        margin: 10px;
        background: rgb(83, 216, 112) !important;
    }

    .btn-buy:hover {
        background: rgb(166, 255, 184) !important;
    }

    .btn-signed-off {
        margin: 10px;
        background: rgb(141, 141, 141)) !important;
    }

    .presentCard-title {
        font-family: 'Playfair Display', serif;
        font-size: 350px !important;
        background-color: rgb(166, 255, 184, 0.75);
        border-radius: 100px;
        box-shadow: 0px 0px 25px rgba(255, 255, 255, 0.505);
        text-align: center;
    }
</style>