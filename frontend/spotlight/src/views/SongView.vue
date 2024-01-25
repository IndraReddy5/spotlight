<template>
    <div>
        <TopNav></TopNav>
        <div class="container-fluid">
            <div class="row">

                <AdminSideNav v-if="role == 'admin'"></AdminSideNav>
                <SideNav v-else></SideNav>
                <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
                    <div class="container pt-5">
                        <img :src="cover_image" class="img-fluid" alt="Responsive image" width="200" height="200">
                        <div class="d-flex justify-content-between">
                            <h6 class="pt-2"> Song Name : {{ name }} </h6>
                            <div class="align-bottom">
                                <a class="link-secondary" @click="AddToPlaylistFlag" aria-label="Add song to playlist"
                                    style="cursor: pointer;" v-if="role != 'admin'">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 24 30"
                                        fill="none" stroke="var(--bp-khaki)" stroke-width="3" stroke-linecap="round"
                                        stroke-linejoin="round" class="feather feather-plus-circle" aria-hidden="true">
                                        <line x1="12" y1="8" x2="12" y2="16"></line>
                                        <line x1="8" y1="12" x2="16" y2="12"></line>
                                    </svg>
                                </a>
                                <a class="link-secondary" @click="FlagSongModify" aria-label="Flag this song"
                                    style="cursor: pointer;" v-if="role != 'admin'">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="none"
                                        class="bi bi-bookmarks" stroke="var(--bp-khaki)" stroke-width="1"
                                        stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"
                                        aria-hidden="true">
                                        <path
                                            d="M2 4a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v11.5a.5.5 0 0 1-.777.416L7 13.101l-4.223 2.815A.5.5 0 0 1 2 15.5V4zm2-1a1 1 0 0 0-1 1v10.566l3.723-2.482a.5.5 0 0 1 .554 0L11 14.566V4a1 1 0 0 0-1-1H4z" />
                                    </svg>
                                </a>
                                <a class="link-secondary" @click="ratingFlagModify" aria-label="Rate this song"
                                    style="cursor: pointer;" v-if="role != 'admin'">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="none"
                                        stroke="var(--bp-khaki)" stroke-width="1" class="bi bi-star" viewBox="0 0 24 24">
                                        <path
                                            d="M2.866 14.85c-.078.444.36.791.746.593l4.39-2.256 4.389 2.256c.386.198.824-.149.746-.592l-.83-4.73 3.522-3.356c.33-.314.16-.888-.282-.95l-4.898-.696L8.465.792a.513.513 0 0 0-.927 0L5.354 5.12l-4.898.696c-.441.062-.612.636-.283.95l3.523 3.356-.83 4.73zm4.905-2.767-3.686 1.894.694-3.957a.56.56 0 0 0-.163-.505L1.71 6.745l4.052-.576a.53.53 0 0 0 .393-.288L8 2.223l1.847 3.658a.53.53 0 0 0 .393.288l4.052.575-2.906 2.77a.56.56 0 0 0-.163.506l.694 3.957-3.686-1.894a.5.5 0 0 0-.461 0z" />
                                    </svg>
                                </a>
                                <a class="link-secondary" @click="DeleteSong" aria-label="delete this song"
                                    v-if="delete_flag || role == 'admin'" style="cursor: pointer;">
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
                        <div v-if="flag_song_visiblility">
                            <h6> Reason for flag </h6>
                            <form @submit.prevent="FlagSong">
                                <input type="text" v-model="flag_reason" placeholder="flag reason" name="flagReason"
                                    autocomplete="off">
                                <button class="btn-3 ms-2" type="submit" role="submit">flag the song</button>
                            </form>
                        </div>
                        <div v-if="rating_flag_visiblility">
                            <h6> Rate the song </h6>
                            <form @submit.prevent="RateSong">
                                <select v-model="user_rating" class="form-floating mb-3" required>
                                    <option value=1>1</option>
                                    <option value=2>2</option>
                                    <option value=3>3</option>
                                    <option value=4>4</option>
                                    <option value=5>5</option>
                                </select>
                                <button class="btn-3 ms-2" type="submit" role="submit">Submit
                                    Rating</button>
                            </form>
                        </div>
                        <div v-if="add_to_playlist_visibility">
                            <h6>select playlist name</h6>
                            <form @submit.prevent="AddToPlaylist">
                                <select v-model="AddToPlaylistID" required>
                                    <option :value="key" v-for="obj, key, index in playlists">{{ obj.playlist_name }}
                                    </option>
                                </select>
                                <button class="btn-3 ms-2" role="submit" type="submit">Add to Playlist</button>
                            </form>
                        </div>
                        <h6 class="pt-2"> Album Name : {{ album_name }} </h6>
                        <h6 class="pt-2" v-if=genres.length> Song Genres : <strong v-for="genre in genres">{{ genre }},
                            </strong> </h6>
                        <h6 class="pt-2"> Song Artists : {{ artists_names }} </h6>
                        <h6 class="pt-2" v-if="rating > 0"> Average Rating : {{ rating }} </h6>
                        <h6 class="pt-2"> Song : </h6>
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
import AdminSideNav from '@/components/AdminSideNav.vue';
import TopNav from '@/components/TopNav.vue';

export default {
    name: 'SongView',
    components: {
        SideNav,
        TopNav,
        AdminSideNav,
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
            rating: '',
            duration: '',
            release_date: '',
            genres: '',
            role: localStorage.getItem('role'),
            delete_flag: false,
            flag_song_visiblility: false,
            flag_reason: '',
            rating_flag_visiblility: false,
            user_rating: 0,
            add_to_playlist_visibility: false,
            AddToPlaylistID: null,
            playlists: [],
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
                this.rating = data.rating,
                    await fetch(this.lyrics, { headers: headers, 'method': 'GET' })
                        .then(response => {
                            return response.text();
                        })
                        .then(data => {
                            this.lyrics_content = data;
                        })
                        .catch((error) => {
                            console.log(error);
                        });
                // this.rating = data.rating;
                this.duration = data.duration;
                this.release_date = data.release_date;
                this.genres = data.genres;
            })
            .catch((error) => {
                console.log(error);
                alert("song not found, redirecting to dashboard");
                this.$router.push("/dashboard")

            })
        if (this.role === "creator") {
            let creator_albums = [];
            await fetch(__API_URL__ + 'albums?creator_name=' + localStorage.getItem("username"), { headers: headers, 'method': 'GET' })
                .then(response => { return response.json() })
                .then(data => {
                    let res = JSON.parse(data);
                    for (const obj in res) { creator_albums.push(res[obj].album_name) }
                })
            if (creator_albums.includes(this.album_name)) { this.delete_flag = true; }
        }
        if (this.role != 'admin') {
            await fetch(__API_URL__ + 'user/' + localStorage.getItem('username') + '/playlists', {
                headers: { 'content-type': 'application/json', "Auth-Token": localStorage.getItem("Auth-Token") },
                'method': 'GET'
            })
                .then(response => response.json())
                .then(data => {
                    if (data === 'No playlists found') {
                        this.playlists = null;
                    }
                    else {
                        this.playlists = JSON.parse(data);
                    }
                });
        }
        document.getElementById('songAudio').load();
    },
    methods: {
        async DeleteSong() {
            const headers = { 'Content-Type': 'application/json', 'Auth-Token': localStorage.getItem('Auth-Token') }
            if (this.role === "admin" || this.delete_flag) {
                await fetch(__API_URL__ + 'remove/song/' + this.$route.params.songID, { headers: headers, 'method': 'DELETE' })
                    .then(response => { return response.json(); })
                    .then(data => { if (data === "Song removed") { console.log(data); this.$router.push('/dashboard') } })
                    .catch((error) => {
                        console.log(error);
                        alert("song can't be deleted, try again later, if issue persists contact admin")
                    })
            }
        },
        async FlagSongModify() {
            if (this.flag_song_visiblility) {
                this.flag_song_visiblility = false;
            }
            else {
                this.flag_song_visiblility = true;
            }
        },
        async ratingFlagModify() {
            if (this.rating_flag_visiblility) {
                this.rating_flag_visiblility = false;
            }
            else {
                this.rating_flag_visiblility = true;
            }
        },
        async AddToPlaylistFlag() {
            if (this.add_to_playlist_visibility) {
                this.add_to_playlist_visibility = false;
            }
            else {
                this.add_to_playlist_visibility = true;
            }
        },
        async FlagSong() {
            const headers = { 'Content-Type': 'application/json', 'Auth-Token': localStorage.getItem('Auth-Token') }
            const body_data = { 'reason': this.flag_reason }
            await fetch(__API_URL__ + 'flag/song/' + this.$route.params.songID, { headers: headers, body: JSON.stringify(body_data), 'method': 'POST' })
                .then(response => { return response.json(); })
                .then(data => { if (data === "Song flagged") { console.log(data); alert("Song flagged, admin will review it soon") } })
                .catch((error) => {
                    console.log(error);
                    alert("song can't be flagged, try again later, if issue persists contact admin")
                })

        },
        async RateSong() {
            const headers = { 'Content-Type': 'application/json', 'Auth-Token': localStorage.getItem('Auth-Token') }
            const body_data = { 'rating': this.user_rating }
            await fetch(__API_URL__ + 'song/' + this.$route.params.songID + '/rating', { headers: headers, body: JSON.stringify(body_data), 'method': 'PUT' })
                .then(response => { return response.json(); })
                .then(data => { if (data === "Thank you for giving feedback on the song") { console.log(data); alert("Thank you for giving feedback on the song") } })
                .catch((error) => {
                    console.log(error);
                    alert("There's some issue while rating the song, try again later, if issue persists contact admin")
                })

        },
        async AddToPlaylist() {
            const headers = { 'Content-Type': 'application/json', 'Auth-Token': localStorage.getItem('Auth-Token') }
            await fetch(__API_URL__ + 'playlist/' + this.AddToPlaylistID + '/add/' + this.$route.params.songID, { headers: headers, 'method': 'POST' })
                .then(response => { return response.json(); })
                .then(data => { if (data === "Song added to playlist") { console.log(data); alert("Song added to playlist") } })
                .catch((error) => {
                    console.log(error);
                    alert("There's some issue while adding the song to playlist, try again later, if issue persists contact admin")
                })
        }
    }
}

</script>

<style></style>