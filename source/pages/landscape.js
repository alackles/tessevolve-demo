// TODO: Vincent cmaera rig should be 25 25 25 

var accessor_3D = function(row) {
    return {
        x: +row.x*10,
        y: +row.y*10,
        z: +row.z*10,
        fitness: +row.fitness,
        id: +row.id
    }
}

var accessor_2D = function(row) {
  return {
      x: +row.x*10,
      y: +row.y*10,
      z: 0,
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

    // Remove LOD nodes
    var boxes = document.querySelectorAll("a-box");
    for (var i = 0; i < boxes.length; i++) {
        boxes[i].parentNode.removeChild(boxes[i]);
    }

    // Remove meshline
    var phyloLine = document.getElementById('phyloLine')
    if (phyloLine !== null) {
      phyloLine.parentNode.removeChild(phyloLine);
    }
}

var load_landscape = function() {
    
    var seed = document.querySelector('select[name="rep"]').value;
    var fcn = document.querySelector('select[name="function"]').value;
    var dim = document.querySelector('select[name="dim"]').value;
    var mutrate = document.querySelector('select[name="mut_rate"]').value;
    var tourny = document.querySelector('select[name="tour_size"]').value;
    var phylo_detail = document.querySelector('select[name="phylo"]').value;

    var basepath = "../../data/"
    var coord_data = basepath + "coords_" + fcn + "_" + dim + "D.csv";

    var replicate_path = basepath + "reps/SEED_" + seed + "__F_" + fcn + "__D_" + dim + "__MUT_" + mutrate + "__T_" + tourny + "/";
    var node_data = replicate_path + "lod.csv"
    var edge_data = replicate_path + "edges.csv"

    var scene = d3.select('a-scene')

    if (dim == 3) {
      d3_coord_data = d3.csv(coord_data, accessor_3D);
      d3_node_data = d3.csv(node_data, accessor_3D);
      d3_edge_data = d3.text(edge_data)
    } else if (dim == 2) {
      d3_coord_data = d3.csv(coord_data, accessor_2D);
      d3_node_data = d3.csv(node_data, accessor_2D);
      d3_edge_data = d3.text(edge_data);
    }

    Promise.all([
        d3_coord_data,
        d3_node_data,
        d3_edge_data
    ])
    .then(
        function(files) {
        landscape = files[0]
        lod = files[1]
        edges = files[2]

        const meshline_param = 'lineWidth: 20; path: ' + edges + '; color: #000'
        
        var pts = scene.selectAll('a-sphere')
            .data(landscape, function(d){return d.x})
        
        if (phylo_detail !== "0") {
          var nodes = scene.selectAll('a-box')
              .data(lod, function(d){return d.id})
        
          var lod = scene.append('a-entity')
            .attr('id', "phyloLine")
            .attr('meshline', meshline_param)
        }

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
            .attr('opacity', 0.9);
        
         nodes.enter()
            .append('a-box')
            .attr('class', 'phylo_node')
            .attr('color', function (d) {return phyloScale(d.id)})
            .attr('position', function(d) {return coords(d.x, d.y, d.z)})
            .attr('height', 0.2)
            .attr('depth', 0.2)
            .attr('width', 0.2) 
        
        }
    )

}

var draw = function() {
  reload();
  load_landscape();
}