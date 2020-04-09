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
        <div  v-if="!authenticated" class="authentication-modals">
          <span class="navbar-text">
            <ModalLogin v-on:authenticated="authenticateSwitch"/>
          </span>
          <span>|</span>
          <span class="navbar-text">
            <ModalRegister/>
          </span>
        </div>
        <div v-if="authenticated" class="signed-in ">
          <span class="navbar-text ">
            Hello, {{username}}
          </span>
          <span>|</span>
          <span class="navbar-text">
            <button @click="authenticateSwitch" type="button" class="btn signout-btn">Sign Out</button>
            <!--<button @click="logout()" type="button" class="btn signout-btn">Sign Out</button>-->
          </span>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
import ModalLogin from './ModalLogin.vue'
import ModalRegister from './ModalRegister.vue'
import axios from 'axios'

export default {
  name: 'NavBar',
  components: {
    ModalLogin,
    ModalRegister
  },
  data() {
    return {
      serviceURL: "http://info3103.cs.unb.ca:8040",
      authenticated: false,
      username: "John"
    }
  }, 
  methods: {
    authenticateSwitch() {
      if(this.authenticated)
        this.authenticated = false;
      else
        this.authenticated = true;
    },

    logout() {
      axios
      .delete(this.serviceURL+'/signin')
      .then(function (response) {
         if (response.data.status == "success") {
           this.authenticated = false
         }
      })
      .catch(function (error) {
          alert("There was a problem while signing out: " + error)
      })
    }
  }
    
}
</script>

<style>
    @import '../assets/styles/NavBar.css';

    .signed-in span{
      padding: 10px;
      font-size: 150%;
      color: white !important;
      font-weight: 700;
    }

    .signout-btn{
      background-color: white!important;
    }
</style>