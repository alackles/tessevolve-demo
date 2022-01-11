$.getScript("./landscape.js", function()
    {;
        landscape_file = "../data/coords_shubert.csv";
        lod_file = "../data/reps/SEED_00__F_Shubert/lod.csv";
        edges_file = "../data/reps/SEED_00__F_Shubert/edges.csv";
        load_landscape(landscape_file, lod_file, edges_file);
    }

)


