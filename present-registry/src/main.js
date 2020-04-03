import Vue from 'vue'
import App from './App.vue'
import 'bootstrap'; 
import 'bootstrap/dist/css/bootstrap.min.css';
import VModal from 'vue-js-modal';


Vue.config.productionTip = false
Vue.use(VModal)

new Vue({
  render: h => h(App),
}).$mount('#app')
