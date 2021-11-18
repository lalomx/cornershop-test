import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Orders from '../views/Orders.vue'
import Choose from '../views/Choose.vue'
import Menu from '../views/Menu.vue'
import Employees from '../views/Employees.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/orders',
    name: 'Orders',
    component: Orders
  },
  {
    path: '/choose',
    name: 'Choose',
    component: Choose
  },
  {
    path: '/menu',
    name: 'Menu',
    component: Menu
  },
  {
    path: '/employees',
    name: 'Employees',
    component: Employees
  },
  {
    path: '',
    redirect: 'home'
  }
]

const router = new VueRouter({
  base: process.env.BASE_URL,
  routes
})

export default router
