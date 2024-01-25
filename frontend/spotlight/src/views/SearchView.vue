<template>
    <TopNav />
    <div class="container-fluid">
        <div class="row">
            <SideNav  v-if="role != 'admin'"/>
            <AdminSideNav v-if="role === 'admin'"/>
            <main class="me-lg-auto ms-md-auto px-md-4 pt-5 main_body">
                <div>
                    <h1 style="color:var(--maize);" class="text-center" v-if="query"> you searched for <br> '{{ query }}'</h1>
                    <h6 class="text-center" v-if="SearchedSongs.length > 0"> Songs are sorted by Rating</h6>
                    <br>
                    <div class="p-3 bg-dark rounded box-shadow" v-if="getSongsLength() >= 1">
                        <div class="media pt-3 d-flex justify-content-between mb-0 pb-3 border-bottom"
                            v-for="value in SearchedSongs">
                            <div class="d-flex justify-content-start">
                                <div class="position-relative SongImgClass">
                                    <img class="mr-2 rounded" :src="getImageUrl(value['cover_image'])"
                                        style="width: 90px; height: 90px;">
                                    <div class="overlayPlay"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 15 15"
                                            width="90" height="70" stroke="var(--bp-yellow)" stroke-width="1"
                                            stroke-linecap="round" fill="var(--bp-yellow)" stroke-linejoin="round"
                                            class="feather feather-home" aria-hidden="true">
                                            <path
                                                d="M6.271 5.055a.5.5 0 0 1 .52.038l3.5 2.5a.5.5 0 0 1 0 .814l-3.5 2.5A.5.5 0 0 1 6 10.5v-5a.5.5 0 0 1 .271-.445z">
                                            </path>
                                        </svg></div>
                                </div>
                                <p class="media-body small lh-125 ms-2 pt-1">
                                    <strong class="d-block pt-1"><a :href="generateSongURL(value['song_id'])">{{ value['song_name'] }}</a></strong>
                                    <strong class="d-block pt-1 text-secondary">Album: {{ value['album_name'] }}</strong>
                                    <strong class="d-block pt-1 text-secondary">Artists: {{ value['artists'] }}</strong>
                                    <strong class="d-block pt-1 text-secondary">Genre: {{ value['genre'] }}</strong>
                                    <strong class="d-block pt-1 text-secondary">Rating: {{ value['rating'] }}</strong>
                                </p>
                            </div>
                        </div>
                    </div>
                    <p class="text-center" v-else> You don't have any songs matching your query.</p>
                </div>
            </main>
        </div>
    </div>
</template>
<script>
import SideNav from '@/components/SideNav.vue';
import TopNav from '@/components/TopNav.vue';
import AdminSideNav from '@/components/AdminSideNav.vue'

export default {
    name: 'SearchView',
    components: {
        SideNav,
        TopNav,
        AdminSideNav
    },
    props: ['query'],
    data: function () {
        return {
            playlistID: this.$route.params.playlistID,
            playlistName: '',
            SearchedSongs: [],
            errormsg: '',
            role: localStorage.getItem('role')
        }
    },
    async beforeMount() {
        const headers = { 'Content-Type': 'application/json', 'Auth-Token': localStorage.getItem('Auth-Token') }
        await fetch(__API_URL__ + "search?query=" + this.query.trim() , { headers: headers, method: "GET" })
            .then(response => {
                if (response.ok) {
                    return response.json();
                }
            })
            .then(data => {
                this.SearchedSongs = data;
            })
            .catch((error) => {
                this.errormsg = error;
                console.log(error)
            })

    },
    methods: {
        getImageUrl(imageUrl) {
            return __BACKEND_URL__ + imageUrl;
        },
        getSongsLength() {
            if (this.SearchedSongs == []) {
                return 0;
            }
            return Object.keys(this.SearchedSongs).length;
        },
        generateSongURL(sid) {
            return '/song/' + sid; 
        }
    }
}
</script>
<style>
.overlayPlay {
    top: 10%;
    left: 0%;
}
</style>