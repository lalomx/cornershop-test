import axios from 'axios'
import Vue from 'vue'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false

axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'
axios.defaults.xsrfCookieName = 'csrftoken'

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
