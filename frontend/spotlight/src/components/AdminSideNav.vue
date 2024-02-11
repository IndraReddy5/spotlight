<template>
  <nav id="sidebarMenu" class="col-md-3 col-lg-2 d-md-block bg-dark sidebar collapse" style="">
    <div class="position-sticky pt-3">
      <h6 class="d-flex align-items-center ps-1 mt-4 mb-1">
        <div class="nav-link pt-2">
          <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="none" class="bi bi-bookmarks"
            stroke="var(--bp-khaki)" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"
            aria-hidden="true">
            <path
              d="M2 4a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v11.5a.5.5 0 0 1-.777.416L7 13.101l-4.223 2.815A.5.5 0 0 1 2 15.5V4zm2-1a1 1 0 0 0-1 1v10.566l3.723-2.482a.5.5 0 0 1 .554 0L11 14.566V4a1 1 0 0 0-1-1H4z" />
            <path d="M4.268 1H12a1 1 0 0 1 1 1v11.768l.223.148A.5.5 0 0 0 14 13.5V2a2 2 0 0 0-2-2H6a2 2 0 0 0-1.732 1z" />
          </svg>
        </div>
        <a class="nav-link active" aria-current="page" href="#">
          Genre Requests
        </a>
      </h6>
      <ul class="nav flex-column mb-3">
        <li class="nav-item" v-for="(value, index) in getPendingGenreReq(pendingGenreReq)">
          <h6 class="d-flex justify-content-between align-items-center mt-2 mb-1">
            <div class="d-flex justify-content-between w-100" v-if="index < 4">
              <div>
                <a class="nav-link" href="#">{{ value.genreReq.genre }}</a>
              </div>
              <div class="d-flex me-1">
                <div class="pe-2 pt-2 approve" @click="approveGenre(value.genreReq_id, index)">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                    class="bi bi-check-circle" viewBox="0 0 16 16">
                    <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z" />
                    <path
                      d="M10.97 4.97a.235.235 0 0 0-.02.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05z" />
                  </svg>
                </div>
                <div class="pe-2 pt-2 reject" @click="rejectGenre(value.genreReq_id, index)">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                    class="bi bi-x-circle" viewBox="0 0 16 16">
                    <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z" />
                    <path
                      d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z" />
                  </svg>
                </div>
              </div>
            </div>
            <a class="nav-link" style="font-size: 0.7em;" href="#" v-else>See all Requests</a>
          </h6>
        </li>
        <li class="nav-item" v-if="pendingGenreReq.length < 1">
          <h6 class="d-flex justify-content-between align-items-center mt-2 mb-1">
            <a class="nav-link" href="#">No Pending Genre Requests</a>
          </h6>
        </li>
      </ul>
      <h6 class="d-flex justify-content-between align-items-center ps-1 mt-4 mb-1">
        <a class="nav-link active" aria-current="page" href="#">Album Flags</a>
      </h6>
      <ul class="nav flex-column mb-2">
        <li class="nav-item" v-for="(value, index) in getPendingAlbumFlagReq(pendingAlbumFlagReq)">
          <div class="d-flex justify-content-between w-100" v-if="index < 4">
            <div>
              <a class="nav-link" href="#">
                {{ value.flag.album_name }}
              </a>
            </div>
            <div class="d-flex me-1">
              <div class="pe-2 pt-2 read" @click="readAlbumFlag(value.flag_id, index)">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                  class="bi bi-check-circle" viewBox="0 0 16 16">
                  <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z" />
                  <path
                    d="M10.97 4.97a.235.235 0 0 0-.02.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05z" />
                </svg>
              </div>
            </div>
          </div>
          <a class="nav-link" style="font-size: 0.7em;" href="#" v-else>
            See all Requests
          </a>
        </li>
        <li class="nav-item" v-if="pendingAlbumFlagReq.length < 1">
          <h6 class="d-flex justify-content-between align-items-center mt-2 mb-1">
            <a class="nav-link" href="#">No Pending AlbumFlag Requests</a>
          </h6>
        </li>
      </ul>
      <h6 class="d-flex justify-content-between align-items-center ps-1 mt-4 mb-1">
        <a class="nav-link active" aria-current="page" href="#">Song Flags</a>
      </h6>
      <ul class="nav flex-column mb-2">
        <li class="nav-item" v-for="(value, index) in getPendingSongFlagReq(pendingSongFlagReq)">
          <div class="d-flex justify-content-between w-100" v-if="index < 4">
            <div>
              <a class="nav-link" :href="generateSongUrl(value.flag.song_id)">
                {{ value.flag.song_name }}
              </a>
            </div>
            <div class="d-flex me-1">
              <div class="pt-2 pe-2 read" @click="readSongFlag(value.flag_id, index)">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                  class="bi bi-check-circle" viewBox="0 0 16 16">
                  <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z" />
                  <path
                    d="M10.97 4.97a.235.235 0 0 0-.02.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05z" />
                </svg>
              </div>
            </div>
          </div>
          <a class="nav-link" style="font-size: 0.7em;" href="#" v-else>
            See all Requests
          </a>
        </li>
        <li class="nav-item" v-if="pendingSongFlagReq.length < 1">
          <h6 class="d-flex justify-content-between align-items-center mt-2 mb-1">
            <a class="nav-link" href="#">No Pending SongFlag Requests</a>
          </h6>
        </li>
      </ul>
    </div>
  </nav>
</template>
<script>
import { onMounted, inject } from 'vue'
export default {
  name: 'AdminSideNav',
  data: function () {
    return {
      pendingGenreReq: [],
      pendingSongFlagReq: [],
      pendingAlbumFlagReq: [],
    }
  },
  async beforeMount() {
    await fetch(__API_URL__ + 'admin/genre', {
      headers: { 'content-type': 'application/json', "Auth-Token": localStorage.getItem("Auth-Token") },
      'method': 'GET'
    }).then(response => response.json())
      .then(data => {
        if (data != "No pending genre creation requests") {
          let res_data = JSON.parse(data);
          if (res_data) {
            for (let genreReq in res_data) {
              this.pendingGenreReq.push({ 'genreReq': res_data[genreReq], genreReq_id: genreReq });
            }
          }
        }
      });
    await fetch(__API_URL__ + 'admin/flags', {
      headers: { 'content-type': 'application/json', "Auth-Token": localStorage.getItem("Auth-Token") },
      'method': 'GET'
    }).then(response => response.json())
      .then(data => {
        if (data != "No pending flags") {
          let res_data = JSON.parse(data);
          if (res_data.albums) {
            for (let flag in res_data.albums) {
              this.pendingAlbumFlagReq.push({ flag: res_data.albums[flag], flag_id: flag });
            }
          }
          if (res_data.songs) {
            for (let flag in res_data.songs) {
              this.pendingSongFlagReq.push({ flag: res_data.songs[flag], flag_id: flag });
            }
          }
        }
      });
  },
  methods: {
    getPendingGenreReq(arr) {
      return arr.slice(0, Math.min(5, arr.length));
    },
    getPendingAlbumFlagReq(arr) {
      return arr.slice(0, Math.min(5, arr.length));
    },
    getPendingSongFlagReq(arr) {
      return arr.slice(0, Math.min(5, arr.length));
    },
    generateSongUrl(sid) {
      return "/song/" + sid;
    },
    async approveGenre(genreReq_id, index) {
      const body = {
        "genre_id": genreReq_id,
        "admin_approval": 'Yes',
      }
      // Yes for accept
      await fetch(__API_URL__ + 'admin/genre', {
        headers: { 'content-type': 'application/json', "Auth-Token": localStorage.getItem("Auth-Token") }, 'body': JSON.stringify(body),
        'method': 'POST'
      }).then(response => response.json())
        .then(data => {
          if (data == "Genre request updated") {
            this.pendingGenreReq.splice(index, 1);
            this.$emit('get-data', { 'key': 'pendingGenreReqLength', 'value' : this.pendingGenreReq.length})
          }
        }).catch((error) => {
          console.error('Error:', error);
        });
    },
    async rejectGenre(genreReq_id, index) {
      const body = {
        "genre_id": genreReq_id,
        "admin_approval": 'No',
      }
      // No for Reject
      await fetch(__API_URL__ + 'admin/genre', {
        headers: { 'content-type': 'application/json', "Auth-Token": localStorage.getItem("Auth-Token") }, 'body': JSON.stringify(body),
        'method': 'POST'
      }).then(response => response.json())
        .then(data => {
          if (data == "Genre request updated") {
            this.pendingGenreReq.splice(index, 1);
            this.$emit('get-data', { 'key': 'pendingGenreReqLength', 'value' : this.pendingGenreReq.length})
          }
        }).catch((error) => {
          console.error('Error:', error);
        });
    },
    async readAlbumFlag(flag_id, index) {
      const body = {
        "flag_type": "album",
        "flag_id": flag_id,
      }
      await fetch(__API_URL__ + 'admin/flags', {
        headers: { 'content-type': 'application/json', "Auth-Token": localStorage.getItem("Auth-Token") }, 'body': JSON.stringify(body),
        'method': 'POST'
      }).then(response => response.json())
        .then(data => {
          if (data == "Flag marked as read") {
            this.pendingAlbumFlagReq.splice(index, 1);
            this.$emit('get-data', { 'key':'pendingAlbumReqLength', 'value': this.pendingAlbumFlagReq.length})
          }
        }).catch((error) => {
          console.error('Error:', error);
        });
    },
    async readSongFlag(flag_id, index) {
      const body = {
        "flag_type": "song",
        "flag_id": flag_id,
      }
      await fetch(__API_URL__ + 'admin/flags', {
        headers: { 'content-type': 'application/json', "Auth-Token": localStorage.getItem("Auth-Token") }, 'body': JSON.stringify(body),
        'method': 'POST'
      }).then(response => response.json())
        .then(data => {
          if (data == "Flag marked as read") {
            this.pendingSongFlagReq.splice(index, 1);
            this.$emit('get-data', { 'key':'pendingSongReqLength', 'value': this.pendingSongFlagReq.length})
          }
        }).catch((error) => {
          console.error('Error:', error);
        });
    },
  }
}
</script>
<style>
.sidebar {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  z-index: 100;
  padding: 48px 0 0;
  box-shadow: inset -1px 0 0 rgba(0, 0, 0, .1);
  overflow-x: hidden;
  overflow-y: auto;
  /* Hide scrollbar for IE, Edge and Firefox */
  -ms-overflow-style: none;
  scrollbar-width: none;
}

/* Hide scrollbar for Chrome, Safari and Opera */
.sidebar::-webkit-scrollbar {
  display: none;
}

@media (max-width: 767.98px) {
  .sidebar {
    top: 5rem;
  }
}

.sidebar-sticky {
  position: relative;
  top: 0;
  height: calc(100vh - 48px);
  padding-top: .5rem;
  overflow-x: hidden;
  overflow-y: hidden;
}

.sidebar .nav-link {
  font-weight: 500;
  color: #fff;
}

.sidebar .nav-link .feather {
  margin-right: 4px;
  color: var(--bp-khaki);
}

.sidebar .nav-link.active {
  color: var(--bp-khaki);
}

.sidebar .nav-link:hover .feather,
.sidebar .nav-link.active .feather {
  color: var(--bp-khaki);
}

.sidebar a:hover {
  color: var(--bp-khaki);
}
</style>