<template>
  <div class="header">
    <nav class="navbar navbar-expand-lg navbar-light bg-Dark">
      <a class="navbar-brand title" href="#">GiftLand</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarText">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <a class="nav-link" href="#">About<span class="sr-only">(current)</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Create Registry</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Cart</a>
          </li>
        </ul>
        <span class="navbar-text">
          <Modal/>
        </span>
      </div>
    </nav>
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

  .nav-link{
    color:  #FFFFFC !important;
  }
</style>
