import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import HelloWorld from '../components/HelloWorld'
import Overview from '../components/Overview'
import Monitor from '../components/Monitor'
import Warning from '../components/Warning'

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
      path: '/monitor',
      name: 'Monitor',
      component: Monitor
    },
    {
      path: '/overview',
      name: 'Overview',
      component: Overview
    },
    {
      path: '/warning',
      name: 'Warning',
      component: Warning
    }
  ]
})
