<template>
    <div>
        <TopNav />
        <div class="container-fluid">
            <div class="row">
                <SideNav />
                <main class="me-lg-auto ms-md-auto col-md-8 col-lg-5 px-md-4 pt-5">
                    <div>
                        <h1 style="color:var(--maize);" class="text-center">Create a new Album</h1>
                        <br>
                        <form method="POST" @submit.prevent="handleFormSubmit">
                            <div class="form-floating mb-3">
                                <input type="text" :class='{ "form-control": true, "is-invalid": v$.albumName.$error }'
                                    v-model="albumName" name="albumName" id="floatingInput1" placeholder="album name"
                                    autocomplete="off">
                                <label for="floatingInput1">album name</label>
                                <div class="invalid-feedback" style="color: #dc3545 !important" v-if="v$.albumName.$error">
                                    <span>{{ v$.albumName.$errors[0].$message }}</span>
                                </div>
                            </div>
                            <div class="form-floating mb-3">
                                <input type="text" :class='{ "form-control": true, "is-invalid": v$.artistsNames.$error }'
                                    v-model="artistsNames" name="artistsNames" id="floatingInput2"
                                    placeholder="artists names" autocomplete="off">
                                <label for="floatingInput2">artists names</label>
                                <div class="invalid-feedback" style="color: #dc3545 !important"
                                    v-if="v$.artistsNames.$error">
                                    <span>{{ v$.artistsNames.$errors[0].$message }}</span>
                                </div>
                            </div>
                            <div class="mb-3">
                                <label for="formFile"
                                    :class='{ "form-label": true, "is-invalid": v$.coverImage.$error }'>Upload Album Cover
                                    Image</label>
                                <input class="form-control" type="file" id="formFile"
                                    accept="image/x-png,image/gif,image/jpeg" @:change="onFileChange">
                                <div class="invalid-feedback" style="color: #dc3545 !important" v-if="v$.coverImage.$error">
                                    <span>{{ v$.coverImage.$errors[0].$message }}</span>
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
import { required, helpers } from '@vuelidate/validators'
import { isImage } from '@/utils/Validator';

export default {
    setup() {
        return {
            v$: useVuelidate()
        }
    },
    name: 'CreateAlbum',
    components: {
        SideNav,
        TopNav
    },
    data: function () {
        return {
            albumName: '',
            artistsNames: '',
            coverImage: '',
            errStatus: false,
            errormsg: ''
        }
    },
    validations: {
        albumName: {
            required: helpers.withMessage('The album name field is required', required),
            alphaNum: helpers.withMessage('don\'t include special characters in album names', helpers.regex(/^[a-zA-Z ]*$/))
        },
        artistsNames: {
            required: helpers.withMessage('The artists names are required', required),
            alphaNum: helpers.withMessage('don\'t include special characters in artists names', helpers.regex(/^[a-zA-Z ,]*$/))
        },
        coverImage: {
            required: helpers.withMessage('The cover image is required', required),
            isImage
        }
    },
    methods: {
        handleFormSubmit: async function () {
            this.v$.$touch()
            if (!this.v$.$error) {
                const headers = { 'Auth-Token': localStorage.getItem('Auth-Token') };
                const formdata = new FormData();
                formdata.append("album_name", this.albumName);
                formdata.append("artists_names", this.artistsNames);
                formdata.append("cover_image", this.coverImage, this.coverImage.name);

                await fetch(__API_URL__ + "creator/album/new", {method: 'POST', body: formdata, headers: headers})
                    .then(response => {
                        return response.json();
                    })
                    .then(data => {
                        if (data == 'Album created') {
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
        onFileChange(e) {
            const file = e.target.files[0];
            this.coverImage = file;
        }
    }
}
</script>

<style></style>