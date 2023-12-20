<template>
  <div>
    <TopNav></TopNav>
    <div class="container-fluid">
      <div class="row">
        <SideNav></SideNav>
        <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
          <div class="container pt-5">
            <h6> Your Stats </h6>
            <CreatorStats :AlbumsCreated="totalCreatorStats[0]" :SongsAdded="totalCreatorStats[1]"
              :SongRatingAvg="avgRating">
            </CreatorStats>
          </div>
          <div class="container pt-5">
            <h6>New Songs</h6>
            <div class="row g-0 row-cols-auto flex-wrap" v-if="newSongs">
              <SongComponent :SongName="value.song_name" :ReleaseDate="value.release_date[0]"
                :SongDuration="value.duration" :imageSource="value.cover_image" v-for="value in newSongs"></SongComponent>
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
              <AlbumComponent :AlbumName="value.album_name" :AlbumCreator="value.artists" :imageSource="value.cover_image"
                v-for="value in albums"></AlbumComponent>
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
import CreatorStats from '@/components/CreatorStats.vue';

export default {
  name: 'CreatorDashboard',
  components: {
    SideNav,
    TopNav,
    AlbumComponent,
    SongComponent,
    CreatorStats,
  },
  data: function () {
    return {
      newSongs: null,
      albums: null,
      creatorAlbums: null,
      avgRating: 0.0,
    }
  },
  async beforeMount() {
    await fetch(__API_URL__ + 'songs?sort_by=release_date&limit=8', {
      headers: { 'content-type': 'application/json', "Auth-Token": localStorage.getItem("Auth-Token") },
      'method': 'GET'
    })
      .then(response => response.json())
      .then(data => {
        if (data != {}) {
          this.newSongs = data;
        }
      });
    await fetch(__API_URL__ + 'albums', {
      headers: { 'content-type': 'application/json', "Auth-Token": localStorage.getItem("Auth-Token") },
      'method': 'GET'
    })
      .then(response => response.json())
      .then(data => {
        if (data != {}) {
          this.albums = JSON.parse(data);
        }
      });
    await fetch(__API_URL__ + 'albums?creator_name=' + localStorage.getItem('username'), {
      headers: { 'content-type': 'application/json', "Auth-Token": localStorage.getItem("Auth-Token") },
      'method': 'GET'
    })
      .then(response => response.json())
      .then(data => {
        if (data != {}) {
          if (data == 'No albums found') { this.creatorAlbums = null; }
          else { this.creatorAlbums = JSON.parse(data); }
        }
      });
    await fetch(__API_URL__ + 'creator/' + localStorage.getItem('username') + '/rating', {
      headers: { 'content-type': 'application/json', "Auth-Token": localStorage.getItem("Auth-Token") },
      'method': 'GET'
    }).then(response => response.json())
      .then(data => {
        if (data != {}) {
          this.avgRating = parseFloat(data.toFixed(2));
        }
      });
  },
  computed: {
    totalCreatorStats() {
      let objectSize = 0;
      let totalSongs = 0;
      for (let key in this.creatorAlbums) {
        objectSize++;
        totalSongs += this.creatorAlbums[key].no_of_songs;
      }
      return [objectSize, totalSongs];
    }
  }
}
</script>
<style></style>