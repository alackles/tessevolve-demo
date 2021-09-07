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

var load_landscape = function(filename) {

    var scene = d3.select('a-scene')

    d3.csv(filename, accessor)
    .then(
        function(landscape) {

        var pts = scene.selectAll('a-sphere')
            .data(landscape, function(d){return d.x})

        var min = d3.min(landscape, function(d) {return d.fitness});
        var max = d3.max(landscape, function(d) {return d.fitness});

        //console.log(min)
        //console.log(max)

        //var rScale = d3.scaleSqrt();
        //rScale.domain([min, max]).range([0, 5]);
    
        //var opScale = d3.scaleSqrt();
        //opScale.domain([min, max]).range([0.05, 1]);

        var colScale = d3.scaleSequential(d3.interpolatePlasma);
        colScale.domain([min, max])

        pts.enter()
            .append('a-sphere')
            .attr('class', 'data_point')
            .attr('color', function(d) {return colScale(d.fitness)})
            .attr('position', function(d) {return coords(d.x, d.y, d.z)})
            .attr('radius', 2)
            .attr('opacity', 0.9);
        }
    )

}



