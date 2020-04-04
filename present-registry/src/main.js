import Vue from 'vue'
import App from './App.vue'
import 'bootstrap'; 
import 'bootstrap/dist/css/bootstrap.min.css';
import VModal from 'vue-js-modal';
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.config.productionTip = false
Vue.use(VModal)
Vue.use(VueAxios, axios)

new Vue({
  render: h => h(App),
}).$mount('#app')
