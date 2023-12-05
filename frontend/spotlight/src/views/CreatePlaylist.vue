<template>
    <div>
        <TopNav />
        <div class="container-fluid">
            <div class="row">
                <SideNav />
                <main class="me-lg-auto ms-md-auto col-md-8 col-lg-5 px-md-4 pt-5">
                    <div >
                        <h1 style="color:var(--maize);" class="text-center">Create a new Playlist</h1>
                        <br>
                        <form method="POST" @submit.prevent="handleFormSubmit">
                            <div class="form-floating mb-3">
                                <input type="text" :class='{ "form-control": true, "is-invalid": v$.playlistName.$error }'
                                    v-model="playlistName" name="playlistName" id="floatingInput" placeholder="playlist name"
                                    autocomplete="off">
                                <label for="floatingInput">playlist name</label>
                                <div class="invalid-feedback" style="color: #dc3545 !important" v-if="v$.playlistName.$error">
                                    <span>{{ v$.playlistName.$errors[0].$message }}</span>
                                </div>
                            </div>
                            <button class="w-100 btn btn-lg" type="submit"
                                style="background-color: var(--bp-khaki); color: var(--bp-white);">Create Playlist</button>
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
import { required, alphaNum, helpers } from '@vuelidate/validators'

export default {
    setup() {
        return {
            v$: useVuelidate()
        }
    },
    name: 'CreatePlaylist',
    components: {
        SideNav,
        TopNav
    },
    data: function () {
        return {
            playlistName: '',
            errStatus: false,
            errormsg: ''
        }
    },
    validations: {
        playlistName: {
            required: helpers.withMessage('The playlist name field is required', required),
            alphaNum: helpers.withMessage('The playlist name must contain only letters and numbers', alphaNum),
        },
    },
    methods: {
        handleFormSubmit: async function () {
            this.v$.$touch()
            if (!this.v$.$error) {
                const headers = { 'Content-Type': 'application/json', 'Auth-Token' : localStorage.getItem('Auth-Token') }
                const formdata = { 'playlist_name': this.playlistName }
                await fetch(__API_URL__ + "playlist/new", { headers: headers, body: JSON.stringify(formdata), method: "POST" })
                    .then(response => {
                        return response.json();
                    })
                    .then(data => {
                        if (data == 'Playlist created') {
                            this.errStatus = false;
                            this.$router.push({ name: 'dashboard' })
                        }
                        else {
                            this.errStatus = true;
                            console.log(data.response.errors[0]);
                            throw new Error(data.response.errors[0]);
                        }
                    })
                    .catch((error) => {
                        this.errormsg = error;
                        console.log(error)
                    })
            }
        }
    }
}
</script>

<style></style>