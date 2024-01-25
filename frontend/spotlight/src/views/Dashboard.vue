<template>
  <div>
    <TopNav></TopNav>
    <div class="container-fluid">
      <div class="row">
        <SideNav></SideNav>
        <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
          <div class="container pt-5">
            <h6>New Songs</h6>
            <div class="row g-0 row-cols-auto flex-wrap" v-if="newSongs">
              <SongComponent 
              v-for="(value,key,index) in newSongs"
              :key="index"
              :SongName="value.song_name" 
              :ReleaseDate="value.release_date[0]" 
              :SongDuration="value.duration" 
              :imageSource="value.cover_image" 
              :sid="key" 
              ></SongComponent>
            </div>
            <div class="row g-0 row-cols-auto flex-wrap" v-else>
              <h6 class="d-flex justify-content-between align-items-center mt-2 mb-1">
                <p class="fs-2">There aren't any new songs.</p>
              </h6>
            </div>
          </div>
          <div class="container pt-5">
            <h6>Albums</h6>
            <div class="row g-0 row-cols-auto" v-if="albums">
              <AlbumComponent :AlbumName="value.album_name" :AlbumCreator="value.artists" :imageSource="value.cover_image" v-for="value in albums"></AlbumComponent>
            </div>
            <div class="row g-0 row-cols-auto" v-else>
              <h6 class="d-flex justify-content-between align-items-center mt-2 mb-1">
                <p class="fs-2">There aren't any albums.</p>
              </h6>
            </div>
          </div>
        </main>
      </div>
    </div>
  </div>
</template>
<script>
import SideNav from '@/components/SideNav.vue';
import TopNav from '@/components/TopNav.vue';
import AlbumComponent from '@/components/AlbumComponent.vue';
import SongComponent from '@/components/SongComponent.vue'
export default {
  name: 'Dashboard',
  components: {
    SideNav,
    TopNav,
    AlbumComponent,
    SongComponent
  },
  data: function () {
    return {
      newSongs: null,
      albums: null,
    }
  },
  async beforeMount() {
    await fetch(__API_URL__ + "songs?sort_by=release_date&limit=8", {
      headers: { 'content-type': 'application/json', "Auth-Token": localStorage.getItem("Auth-Token") },
      'method': 'GET'
    })
      .then(response => response.json())
      .then(data => {
        if (data != {}) {
          this.newSongs = data;
        }
      });
      await fetch(__API_URL__ + "albums", {
      headers: { 'content-type': 'application/json', "Auth-Token": localStorage.getItem("Auth-Token") },
      'method': 'GET'
    })
      .then(response => response.json())
      .then(data => {
        if (data != {}) {
          this.albums = JSON.parse(data);
        }
      });
  },
}
</script>
<style></style>