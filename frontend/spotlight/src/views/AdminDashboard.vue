<template>
    <div>
        <TopNav></TopNav>
        <div class="container-fluid">
            <div class="row">
                <SideNav></SideNav>
                <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
                    <canvas class="my-4 w-100" id="myChart" width="1351" height="570"
                        style="display: block; box-sizing: border-box; height: 380px; width: 900px;"></canvas>
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
    name: 'AdminDashboard',
    components: {
        SideNav,
        TopNav,
        AlbumComponent,
        SongComponent,
        CreatorStats,
    }
}
</script>
<style></style>