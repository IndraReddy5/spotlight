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
        return "/dashboard/a";
      }
    }
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: Dashboard,
    beforeEnter() {
      if (!localStorage.getItem("Auth-Token")) {
        return "/login";
      }
      if (localStorage.getItem("role") === "admin") {
        return "/dashboard/a";
      }
      if (localStorage.getItem("role") === "creator") {
        return "/dashboard/c";
      }
    }
  },
  {
    path: '/dashboard/c',
    name: 'CreatorDashboard',
    component: CreatorDashboard,
    beforeEnter() {
      if (!localStorage.getItem("Auth-Token")) {
        return "/login";
      }
      if (localStorage.getItem("role") != "creator") {
        return "/dashboard";
      }
    }
  },
  {
    path: '/dashboard/a',
    name: 'AdminDashboard',
    component: AdminDashboard,
    beforeEnter() {
      if (!localStorage.getItem("Auth-Token")) {
        return "/login";
      }
      if (localStorage.getItem("role") != "admin") {
        return "/dashboard";
      }
    }
  },
  {
    path: '/about',
    name: 'about',
    component: () => import('../views/AboutView.vue')
  },
  {
    path: "/logout",
    name: "logout",
    beforeEnter(to, from, next) {
      fetch(__API_URL__ + "logout",
        {
          headers: { 'content-type': 'application/json', "Auth-Token": localStorage.getItem("Auth-Token") },
          'method': 'POST'
        })
      localStorage.clear();
      if (from.path == '/login') {
        next("/adminlogin");
      }
      else {
        next("/login");
      }
    }
  }
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router
