// TODO: Vincent cmaera rig should be 25 25 25 

var accessor = function(row) {
    return {
        x: +row.x*10,
        y: +row.y*10,
        z: +row.z*10,
        fitness: +row.fitness,
        id: +row.id
    }
}


var coords = function(x, y, z) {
    return x + " " + y + " " + z
}

var reload = function() {
    // Remove default text if it's there 
    var defaultText = document.getElementById('defaultText');
    if (defaultText !== null) {
      defaultText.parentNode.removeChild(defaultText);
    }

    // Remove previous landscape
    var spheres = document.querySelectorAll("a-sphere");
    for (var i = 0; i < spheres.length; i++) {
        spheres[i].parentNode.removeChild(spheres[i]);
    }

    // TODO: As you add elements, remove them when you need to
}

var load_landscape = function() {


    var fcn = document.querySelector('select[name="function"').value;
    var filename1 = "../../data/coords_" + fcn + "_3D.csv";
    var scene = d3.select('a-scene')

    Promise.all([
        d3.csv(filename1, accessor),
        //d3.csv(filename2, accessor),
        //d3.text(filename3)
    ])
    .then(
        function(files) {
        landscape = files[0]
        //lod = files[1]
        //edges = files[2]

        var pts = scene.selectAll('a-sphere')
            .data(landscape, function(d){return d.x})
        
        
        //var nodes = scene.selectAll('a-box')
        //    .data(lod, function(d){return d.id})
        

        //const meshline_param = 'linewidth: 20; path: ' + edges + '; color: #000'

        //var lod = scene.append('a-entity')
        //    .attr('meshline', meshline_param)

        var min = d3.min(landscape, function(d) {return d.fitness});
        var max = d3.max(landscape, function(d) {return d.fitness});

        var colScale = d3.scaleSequential(d3.interpolatePlasma);
        colScale.domain([min, max])

        var phyloScale = d3.scaleSequential(d3.interpolateViridis);
        phyloScale.domain([0, 10000])
        
        pts.enter()
            .append('a-sphere')
            .attr('class', 'data_point')
            .attr('color', function(d) {return colScale(d.fitness)})
            .attr('position', function(d) {return coords(d.x, d.y, d.z)})
            .attr('radius', 1)
            .attr('opacity', 1);
        
/*         nodes.enter()
            .append('a-box')
            .attr('class', 'phylo_node')
            .attr('color', function (d) {return phyloScale(d.id)})
            .attr('position', function(d) {return coords(d.x, d.y, d.z)})
            .attr('height', 0.2)
            .attr('depth', 0.2)
            .attr('width', 0.2) */
        
        }
    )

}

var draw = function() {
  reload();
  load_landscape();
}