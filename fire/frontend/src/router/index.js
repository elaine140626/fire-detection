import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import HelloWorld from '../components/HelloWorld'
import Overview from '../components/Overview'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/login'
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/test',
      name: 'Test',
      component: HelloWorld
    },
    {
      path: '/overview',
      name: 'Overview',
      component: Overview
    }
  ]
})
