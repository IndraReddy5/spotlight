<template>
    <TopNav />
    <div class="container-fluid">
        <div class="row">
            <SideNav />
            <main class="me-lg-auto ms-md-auto px-md-4 pt-5 main_body">
                <div>
                    <h1 style="color:var(--maize);" class="text-center"> {{ playlistName }}</h1>
                    <br>
                    <div class="p-3 bg-dark rounded box-shadow" v-if="getPlaylistSongsLength() >= 1">
                        <div class="media pt-3 d-flex justify-content-between mb-0 pb-3 border-bottom"
                            v-for="value in playlistSongs">
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
                                </p>
                            </div>
                            <div>
                                <a class="link-secondary" aria-label="delete this song from playlist"
                                    @click="RemoveSongPlaylist(value['song_id'])" style="cursor: pointer; float: 10%;">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="none"
                                        stroke="var(--bp-khaki)" stroke-width="0.8" class="bi bi-trash" viewBox="0 0 24 22">
                                        <path
                                            d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0z" />
                                        <path
                                            d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4zM2.5 3h11V2h-11z" />
                                    </svg>
                                </a>
                            </div>
                        </div>
                    </div>
                    <p class="text-center" v-else> You don't have any songs in this playlist.</p>
                </div>
            </main>
        </div>
    </div>
</template>
<script>
import SideNav from '@/components/SideNav.vue';
import TopNav from '@/components/TopNav.vue';

export default {
    name: 'PlaylistView',
    components: {
        SideNav,
        TopNav
    },
    data: function () {
        return {
            playlistID: this.$route.params.playlistID,
            playlistName: '',
            playlistSongs: [],
            errormsg: '',
        }
    },
    async beforeMount() {
        const headers = { 'Content-Type': 'application/json', 'Auth-Token': localStorage.getItem('Auth-Token') }
        await fetch(__API_URL__ + "playlist/" + this.playlistID + "/songs", { headers: headers, method: "GET" })
            .then(response => {
                if (response.ok) {
                    return response.json();
                }
                else {
                    alert("You don't have access to this playlist, redirecting you to dashboard");
                    this.$router.push({ name: 'dashboard' })
                }
            })
            .then(data => {
                this.playlistName = JSON.parse(data)['playlist_name'];
                this.playlistSongs = JSON.parse(data)['songs'];
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
        getPlaylistSongsLength() {
            if (this.playlistSongs == []) {
                return 0;
            }
            return Object.keys(this.playlistSongs).length;
        },
        async RemoveSongPlaylist(sid) {
            const headers = { 'Content-Type': 'application/json', 'Auth-Token': localStorage.getItem('Auth-Token') }
            await fetch(__API_URL__ + 'playlist/' + this.$route.params.playlistID + '/remove/' + sid, { headers: headers, 'method': 'DELETE' })
                .then(response => { return response.json(); })
                .then(data => { if (data === "Song removed from playlist") { console.log(data); alert("Song removed from playlist"); location.reload(); } })
                .catch((error) => {
                    console.log(error);
                    alert("There's some issue while removing the song from playlist, try again later, if issue persists contact admin")
                })
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