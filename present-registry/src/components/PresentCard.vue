<template>
    <div class="presentCard">
      <div class="presentCard-inner">
          <div class="presentCard-title">
              <h2>{{presentCard.presentName}}</h2>
          </div>
          <div class="presentCard-image-wrap">
              <img v-bind:src="presentCard.src" class="image"/>
          </div>
          <div class="presentCard-detail">
              <p>{{presentCard.presentDescription}}</p>
          </div>
          <div class="presentCard-interface">
              <button @click="$emit('delete-presentCard', presentCard.presentID)" type="button" class="btn btn-buy">Buy</button>
          </div>
      </div>
    </div>  
</template>

<script>
export default {
    name: "presentCard",
    props: ['presentCard']
}
</script>

<style scoped>
    .presentCard {
        flex: 1 1 33.333%;
        width: 100%;
        padding: 25px;
    }

    .presentCard-inner {
        position: relative;
        padding: 25px;
        box-shadow: 0px 0px 16px rgba(0, 0, 0, 0.25);
    }

    .presentCard-image-wrap {
        width: 100%;
    }

    .presentCard-image-wrap img {
        max-width: 500px;
        max-height: 500px;
    }

    .btn-buy {
        background: rgb(74, 226, 107) !important;
    }

    .btn-buy:hover {
        background: rgb(166, 255, 184) !important;
    }
</style>