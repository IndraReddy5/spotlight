<template>
<div class="row g-0 text-center">
    <div class="col menu_board p-2 m-2 rounded">
        <div><h5>Total Albums Created</h5></div>
        <div>{{ AlbumsCreated }}</div>
    </div>
    <div class="col menu_board p-2 m-2 rounded">
        <div><h5>Total Songs Created</h5></div>
        <div>{{ SongsAdded }}</div>
    </div>
    <div class="col menu_board p-2 m-2 rounded">
        <div><h5>Average Rating of Songs</h5></div>
        <div>{{ SongRatingAvg }}</div>
    </div>
</div>
</template>
<script>
export default {
    name: 'CreatorStats',
    props: {
        AlbumsCreated: Number,
        SongsAdded: Number,
        SongRatingAvg: Number,
    }
}
</script>
<style>
.menu_board{
    background-color: var(--bp-khaki);
}
</style>