import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import { checkLogin } from '../utils/Authentication'
import ComputerView from '../views/ComputerView.vue'

const router = createRouter({
  history: createWebHistory("."),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/stats',
      name: 'stats',
      component: () => import('../views/StatisticsView.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/admin_panel',
      name: 'adminpanel',
      component: () => import('../views/AdminView.vue')
    },
    {
      path: "/computers",
      name: "computers",
      component: ComputerView
    }
  ]
})

/* router.beforeEach(async (to, from) => {
  const isAuthenticated = await checkLogin();

  if (!isAuthenticated && to.name == "adminpanel") {
    return { name: "login" }
  }
}) */

export default router
