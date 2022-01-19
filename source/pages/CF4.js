$.getScript("./landscape.js", function()
    {;
        landscape_file = "../../data/coords_CF4.csv";
        lod_file = "../../data/reps/SEED_0__F_CF4/lod.csv";
        edges_file = "../../data/reps/SEED_0__F_CF4/edges.csv";
        load_landscape(landscape_file, lod_file, edges_file);
    }

)


