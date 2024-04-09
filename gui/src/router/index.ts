import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import { checkLogin } from '../utils/Authentication';
import ProductList from '@/views/ProductList.vue';
import ShoppingCart from '@/views/ShoppingCart.vue';

const router = createRouter({
    history: createWebHistory("."),
    routes: [
        {
            path: '/',
            name: 'home',
            redirect: { name: 'products' }
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
            path: "/products",
            name: "products",
            component: ProductList
        },
        {
            path: "/shoppingcart",
            name: "shoppingcart",
            component: ShoppingCart
        }
    ]
});

/* router.beforeEach(async (to, from) => {
  const isAuthenticated = await checkLogin();

  if (!isAuthenticated && to.name == "adminpanel") {
    return { name: "login" }
  }
}) */

export default router;
