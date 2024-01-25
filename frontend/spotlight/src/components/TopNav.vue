<template>
    <header class="navbar navbar-dark sticky-top bg-dark flex-md-nowrap p-0 shadow">
        <a class="navbar-brand col-md-3 col-lg-2 me-0 px-3 fs-4" href="/dashboard">Spotlight</a>
        <button class="navbar-toggler d-md-none collapsed" type="button" data-bs-toggle="collapse"
            data-bs-target="#sidebarMenu" aria-controls="sidebarMenu" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <input name="search" class="form-control form-control-dark w-100" type="text" placeholder="Search by artist name / genre or just click enter here to view all songs"
            aria-label="Search" v-model="query" @keyup.enter="SearchFor">
        <div class="navbar-nav topnav_user">
            <div class="nav-item text-nowrap">
                <!-- <a class="nav-link px-3" href="#">Sign out</a> -->
                <div class="dropdown px-3 float-end">
                    <a href="#" class="d-flex align-items-center text-white text-decoration-none dropdown-toggle"
                        id="dropdownUser" data-bs-toggle="dropdown" aria-expanded="false">
                        <strong>{{ username }}</strong>
                    </a>
                    <ul class="dropdown-menu dropdown-menu-dark text-small shadow" aria-labelledby="dropdownUser"
                        data-popper-placement="bottom-end"
                        style="position: absolute; inset: 0px auto auto 0px; margin: 0px; transform: translate3d(-119px, 34px, 0px);">
                        <div v-if="role == 'melophile'">
                            <li><a class="dropdown-item" @click="newPatron()">Sign up as Patron</a></li>
                        </div>
                        <div v-if="role == 'patron' || role == 'melophile'">
                            <li><a class="dropdown-item" @click="newCreator()">Sign up as Creator</a></li>
                        </div>
                        <div v-if="role == 'creator'">
                            <li><a class="dropdown-item" href="/album/new">New Album</a></li>
                            <li><a class="dropdown-item" href="/genre/new">Request New Genre</a></li>
                            <li><a class="dropdown-item" href="/song/new">Upload a song</a></li>
                            <!-- Add a separate page to see profile page where all playlists and all reviews by user are displayed, maybe in second version of the app-->
                            <!-- <li><a class="dropdown-item" href="#">Profile</a></li> -->
                            <li>
                                <hr class="dropdown-divider">
                            </li>
                        </div>
                        <router-link to="/logout" class="dropdown-item">logout</router-link>
                    </ul>
                </div>
            </div>
        </div>
    </header>
</template>
<script>
export default {
    name: 'TopNav',
    data: function () {
        return {
            username: localStorage.getItem("username"),
            role: localStorage.getItem("role"),
            query: "",
        }
    },
    methods: {
        async newCreator() {
            const headers = { 'Content-Type': 'application/json', 'Auth-Token': localStorage.getItem('Auth-Token') }
            await fetch(__API_URL__ + "creator/signup/" + localStorage.getItem("username"), { headers: headers, method: "POST" })
                .then(response => {
                    return response.json();
                })
                .then(data => {
                    if (data == 'Time to shine on Spotlight with your creations') {
                        localStorage.setItem("role", "creator");
                        alert("You are now a creator, you can see your new dashboard now")
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
        },
        async newPatron() {
            const headers = { 'Content-Type': 'application/json', 'Auth-Token': localStorage.getItem('Auth-Token') }
            await fetch(__API_URL__ + "patron/" + localStorage.getItem("username") + "/subscribe", { headers: headers, method: "POST" })
                .then(response => {
                    return response.json();
                })
                .then(data => {
                    if (data == 'You are now a patron') {
                        localStorage.setItem("role", "patron");
                        alert("You are now a patron, redirecting you back to dashboard")
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
        },
        SearchFor() {
            window.location.href = "/search?query="+this.query
        }

    }
}
</script>
<style>
.navbar-toggler:focus {
    box-shadow: 0 0 0 0.10rem var(--bp-khaki) !important;
}

.navbar-brand {
    padding-top: .75rem;
    padding-bottom: .75rem;
    font-size: 1rem;
    background-color: rgba(0, 0, 0, .25);
    box-shadow: inset -1px 0 0 rgba(0, 0, 0, .25);
}

.navbar .navbar-toggler {
    top: .25rem;
    right: 1rem;
}

.navbar .form-control {
    padding: .75rem 1rem;
    border-width: 0;
    border-radius: 0;
}

.form-control-dark {
    color: #fff;
    background-color: rgba(255, 255, 255, .1);
    border-color: rgba(255, 255, 255, .1);
}

.form-control-dark:focus {
    border-color: transparent;
    box-shadow: 0 0 0 3px rgba(255, 255, 255, .25);
}

@media (max-width:768px) {
    .topnav_user {
        width: 100% !important
    }
}

;
</style>