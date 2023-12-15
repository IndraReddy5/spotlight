<template>
    <div>
        <TopNav />
        <div class="container-fluid">
            <div class="row">
                <SideNav />
                <main class="me-lg-auto ms-md-auto col-md-8 col-lg-5 px-md-4 pt-5">
                    <div >
                        <h1 style="color:var(--maize);" class="text-center">Request a new Genre</h1>
                        <br>
                        <form method="POST" @submit.prevent="handleFormSubmit">
                            <div class="form-floating mb-3">
                                <input type="text" :class='{ "form-control": true, "is-invalid": v$.genreName.$error }'
                                    v-model="genreName" name="genreName" id="floatingInput" placeholder="genre name"
                                    autocomplete="off">
                                <label for="floatingInput">genre name</label>
                                <div class="invalid-feedback" style="color: #dc3545 !important" v-if="v$.genreName.$error">
                                    <span>{{ v$.genreName.$errors[0].$message }}</span>
                                </div>
                            </div>
                            <button class="w-100 btn btn-lg" type="submit"
                                style="background-color: var(--bp-khaki); color: var(--bp-white);">Req Genre</button>
                            <hr class="my-4">
                            <div class="alert alert-danger alert-dismissible fade show" role="alert" v-if="errStatus">
                                <strong>{{ errormsg }}</strong>.
                                <button type="button" class="btn-close" aria-label="Close"
                                    @click="errStatus = false"></button>
                            </div>
                        </form>
                    </div>
                    <div v-if="genres.length > 1">
                        <p> These are all the genres you've requested until now</p>
                        <table class="table table-dark">
                            <thead>
                                <tr>
                                    <th scope="col">Genre</th>
                                    <th scope="col">Status</th>
                                </tr>
                            </thead>
                            <tbody class="table-group-divider">
                                <tr scope="row" v-for="genre in genres">
                                    <td>{{ genre[0] }}</td>
                                    <td>{{ genre[1] }}</td>
                                </tr>
                            </tbody>
                        </table>
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
    name: 'GenreRequest',
    components: {
        SideNav,
        TopNav
    },
    data: function () {
        return {
            genreName: '',
            errStatus: false,
            errormsg: '',
            genres: []
        }
    },
    beforeMount() {
        const headers = { 'Content-Type': 'application/json', 'Auth-Token' : localStorage.getItem('Auth-Token') }
        fetch(__API_URL__ + "genre?req_by=" + localStorage.getItem('username'), { headers: headers })
            .then(response => {
                return response.json();
            })
            .then(data => {
                this.genres = data;
            })
            .catch((error) => {
                console.log(error)
            })
    },
    validations: {
        genreName: {
            required: helpers.withMessage('The playlist name field is required', required),
            alphaNum: helpers.withMessage('The playlist name must contain only letters and numbers', alphaNum),
        },
    },
    methods: {
        handleFormSubmit: async function () {
            this.v$.$touch()
            if (!this.v$.$error) {
                const headers = { 'Content-Type': 'application/json', 'Auth-Token' : localStorage.getItem('Auth-Token') }
                const formdata = { 'genre': this.genreName }
                await fetch(__API_URL__ + "creator/genre/new", { headers: headers, body: JSON.stringify(formdata), method: "POST" })
                    .then(response => {
                        return response.json();
                    })
                    .then(data => {
                        if (data == 'Genre request created') {
                            this.errStatus = false;
                            this.$router.push({ name: 'dashboard' })
                        }
                        else {
                            this.errStatus = true;
                            console.log(data.error_message);
                            throw new Error(data.error_message);
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