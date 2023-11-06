<template>
  <div>
    <TopNav></TopNav>
    <div class="container-fluid">
      <div class="row">
        <SideNav></SideNav>
        <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
          <div class="container pt-5">
            <h6>New Songs</h6>
            <div class="row g-0 row-cols-auto flex-wrap">
              <SongComponent SongName="Comethru" ReleaseDate="15-4-2023" :SongDuration="246"></SongComponent>
              <SongComponent SongName="Comethru" ReleaseDate="15-4-2023" :SongDuration="246"></SongComponent>
              <SongComponent SongName="Comethru" ReleaseDate="15-4-2023" :SongDuration="246"></SongComponent>
              <SongComponent SongName="Comethru" ReleaseDate="15-4-2023" :SongDuration="246"></SongComponent>
              <SongComponent SongName="Comethru" ReleaseDate="15-4-2023" :SongDuration="246"></SongComponent>
              <SongComponent SongName="Comethru" ReleaseDate="15-4-2023" :SongDuration="246"></SongComponent>
              <SongComponent SongName="Comethru" ReleaseDate="15-4-2023" :SongDuration="246"></SongComponent>
              <SongComponent SongName="Comethru" ReleaseDate="15-4-2023" :SongDuration="246"></SongComponent>
            </div>
          </div>
          <div class="container pt-5">
            <h6>Albums</h6>
            <div class="row g-0 row-cols-auto">
              <AlbumComponent AlbumName="Comethru" AlbumCreator="Jeremy Zucker"></AlbumComponent>
              <AlbumComponent AlbumName="Comethru" AlbumCreator="Jeremy Zucker"></AlbumComponent>
              <AlbumComponent AlbumName="Comethru" AlbumCreator="Jeremy Zucker"></AlbumComponent>
              <AlbumComponent AlbumName="Comethru" AlbumCreator="Jeremy Zucker"></AlbumComponent>
              <AlbumComponent AlbumName="Comethru" AlbumCreator="Jeremy Zucker"></AlbumComponent>
              <AlbumComponent AlbumName="Comethru" AlbumCreator="Jeremy Zucker"></AlbumComponent>
              <AlbumComponent AlbumName="Comethru" AlbumCreator="Jeremy Zucker"></AlbumComponent>
              <AlbumComponent AlbumName="Comethru" AlbumCreator="Jeremy Zucker"></AlbumComponent>
              <AlbumComponent AlbumName="Comethru" AlbumCreator="Jeremy Zucker"></AlbumComponent>
              <AlbumComponent AlbumName="Comethru" AlbumCreator="Jeremy Zucker"></AlbumComponent>
              <AlbumComponent AlbumName="Comethru" AlbumCreator="Jeremy Zucker"></AlbumComponent>
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
  }
}
</script>
<style>

</style>