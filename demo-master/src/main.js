import Vue from 'vue'
import VUeJsonp from 'vue-jsonp'
import App from './App.vue'
import router from './router'
import './plugin/element.js'
import 'element-ui/lib/theme-chalk/index.css'
import './assets/css/global/global.css'
import axios from 'axios'
import ElementUI from 'element-ui'

Vue.use(VUeJsonp)

Vue.use(ElementUI)

Vue.config.productionTip = false

Vue.prototype.$http = axios

router.beforeEach((to, from, next) => {
  /* 路由发生变化修改页面title */
  if (to.meta.title) {
    document.title = to.meta.title
  }
  next()
})
new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
