// TODO: Vincent cmaera rig should be 25 25 25 

// Standard accessor: 2D and 3D
// https://stackoverflow.com/questions/25412046/d3js-working-with-unknown-headers-number-of-columns-number-of-rows
var accessor = function(row) {
   numeric_row = {};
    for (col in row) {
        numeric_row[col] = +row[col];
    }
    return numeric_row;
}

var coords = function(x, y, z) {
    return x + " " + y + " " + z;
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
    var phyloLine = document.getElementById('phyloLine');
    if (phyloLine !== null) {
      phyloLine.parentNode.removeChild(phyloLine);
    }
}

var load_landscape = function() {
    
    // look at the labels -> names
    /*
    var seed = document.querySelector('select[name="rep"]').value;
    var fcn = document.querySelector('select[name="function"]').value;
    var dim = document.querySelector('select[name="dim"]').value;
    var mutrate = document.querySelector('select[name="mut_rate"]').value;
    var tourny = document.querySelector('select[name="tour_size"]').value;
    var phylo_detail = document.querySelector('select[name="phylo"]').value;
    */

    // start of my stuff -Lilia
    var seed; var fcn; var dim; var mutrate; var tourny; var phylo_detail;

        var CF1 = document.querySelector('input[name="CF1"]');
        var CF2 = document.querySelector('input[name="CF2"]');
        var shubert = document.querySelector('input[name="shubert"]');
        var vincent = document.querySelector('input[name="vincent"]');
        var twoD = document.querySelector('input[name="2D"]');
        var threeD = document.querySelector('input[name="3D"]');
        var fourD = document.querySelector('input[name="4D"]');
        var showLineage = document.querySelector('input[name="lineage"]');
        var mut_rate = document.querySelector('input[id="mut_rate_slider"]').value;
        var tourn_size = document.querySelector('input[id="tourn_size_slider"]').value;
        var rep = document.querySelector('input[id="replicate"]').value;

        if(mut_rate == 1){
            mut_rate = "00001";
        } else if(mut_rate == 2){
            mut_rate = "0001";
        } else if(mut_rate == 3){
            mut_rate = "001";
        } else {
            mut_rate = "01";
        }

        if(tourn_size == 1){
            tourn_size = "02";
        } else if(tourn_size == 2){
            tourn_size = "04";
        } else if(tourn_size == 3){
            tourn_size = "08";
        } else {
            tourn_size = 16;
        }

        // check to see if show lineage is checked. if it is not, set to null
        if(!showLineage){
            showLineage = null;
        } else {
            showLineage = true;
        }

        tourny = tourn_size;
        seed = rep;
        mutrate = mut_rate;
        phylo_detail = showLineage;

        // these are not showing up?
        console.log("showLineage: " + showLineage);
        console.log("mut_rate: " + mut_rate);
        console.log("tourn_size: " + tourn_size);
        console.log("rep: " + rep);

        // create an if-statement to choose only one box for fcn
        if(CF1.checked && !CF2.checked && !shubert.checked && !vincent.checked){
            fcn = "CF1";
        } else if (CF2.checked && !CF1.checked && !shubert.checked && !vincent.checked ){
            fcn = "CF2";
        } else if (shubert.checked && !CF2.checked && !CF1.checked && !vincent.checked ){
            fcn = "shubert";
        } else if (vincent.checked && !CF2.checked && !shubert.checked && !CF1.checked ){
            fcn = "vincent";
        } else {
            // default to CF1
            fcn = "CF1";
        }

        // create an if-statement to choose only one box for dim
        if(twoD.checked && !threeD.checked && !fourD.checked){
            dim = "2";
        } else if (threeD.checked && !twoD.checked && !fourD.checked){
            dim = "3";
        } else if (fourD.checked && !threeD.checked && !twoD.checked){
            dim = "4";
        } else {
            // default to 3D
            dim = "3";
        }
    // end of my stuff -Lilia

    var basepath = "../../tessevolve/data/"; // for web deployment
    //var basepath = "../../data/" // for local host 
    var coord_data = basepath + "coords/coords_" + fcn + "_" + dim + "D.csv";

    var replicate_path = basepath + "reps/SEED_" + seed + "__F_" + fcn + "__D_" + dim + "__MUT_" + mutrate + "__T_" + tourny + "/";
    var node_data =  replicate_path + "lod.csv";
    var edge_data = replicate_path + "edge.csv";

    var scene = d3.select('a-scene');

    var d3_coord_data = d3.csv(coord_data, accessor);
    var d3_node_data = d3.csv(node_data, accessor);
    var d3_edge_data = d3.text(edge_data);

    Promise.all([
        d3_coord_data,
        d3_node_data,
        d3_edge_data,
        dim,
        fcn
    ])
    .then(
        function(files) {
        landscape = files[0];
        lod = files[1];
        edges = files[2];
        dims = files[3];
        fcn = files[4];

        var fitnessCol = "fitness";

        if (dims == 4) {
            fitnessCol = "fitness5";
        }
        
        // Set color scale 
        var set_min = function(fitnessCol) {
            return d3.min(landscape, function(d) {return d[fitnessCol]});
        };

        var set_max = function(fitnessCol) {
            return d3.max(landscape, function(d) {return d[fitnessCol]});
        };

        var colScale = d3.scaleSequential(d3.interpolatePlasma);
        colScale.domain([set_min(fitnessCol), set_max(fitnessCol)]);

        // Draw Points 
        var pts = scene.selectAll('a-sphere')
            .data(landscape, function(d){return d.x0});

        pts.enter()
            .append('a-sphere')
            .attr('class', 'data_point')
            .attr('position', function(d) {return coords(d.x0, d.x1, d.x2)})
            .attr('color', function (d) {return colScale(d[fitnessCol])})
            .attr('radius', 0.1)
            .attr('opacity', 0.9);
        
        // Draw Nodes
        if (phylo_detail !== "0") {

          const meshline_param = 'lineWidth: 2; path: ' + edges + '; color: grey';
          
          var nodes = scene.selectAll('a-box')
              .data(lod, function(d){return d.id});
        
          scene.append('a-entity')
            .attr('id', "phyloLine")
            .attr('meshline', meshline_param);
        
          nodes.enter()
            .append('a-box')
            .attr('class', 'phylo_node')
            .attr('position', function(d) {return coords(d.x0, d.x1, d.x2)})
            .attr('height', 0.04)
            .attr('depth', 0.04)
            .attr('width', 0.04)
            .attr('color', function (d) {return colScale(d[fitnessCol])});
          }

        var colScaleNode = function(d) {
            if (typeof d == 'undefined' || isNaN(d)) {
                return "grey"
            } else {
                return colScale(d)
            }
        }

        var opScaleNode = function(d) {
            if (typeof d == 'undefined' || isNaN(d)) {
                return 0.5
            } else {
                return 1
            }
        }

        // Change colors on scroll
        var colorDim = 0;
        var colorChange = function() {

            colorDim -= 0.5

            // Handle different ranges
            if (fcn == "vincent") {
                if (colorDim < 0.5) {
                    colorDim = 10.5;
                }
            } else {
               if (colorDim < -5) {
                    colorDim = 5;
               }
            }   
            
            // Set fitness column name
            var colorDimName = "fitness" + String(colorDim);

            // Change points color
            scene.selectAll('.data_point')
                .attr('color', function(d) {return colScale(d[colorDimName])});

            // Change nodes color 
            scene.selectAll('.phylo_node')
                .attr('color', function(d) {return colScaleNode(d[colorDimName])})
                .attr('opacity', function(d) {return opScaleNode(d[colorDimName])});
        };
        
        if (dims == 4) {
            scene.on("wheel", colorChange);
        }

        }
    ) // end of then
}

var draw = function() {
    console.log("Draw function called");
    reload();
    load_landscape();
}