d3.csv("actors.csv").then(data => {
    const parseDate = d3.timeParse("%Y");
    // const parseDate = Date.;

    data.forEach(d => {
        d.DateOfBirth = Date.parse(d["BirthDate"]);
        d.DateOfDeath = Date.parse(d["DeathDate"]);
        d.DebutDate = Date.parse(d["DebutDate"]);
        d.LastFilmDate = Date.parse(d["LastFilmDate"]);
        console.log(d);
    });

    const svgWidth = 3000;
    const svgHeight = data.length * 30;
    const barHeight = 20;

    const minYear = d3.min(data, d => new Date(d.DateOfBirth).getFullYear());
    const maxYear = d3.max(data, d => new Date(d.DateOfDeath).getFullYear() || new Date()).getFullYear();

    const xScale = d3.scaleLinear()
        .domain([minYear, maxYear])
        .range([0, svgWidth]);

    const timelineSvg = d3.select("#timeline").append("svg")
        .attr("width", svgWidth)
        .attr("height", 50);

    const axisBottom = d3.axisBottom(xScale)
        .tickFormat(d3.format(".0f"));

    timelineSvg.append("g")
        .attr("transform", "translate(0, 30)")
        .call(axisBottom);

    const actorsSvg = d3.select("#actors").append("svg")
        .attr("width", svgWidth)
        .attr("height", svgHeight);

    const actorBars = actorsSvg.selectAll(".actor-bar")
        .data(data)
        .enter().append("rect")
        .attr("class", "actor-bar")
        .attr("x", d => xScale(new Date(d.DebutDate).getFullYear()))
        .attr("y", (d, i) => i * 30)
        .attr("width", d => {
            const endYear = new Date(d.LastFilmDate).getFullYear() || new Date().getFullYear();
            return xScale(endYear) - xScale(new Date(d.DebutDate).getFullYear());
            // console.log(endYear);
        })
        .attr("height", barHeight);
});
