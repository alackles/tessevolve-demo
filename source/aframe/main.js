var scene = d3.select('a-scene')

var accessor = function(row) {
    return {
        x: +row.x*10,
        y: +row.y*10,
        z: +row.z*10,
        fitness: +row.fitness
    }
}

var coords = function(x, y, z) {
    return x + " " + y + " " + z
}

var rScale = d3.scaleSqrt();
rScale.domain([0, 100]).range([0, 5]);

var opScale = d3.scaleSqrt();
opScale.domain([0, 100]).range([0.25, 0.75]);

d3.csv("../../data/coords_shubert.csv", accessor)
    .then(
        function(landscape) {

        var pts = scene.selectAll('a-sphere')
            .data(landscape, function(d){return d.x})

        pts.enter()
            .append('a-sphere')
            .attr('class', 'data_point')
            .attr('color', 'darkseagreen')
            .attr('transparent', 'true')
            .attr('position', function(d) {return coords(d.x, d.y, d.z)})
            .attr('radius', function(d) {return rScale(d.fitness)})
            .attr('opacity', function(d) {return opScale(d.fitness)});

        console.log(coords(10, 2, 4));
        }
    )