import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: Login
    },
    {
      path: '/adminPanel',
      name: 'adminPanel',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AdminPanel.vue')
    },
    {
      path: '/studentLogin',
      name: 'studentLogin',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/StudentLogin.vue')
    },
    {
      path: '/test/:id',
      name: 'test',
      component: () => import('../views/Test.vue')
    }
  ]
})

export default router
