<template>
  <div class="header">
    <nav class="navbar navbar-expand-lg navbar-light bg-Dark">
      <a class="navbar-brand title" href="#">GiftLand</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarText">
        <ul class="navbar-nav mr-auto">
        </ul>
        <span class="navbar-text">
          <Modal/>
        </span>
      </div>
    </nav>
    <transition name="fade" appear>
        <div class="modal-overlay" v-if="showModal" @click="showModal = false"></div>
    </transition>
    <div class="hero-image">
      <div class="hero-text">
        <h1>Joe Exotic's Wedding</h1>
        <p>Everyone's invited except Carole</p>
      </div>
    </div>
  </div>
</template>

<script>
import Modal from './Modal.vue'

export default {
  name: 'HeaderContainer',
  components: {
    Modal
  },
  data() {
    return{
      title: "Gift-Land",
      showModal: false
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  @import '../assets/styles/Header.css';
  a.navbar-brand{
    display:inline;
    text-align: center;
    color: #FFFFFC;
    font-weight: 700;
    font-size: 200%;
  }

  a.navbar-brand:hover{
    display:inline;
    text-align: center;
    color: rgb(255, 203, 246);
    font-weight: 700;
    font-size: 200%;
  }
</style>
