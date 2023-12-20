<template>
    <div>
        <TopNav></TopNav>
        <div class="container-fluid">
            <div class="row">
                <SideNav></SideNav>
                <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
                    <div class="container pt-5">
                        <img :src="cover_image" class="img-fluid" alt="Responsive image" width="200" height="200">
                        <h6 class="pt-2"> Song Name </h6>
                        <strong>{{ name }}</strong>
                        <h6 class="pt-2"> Album Name </h6>
                        <strong>{{ album_name }}</strong>
                        <h6 class="pt-2"> Song Genres </h6>
                        <strong v-for="genre in genres">{{ genre }}, </strong>
                        <h6 class="pt-2"> Song Artists </h6>
                        <strong>{{ artists_names }} </strong>
                        <h6 class="pt-2"> Song </h6>
                        <audio controls class="pt-2" id="songAudio">
                            <source :src="song_url" type="audio/mpeg">
                        </audio>
                        <h6 class="pt-2"> Song Lyrics </h6>
                        {{ lyrics_content }}
                    </div>
                </main>
            </div>
        </div>
    </div>
</template>

<script>
import SideNav from '@/components/SideNav.vue';
import TopNav from '@/components/TopNav.vue';

export default {
    name: 'CreatorDashboard',
    components: {
        SideNav,
        TopNav,
    },
    data: function () {
        return {
            songID: this.$route.params.songID,
            name: '',
            album_name: '',
            artists_names: '',
            song_url: '',
            cover_image: '',
            lyrics_content: '',
            lyrics: '',
            // rating: '',
            duration: '',
            release_date: '',
            genres: ''
        }
    },
    async beforeMount() {
        const headers = { 'Content-Type': 'application/json', 'Auth-Token': localStorage.getItem('Auth-Token') }
        await fetch(__API_URL__ + "play/song/" + this.$route.params.songID, { headers: headers, 'method': 'GET' })
            .then(response => {
                return response.json();
            })
            .then(async data => {
                this.name = data.name;
                this.album_name = data.album_name;
                this.artists_names = data.artists_names;
                this.song_url = __BACKEND_URL__ + data.song_url;
                this.cover_image = __BACKEND_URL__ + data.cover_image;
                this.lyrics = __BACKEND_URL__ + data.lyrics_url;
                await fetch(this.lyrics, { headers: headers, 'method': 'GET' })
                    .then(response => {
                        return response.text();
                    })
                    .then(data => {
                        this.lyrics_content = data;
                    })
                    .catch((error) => {
                        console.log(error)
                    });
                // this.rating = data.rating;
                this.duration = data.duration;
                this.release_date = data.release_date;
                this.genres = data.genres;
            })
            .catch((error) => {
                console.log(error)
            })
        document.getElementById('songAudio').load();
    },
}

</script>

<style></style>