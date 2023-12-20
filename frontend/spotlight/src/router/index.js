import { createRouter, createWebHistory } from 'vue-router'
import UserLogin from '@/views/UserLogin.vue'
import SignUp from '@/views/SignUp.vue'
import AdminLogin from '@/views/AdminLogin.vue'
import Dashboard from '@/views/Dashboard.vue'
import CreatorDashboard from '@/views/CreatorDashboard.vue'
import AdminDashboard from '@/views/AdminDashboard.vue'
import CreatePlaylist from '@/views/CreatePlaylist.vue'
import PlaylistView from '@/views/PlaylistView.vue'
import CreateAlbum from '@/views/CreateAlbum.vue'
import GenreRequest from '@/views/GenreRequest.vue'
import AddSong from '@/views/AddSong.vue'
import SongView from '@/views/SongView.vue'

const routes = [
  {
    path: '/',
    redirect: '/login',
    name: 'home',
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
    path: "/playlist/new",
    name: "newPlaylist",
    component: CreatePlaylist,
    beforeEnter() {
      if (!localStorage.getItem("Auth-Token")) {
        return "/login";
      }
      if (localStorage.getItem("role") == "admin") {
        alert("Admins cannot create playlists");
        return "/dashboard/a";
      }
    }
  },
  {
    path: "/playlist/:playlistID",
    name: "playlist",
    component: PlaylistView,
    beforeEnter() {
      if (!localStorage.getItem("Auth-Token")) {
        return "/login";
      }
    }
  },
  {
    path: "/song/:songID",
    name: "songView",
    component: SongView,
    beforeEnter() {
      if (!localStorage.getItem("Auth-Token")) {
        return "/login";
      }
    }
  },
  {
    path: "/album/new",
    name: "newAlbum",
    component: CreateAlbum,
    beforeEnter() {
      if (!localStorage.getItem("Auth-Token")) {
        return "/login";
      }
      if (localStorage.getItem("role") != "creator") {
        alert("you cannot create albums");
        return "/dashboard";
      }
    }
  },
  {
    path: "/song/new",
    name: "newSong",
    component: AddSong,
    beforeEnter() {
      if (!localStorage.getItem("Auth-Token")) {
        return "/login";
      }
      if (localStorage.getItem("role") != "creator") {
        alert("you cannot create albums");
        return "/dashboard";
      }
    }
  },
  {
    path: "/genre/new",
    name: "newGenre",
    component: GenreRequest,
    beforeEnter() {
      if (!localStorage.getItem("Auth-Token")) {
        return "/login";
      }
      if (localStorage.getItem("role") != "creator") {
        alert("you cannot request for new genres");
        return "/dashboard";
      }
    }
  },
  // {
  //   path: '/about',
  //   name: 'about',
  //   component: () => import('../views/AboutView.vue')
  // },
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
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router
