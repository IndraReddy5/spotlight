<template>
    <div class="col">
        <div class="rounded AlbumComponent m-2 position-relative">
            <img class="rounded" :src="generateUrl(imageSource)" alt = "album image" style="height: 120px; width:120px;">
            <div class="overlayPlayAlbum"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 15 15" width="90" height="70"
                    stroke="var(--bp-yellow)" stroke-width="1" stroke-linecap="round" fill="var(--bp-yellow)"
                    stroke-linejoin="round" class="feather feather-home" aria-hidden="true">
                    <path
                        d="M6.271 5.055a.5.5 0 0 1 .52.038l3.5 2.5a.5.5 0 0 1 0 .814l-3.5 2.5A.5.5 0 0 1 6 10.5v-5a.5.5 0 0 1 .271-.445z" />
                </svg></div>
            <div class="pt-2 ps-1">{{ AlbumName }}</div>
            <div class="pt-1 ps-1 pb-3 AlbumComponentSecondary"> <strong><em>{{ AlbumCreator }}</em></strong></div>
        </div>
    </div>
</template>
<script>
export default {
    name: 'AlbumComponent',
    props: {
        AlbumName: String,
        AlbumCreator: String,
        imageSource: String,
    },
    methods: {
        generateUrl(src) {
            return "http://127.0.0.1:8000/static/Album_Images/" + src;
        }
    }
}
</script>
<style>
.AlbumComponent {
    height: 250px;
    background-color: var(--bp-khaki);
    width: 140px;
    padding: 10px;
    padding-bottom: 0px;
    overflow-y: scroll;
}

.AlbumComponentSecondary {
    color: #DCDCDC;
    font-size: 14px;
    text-wrap: balance;
}

.overlayPlayAlbum {
    position: absolute;
    opacity: 0;
    left: 15%;
    top: 15%;
}

.AlbumComponent:hover .overlayPlayAlbum {
    opacity: 1;
}
</style>