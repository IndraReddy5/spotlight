<template>
    <div>
        <TopNav />
        <div class="container-fluid">
            <div class="row">
                <SideNav />
                <main class="me-lg-auto ms-md-auto col-md-8 col-lg-5 px-md-4 pt-5">
                    <div>
                        <h1 style="color:var(--maize);" class="text-center">Create a new Song</h1>
                        <br>
                        <form method="POST" @submit.prevent="handleFormSubmit">
                            <div class="form-floating mb-3">
                                <input type="text" :class='{ "form-control": true, "is-invalid": v$.songName.$error }'
                                    v-model="songName" name="songName" id="floatingInput1" placeholder="song name"
                                    autocomplete="off">
                                <label for="floatingInput1">song name</label>
                                <div class="invalid-feedback" style="color: #dc3545 !important" v-if="v$.songName.$error">
                                    <span>{{ v$.songName.$errors[0].$message }}</span>
                                </div>
                            </div>
                            <div class="form-floating mb-3">
                                <input type="text" :class='{ "form-control": true, "is-invalid": v$.duration.$error }'
                                    v-model="duration" name="duration" id="floatingInput1" placeholder="duration of song in seconds"
                                    autocomplete="off">
                                <label for="floatingInput1">duration of song in seconds</label>
                                <div class="invalid-feedback" style="color: #dc3545 !important" v-if="v$.duration.$error">
                                    <span>{{ v$.duration.$errors[0].$message }}</span>
                                </div>
                            </div>
                            <div class="form-floating mb-3">
                                <select v-model="albumID">
                                    <!-- inline object literal -->
                                    <option value="" disabled selected>Select Album</option>
                                    <option :value="key" v-for="album, key, index in creatorAlbums">{{ album.album_name }}
                                    </option>
                                </select>
                            </div>
                            <div class="mb-3">
                                <label for="formFile" :class='{ "form-label": true, "is-invalid": v$.lyrics.$error }'>Upload
                                    lyrics file
                                </label>
                                <input class="form-control" type="file" id="formFile" accept=".txt"
                                    @:change="onTextFileChange">
                                <div class="invalid-feedback" style="color: #dc3545 !important" v-if="v$.lyrics.$error">
                                    <span>{{ v$.lyrics.$errors[0].$message }}</span>
                                </div>
                            </div>
                            <div class="mb-3">
                                <label for="formFile"
                                    :class='{ "form-label": true, "is-invalid": v$.coverImage.$error }'>Upload Song Cover
                                    Image</label>
                                <input class="form-control" type="file" id="formFile"
                                    accept="image/x-png,image/gif,image/jpeg" @:change="onImageFileChange">
                                <div class="invalid-feedback" style="color: #dc3545 !important" v-if="v$.coverImage.$error">
                                    <span>{{ v$.coverImage.$errors[0].$message }}</span>
                                </div>
                            </div>
                            <div class="mb-3">
                                <label for="formFile"
                                    :class='{ "form-label": true, "is-invalid": v$.songFile.$error }'>Upload Song File
                                </label>
                                <input class="form-control" type="file" id="formFile" accept="audio/mpeg"
                                    @:change="onSongFileChange">
                                <div class="invalid-feedback" style="color: #dc3545 !important" v-if="v$.songFile.$error">
                                    <span>{{ v$.songFile.$errors[0].$message }}</span>
                                </div>
                            </div>
                            <button class="w-100 btn btn-lg" type="submit"
                                style="background-color: var(--bp-khaki); color: var(--bp-white);">Create Album</button>
                            <hr class="my-4">
                            <div class="alert alert-danger alert-dismissible fade show" role="alert" v-if="errStatus">
                                <strong>{{ errormsg }}</strong>.
                                <button type="button" class="btn-close" aria-label="Close"
                                    @click="errStatus = false"></button>
                            </div>
                        </form>
                    </div>
                </main>
            </div>
        </div>
    </div>
</template>

<script>
import SideNav from '@/components/SideNav.vue';
import TopNav from '@/components/TopNav.vue';
import { useVuelidate } from '@vuelidate/core'
import { required, helpers, numeric } from '@vuelidate/validators'
import { isImage, isText, isAudio } from '@/utils/Validator';

export default {
    setup() {
        return {
            v$: useVuelidate()
        }
    },
    name: 'AddSong',
    components: {
        SideNav,
        TopNav
    },
    data: function () {
        return {
            creatorAlbums: '',
            duration: '',
            songName: '',
            albumID: '',
            coverImage: '',
            songFile: '',
            lyrics: '',
            errStatus: false,
            errormsg: ''
        }
    },
    validations: {
        songName: {
            required: helpers.withMessage('The album name field is required', required),
            alphaNum: helpers.withMessage('don\'t include special characters in album names', helpers.regex(/^[a-zA-Z ]*$/))
        },
        duration: {
            required: helpers.withMessage('The duration field is required', required),
            numeric: helpers.withMessage('The duration field must be only in seconds', helpers.regex(/^[0-9]*$/))
        },
        albumID: {
            required: helpers.withMessage('The album id is required', required),
        },
        coverImage: {
            isImage
        },
        lyrics: {
            isText,
            required: helpers.withMessage('The lyrics file is required', required),
        },
        songFile: {
            isAudio,
            required: helpers.withMessage('The song file is required', required),
        }
    },
    async beforeMount() {
        await fetch(__API_URL__ + 'albums?creator_name=' + localStorage.getItem('username'), {
            headers: { 'content-type': 'application/json', "Auth-Token": localStorage.getItem("Auth-Token") },
            'method': 'GET'
        })
            .then(response => response.json())
            .then(data => {
                if (data != {}) {
                    if (data == "No albums found") { alert("create a album first"), this.$router.push({ name: 'newAlbum' }) }
                    else
                        this.creatorAlbums = JSON.parse(data);
                }
            });
    },
    methods: {
        handleFormSubmit: async function () {
            this.v$.$touch()
            if (!this.v$.$error) {
                const headers = { 'Auth-Token': localStorage.getItem('Auth-Token') };
                const formdata = new FormData();
                formdata.append("album_id", this.albumID);
                formdata.append("song_name", this.songName);
                if (this.coverImage != '') { formdata.append("cover_image", this.coverImage, this.coverImage.name); }
                formdata.append("lyrics_file", this.lyrics, this.lyrics.name);
                formdata.append("audio_file", this.songFile, this.songFile.name)


                await fetch(__API_URL__ + "creator/song/new", { method: 'POST', body: formdata, headers: headers })
                    .then(response => {
                        return response.json();
                    })
                    .then(data => {
                        if (data == 'Song created') {
                            this.errStatus = false;
                            this.$router.push({ name: 'dashboard' })
                        }
                        else {
                            this.errStatus = true;
                            throw new Error(data.response.errors[0]);
                        }
                    })
                    .catch((error) => {
                        this.errormsg = error;
                        console.log(error)
                    })
            }
        },
        onImageFileChange(e) {
            const file = e.target.files[0];
            this.coverImage = file;
        },
        onTextFileChange(e) {
            const file = e.target.files[0];
            this.lyrics = file;
        },
        onSongFileChange(e) {
            const file = e.target.files[0];
            this.songFile = file;
        }
    }
}
</script>

<style></style>