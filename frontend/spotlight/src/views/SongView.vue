<template>
    <div>
        <TopNav></TopNav>
        <div class="container-fluid">
            <div class="row">
                <SideNav></SideNav>
                <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
                    {{ lyrics_content }}

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
            name: '',
            album_name: '',
            artists_names: '',
            song_url: '',
            cover_image: '',
            lyrics_content: '',
            lyrics: '',
            rating: '',
            duration: '',
            release_date: '',
            genres: ''
        }
    },
    async beforeMount() {
        const headers = { 'Content-Type': 'application/json', 'Auth-Token': localStorage.getItem('Auth-Token') }
        await fetch(__API_URL__ + "play/song/12", { headers: headers, 'method': 'GET' })
            .then(response => {
                return response.json();
            })
            .then(async data => {
                this.name = data.name;
                this.album_name = data.album_name;
                this.artists_names = data.artists_names;
                this.song_url = data.song_url;
                this.cover_image = data.cover_image;
                this.lyrics = __BACKEND_URL__ + data.lyrics_url;
                await fetch( this.lyrics, { headers: headers, 'method': 'GET' })
                    .then(response => {
                        return response.text();
                    })
                    .then(data => {
                        this.lyrics_content = data;
                    })
                    .catch((error) => {
                        console.log(error)
                    });
                this.rating = data.rating;
                this.duration = data.duration;
                this.release_date = data.release_date;
                this.genres = data.genres;
            })
            .catch((error) => {
                console.log(error)
            })
    }
}

</script>

<style></style>