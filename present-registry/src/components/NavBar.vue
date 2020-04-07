<template>
  <div class="NavBar">
    <nav class="navbar navbar-expand-lg navbar-light bg-Dark stripes">
      <router-link class="routerLink" to="/"><h1 class="navbar-brand title">GiftLand</h1></router-link>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarText">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item">
            <router-link class="subItem" to="CreateRegistry">Create Registry</router-link>
          </li>
          <li class="nav-item">
          </li>
        </ul>
        <div class="authentication-modals">
          <span class="navbar-text">
            <ModalLogin/>
          </span>
          <span>|</span>
          <span class="navbar-text">
            <ModalRegister/>
          </span>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
import ModalLogin from './ModalLogin.vue'
import ModalRegister from './ModalRegister.vue'

export default {
  name: 'NavBar',
  components: {
    ModalLogin,
    ModalRegister
  },
    
}
</script>

<style>
    @import '../assets/styles/NavBar.css';
</style>