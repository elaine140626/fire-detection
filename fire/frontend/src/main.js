// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import 'element-ui/lib/theme-chalk/display.css'
import '../static/css/style.css'

Vue.use(ElementUI)
Vue.prototype.$axios = axios
Vue.prototype.$axios.defaults.withCredentials = true
Vue.prototype.urlHead = 'http://127.0.0.1:8000'
// Vue.prototype.urlHead = ''

router.beforeEach((to, from, next) => {
  console.log(from.name)
  console.log(to.name)
  axios.get(Vue.prototype.urlHead + '/api/user/check_login/', {
    withCredentials: true
  })
    .then((e) => {
      if (e.data.code === 0) {
        if (to.name === 'Login') {
          next({
            path: 'overview'
          })
        } else {
          next()
        }
      } else {
        if (to.name === 'Login') {
          next()
        } else {
          next({
            path: 'login'
          })
        }
      }
    })
    .catch(() => {
      if (to.name === 'Login') {
        next()
      } else {
        next({
          path: 'login'
        })
      }
    })
})

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
