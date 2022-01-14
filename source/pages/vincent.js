$.getScript("./landscape.js", function()
    {;
        landscape_file = "../../data/coords_vincent.csv";
        lod_file = "../../data/reps/SEED_00__F_Vincent/lod.csv";
        edges_file = "../../data/reps/SEED_00__F_Vincent/edges.csv";
        load_landscape(landscape_file, lod_file, edges_file);
    }

)


