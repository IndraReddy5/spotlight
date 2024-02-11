<template>
    <div>
        <TopNav></TopNav>
        <div class="container-fluid">
            <div class="row">
                <AdminSideNav @get-data="receiveData"></AdminSideNav>
                <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
                    <h2 class="pt-5">Admin Dashboard</h2>
                    <div class="container pt-5">
                        <div class="row g-0 text-center">
                            <div class="col menu_board p-2 m-2 rounded">
                                <div>
                                    <h5>Pending Genre Req</h5>
                                </div>
                                <div><span> {{ pendingGenreReqLength }}</span></div>
                            </div>
                            <div class="col menu_board p-2 m-2 rounded">
                                <div>
                                    <h5>Pending Album Flag Req</h5>
                                </div>
                                <div><span> {{ pendingAlbumReqLength }}</span></div>
                            </div>
                            <div class="col menu_board p-2 m-2 rounded">
                                <div>
                                    <h5>Pending Song Flag Req</h5>
                                </div>
                                <div>{{ pendingSongReqLength }}</div>
                            </div>
                        </div>
                    </div>
                    <div class="container pt-5">
                        <div class="row g-0 text-center">
                            <div class="col menu_board p-2 m-2 rounded">
                                <div>
                                    <h5>Total Users</h5>
                                </div>
                                <div>{{ totalUsers }}</div>
                            </div>
                            <div class="col menu_board p-2 m-2 rounded">
                                <div>
                                    <h5>Melophiles</h5>
                                </div>
                                <div>{{ Melophiles - Patrons - Creators }}</div>
                            </div>
                            <div class="col menu_board p-2 m-2 rounded">
                                <div>
                                    <h5>Patrons</h5>
                                </div>
                                <div>{{ Patrons }}</div>
                            </div>
                            <div class="col menu_board p-2 m-2 rounded">
                                <div>
                                    <h5>Creators</h5>
                                </div>
                                <div>{{ Creators }}</div>
                            </div>
                        </div>
                    </div>
                    <div class="container pt-5 position-relative">
                        <div class="row g-0 justify-content-between">
                            <div class="col menu_board p-2 m-2 rounded text-center">
                                <svg id="canvasPie" class="w-100 p-2"></svg>
                            </div>
                            <div class="col menu_board p-2 m-2 rounded text-center">
                                <svg id="canvas1" class="w-100 p-2"></svg>
                            </div>
                        </div>
                    </div>
                </main>
            </div>
        </div>
    </div>
</template>
<script>
import AdminSideNav from '@/components/AdminSideNav.vue';
import TopNav from '@/components/TopNav.vue';
import * as d3 from "d3";

export default {
    name: 'AdminDashboard',
    components: {
        AdminSideNav,
        TopNav,
    },
    data: function () {
        return {
            pendingGenreReqLength: null,
            pendingAlbumReqLength: null,
            pendingSongReqLength: null,
            pendingGenreReq: null,
            pendingSongFlagReq: null,
            pendingAlbumFlagReq: null,
            totalUsers: 0,
            Melophiles: 0,
            Patrons: 0,
            Creators: 0,
            totalSongs: 0,
            song_rating_data: [],
            song_genre_data: [],
        }
    },
    async mounted() {
        await fetch(__API_URL__ + 'admin/dashboard/stats', {
            headers: { 'content-type': 'application/json', "Auth-Token": localStorage.getItem("Auth-Token") },
            'method': 'GET'
        }).then(response => response.json())
            .then(data => {
                if (data != "No pending genre creation requests") {
                    let res_data = data;
                    this.pendingGenreReqLength = res_data.pending_genre_req;
                    this.pendingAlbumReqLength = res_data.pending_album_flag_req;
                    this.pendingSongReqLength = res_data.pending_song_flag_req;
                    this.Creators = res_data.Creators;
                    this.Melophiles = res_data.Melophiles;
                    this.Patrons = res_data.Patrons;
                    this.totalUsers = res_data.total_users;
                    this.totalSongs = res_data.total_songs;
                    let temp_data = [];
                    for (let i = 0; i < res_data.genre_data.length; i++) {
                        if (res_data.genre_data[i].value != 0) {
                            temp_data.push({ name: res_data.genre_data[i].name, value: res_data.genre_data[i].value });
                        }
                    }
                    this.song_genre_data = temp_data;
                    this.song_rating_data = res_data.song_rating_data;
                }
            });
        const width = 300;
        const height = 300;
        const marginTop = 20;
        const marginRight = 0;
        const marginBottom = 30;
        const marginLeft = 40;
        const bar_data = this.song_rating_data;
        const x = d3.scaleBand()
            .domain(d3.sort(bar_data, d => -d.frequency).map(d => d.range))
            .range([marginLeft, width - marginRight])
            .padding(0.1);

        const xAxis = d3.axisBottom(x).tickSizeOuter(0);

        const y = d3.scaleLinear()
            .domain([0, d3.max(bar_data, d => d.frequency)]).nice()
            .range([height - marginBottom, marginTop]);

        const svg = d3.select("#canvas1")
            .attr("viewBox", [0, 0, width, height])
            .attr("width", width)
            .attr("height", height)
            .attr("style", "max-width: 100%; height: auto;")
            .call(zoom);

        const g = svg.append("g");

        g.append("g")
            .attr("class", "bars")
            .attr("fill", "steelblue")
            .selectAll("rect")
            .data(bar_data)
            .join("rect")
            .attr("x", d => x(d.range))
            .attr("y", d => y(d.frequency))
            .attr("height", d => y(0) - y(d.frequency))
            .attr("width", x.bandwidth());

        g.append("g")
            .attr("class", "x-axis")
            .attr("transform", `translate(0,${height - marginBottom})`)
            .call(xAxis);

        g.append("g")
            .attr("class", "y-axis")
            .attr("transform", `translate(${marginLeft},0)`)
            .call(d3.axisLeft(y))
            .call(g => g.select(".domain").remove());

        svg.append("text")
            .attr("transform", `translate(180, 40)`)
            .style("font", "20px sans-serif")
            .style("fill", "#fff")
            .text("Total Songs");

        svg.append("text")
            .attr("transform", `translate(220, 70)`)
            .style("font", "20px sans-serif")
            .style("fill", "#fff")
            .text(this.totalSongs);

        function zoom(svg) {
            const extent = [[marginLeft, marginTop], [width - marginRight, height - marginTop]];

            svg.call(d3.zoom()
                .scaleExtent([1, 6])
                .translateExtent(extent)
                .extent(extent)
                .on("zoom", zoomed));

            function zoomed(event) {
                x.range([marginLeft, width - marginRight].map(d => event.transform.applyX(d)));
                svg.selectAll(".bars rect").attr("x", d => x(d.range)).attr("width", x.bandwidth());
                svg.selectAll(".x-axis").call(xAxis);
            }
        }
        const data = this.song_genre_data;
        const color = d3.scaleOrdinal()
            .domain(data.map(d => d.name))
            .range(d3.quantize(t => d3.interpolateSpectral(t * 0.8 + 0.1), data.length).reverse())
        const pie = d3.pie()
            .sort(null)
            .value(d => d.value);

        const arc = d3.arc()
            .innerRadius(0)
            .outerRadius(Math.min(width, height) / 2 - 1);

        const labelRadius = arc.outerRadius()() * 0.8;

        // A separate arc generator for labels.
        const arcLabel = d3.arc()
            .innerRadius(labelRadius)
            .outerRadius(labelRadius);

        const arcs = pie(data);

        // Create the SVG container.
        const pie_svg = d3.select("#canvasPie")
            .attr("width", width)
            .attr("height", height)
            .attr("viewBox", [-width / 2, -height / 2, width, height])
            .attr("style", "max-width: 100%; height: auto; font: 10px sans-serif;");

        pie_svg.append("g")
            .attr("stroke", "white")
            .selectAll()
            .data(arcs)
            .join("path")
            .attr("fill", d => color(d.data.name))
            .attr("d", arc)
            .append("title")
            .text(d => `${d.data.name}: ${d.data.value.toLocaleString("en-US")}`);

        // Create a new arc generator to place a label close to the edge.
        // The label shows the value if there is enough room.
        pie_svg.append("g")
            .attr("text-anchor", "middle")
            .selectAll()
            .data(arcs)
            .join("text")
            .attr("transform", d => `translate(${arcLabel.centroid(d)})`)
            .call(text => text.append("tspan")
                .attr("y", "-0.4em")
                .attr("font-weight", "bold")
                .text(d => d.data.name))
            .call(text => text.filter(d => (d.endAngle - d.startAngle) > 0.25).append("tspan")
                .attr("x", 0)
                .attr("y", "0.7em")
                .attr("fill-opacity", 0.7)
                .text(d => d.data.value.toLocaleString("en-US")));

    },
    methods: {
        receiveData(data) {
            if (data.key == "pendingGenreReqLength") {
                this.pendingGenreReqLength = data.value;
            }
            else if (data.key == "pendingAlbumReqLength") {
                this.pendingAlbumReqLength = data.value;
            }
            else if (data.key == "pendingSongReqLength") {
                this.pendingSongReqLength = data.value;
            }
        }
    }
}
</script>
<style>
/* This controls the Chart Title */
text .title {
    font-size: 16px;
}

/* This controls the axis text size */
.axis text {
    font-size: 8px;
}
</style>