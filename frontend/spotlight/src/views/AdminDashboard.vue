<template>
    <div>
        <TopNav></TopNav>
        <div class="container-fluid">
            <div class="row">
                <AdminSideNav></AdminSideNav>
                <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
                    <h2 class="pt-5">Admin Dashboard</h2>
                    <div class="container pt-5">
                        <div class="row g-0 text-center">
                            <div class="col menu_board p-2 m-2 rounded">
                                <div>
                                    <h5>Pending Album Flag Req</h5>
                                </div>
                                <div>25</div>
                            </div>
                            <div class="col menu_board p-2 m-2 rounded">
                                <div>
                                    <h5>Pending Song Flag Req</h5>
                                </div>
                                <div>10</div>
                            </div>
                            <div class="col menu_board p-2 m-2 rounded">
                                <div>
                                    <h5>Current Logged in users Number</h5>
                                </div>
                                <div>50</div>
                            </div>
                        </div>
                    </div>
                    <div class="container pt-5">
                        <div class="row g-0 text-center">
                            <div class="col menu_board p-2 m-2 rounded">
                                <div>
                                    <h5>Total Users</h5>
                                </div>
                                <div>200</div>
                            </div>
                            <div class="col menu_board p-2 m-2 rounded">
                                <div>
                                    <h5>Melophiles</h5>
                                </div>
                                <div>125</div>
                            </div>
                            <div class="col menu_board p-2 m-2 rounded">
                                <div>
                                    <h5>Patrons</h5>
                                </div>
                                <div>50</div>
                            </div>
                            <div class="col menu_board p-2 m-2 rounded">
                                <div>
                                    <h5>Creators</h5>
                                </div>
                                <div>25</div>
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
    mounted() {
        const width = 300;
        const height = 300;
        const marginTop = 20;
        const marginRight = 0;
        const marginBottom = 30;
        const marginLeft = 40;
        const bar_data = [{ "letter": "1-2", "frequency": 2 },
        { "letter": "2-3", "frequency": 5 },
        { "letter": "3-3.5", "frequency": 10 },
        { "letter": "3.5-4", "frequency": 25 },
        { "letter": "4-4.5", "frequency": 50 },
        { "letter": "4.5-5", "frequency": 90 },
        ];

        const x = d3.scaleBand()
            .domain(d3.sort(bar_data, d => -d.frequency).map(d => d.letter))
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
            .attr("x", d => x(d.letter))
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
            .text("45");

        function zoom(svg) {
            const extent = [[marginLeft, marginTop], [width - marginRight, height - marginTop]];

            svg.call(d3.zoom()
                .scaleExtent([1, 6])
                .translateExtent(extent)
                .extent(extent)
                .on("zoom", zoomed));

            function zoomed(event) {
                x.range([marginLeft, width - marginRight].map(d => event.transform.applyX(d)));
                svg.selectAll(".bars rect").attr("x", d => x(d.letter)).attr("width", x.bandwidth());
                svg.selectAll(".x-axis").call(xAxis);
            }
        }
        const data = [{"name":"Classic","value":30},
        {"name":"Blues","value":15},
        {"name":"Metal","value":50},
        {"name":"Lofi","value":40},
        {"name":"Indie","value":25}
    ];
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