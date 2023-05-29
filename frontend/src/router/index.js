import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
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
    // {
    //   path: '/studentLogin',
    //   name: 'studentLogin',
    //   // route level code-splitting
    //   // this generates a separate chunk (About.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import('../views/StudentLogin.vue')
    // },
    {
      path: '/test/:id',
      name: 'test',
      component: () => import('../views/Test.vue')
    }
  ]
})

// router.beforeEach((to, from, next) => {
//   // redirect to login page if not logged in and trying to access a restricted page
//   const publicPages = ['/login'];
//   const authRequired = !publicPages.includes(to.path);
//   const loggedIn = localStorage.getItem('access_token');

//   if (authRequired && !loggedIn) {
//     return next('/login');
//   }

//   next();
// })

export default router
