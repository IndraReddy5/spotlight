<template>
    <div class="col">
        <div class="container rounded SongComponent m-2">
            <div class="row row-cols-2">
                <div class="col-4 SongImgClass position-relative"><img class="rounded float-start"
                        :src="generateUrl(imageSource)" alt=""
                        style="height: 90px; width:90px;">
                    <div class="overlayPlay"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 15 15" width="90"
                            height="70" stroke="var(--bp-yellow)" stroke-width="1" stroke-linecap="round"
                            fill="var(--bp-yellow)" stroke-linejoin="round" class="feather feather-home" aria-hidden="true">
                            <path
                                d="M6.271 5.055a.5.5 0 0 1 .52.038l3.5 2.5a.5.5 0 0 1 0 .814l-3.5 2.5A.5.5 0 0 1 6 10.5v-5a.5.5 0 0 1 .271-.445z" />
                        </svg></div>
                </div>
                <div class="col-8 position-relative">
                    <div class="float-start">
                        <div class="pt-2"><a :href=generateSongUrl(sid) style="color: white;"> {{ SongName }}</a></div>
                    </div>
                    <div class="d-flex justify-content-between SongComponentSecondary end-20 bottom-0 position-absolute">
                        <strong><em>{{ SongDuration }} secs</em></strong>
                        <span>{{ ReleaseDate }}</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: 'SongComponent',
    props: {
        SongName: String,
        ReleaseDate: String,
        SongDuration: Number,
        imageSource: String,
        sid: String,
    },
    methods: {
        generateUrl(src) {
            return __BACKEND_URL__ + src;
        },
        generateSongUrl(id) {
            return "/song/" + id;
        }
    }
}
</script>
<style>
.SongComponent {
    height: 100px;
    background-color: var(--bp-khaki);
    width: 300px !important;
    padding: 5px;
    padding-left: 0px;
    overflow-y: scroll;
}

.SongComponentSecondary {
    color: #DCDCDC;
    font-size: 14px;
    text-wrap: balance;
    width: 160px;
}

@media (max-width: 320px) {
    .SongImgClass img {
        height: 70px !important;
        width: 70px !important;
    }

    .SongComponent {
        height: 80px;
        background-color: var(--bp-khaki);
        width: 240px !important;
        padding: 5px;
        padding-left: 0px;
        overflow-y: scroll;
    }

    .SongComponentSecondary {
        color: #DCDCDC;
        font-size: 14px;
        text-wrap: balance;
        width: 140px;
    }

    .overlayPlay {
        left: 0% !important;
        top: 0% !important;
    }
}

.overlayPlay {
    position: absolute;
    opacity: 0;
    left: 7%;
    top: 7%;
}

.SongImgClass:hover .overlayPlay {
    opacity: 1;
}
</style>