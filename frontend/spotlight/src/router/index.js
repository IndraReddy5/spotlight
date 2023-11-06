import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import UserLogin from '@/views/UserLogin.vue'
import SignUp from '@/views/SignUp.vue'
import AdminLogin from '@/views/AdminLogin.vue'
import Dashboard from '@/views/Dashboard.vue'
import CreatorDashboard from '@/views/CreatorDashboard.vue'
import AdminDashboard from '@/views/AdminDashboard.vue'

const routes = [
    {
      path: '/',
      redirect: '/login',
      name: 'home',
      component: HomeView
    },
    {
      path: '/login',
      name: 'login',
      component: UserLogin,
      beforeEnter() {
        if (localStorage.getItem("Auth-Token")) {
          return "/dashboard";
        }
      }
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUp,
      beforeEnter() {
        if (localStorage.getItem("Auth-Token")) {
          return "/dashboard";
        }
      }
    },
    {
      path: '/adminlogin',
      name: 'adminlogin',
      component: AdminLogin,
      beforeEnter() {
        if (localStorage.getItem("Auth-Token")) {
          return "/dashboard";
        }
      }
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: Dashboard,
    },
    {
      path: '/dashboard/c',
      name: 'CreatorDashboard',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: CreatorDashboard,
    },
    {
      path: '/dashboard/a',
      name: 'AdminDashboard',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: AdminDashboard,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    }
  ];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router
