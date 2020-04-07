import Vue from 'vue'
import App from './App.vue'
import 'bootstrap'; 
import 'bootstrap/dist/css/bootstrap.min.css';
import VModal from 'vue-js-modal';
import axios from 'axios'
import VueAxios from 'vue-axios'
import router from './router'
import Vuex from 'vuex'

Vue.config.productionTip = false
Vue.use(VModal)
Vue.use(VueAxios, axios)
Vue.use(Vuex)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
