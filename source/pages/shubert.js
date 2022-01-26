$.getScript("./landscape.js", function()
    {;
        landscape_file = "../../data/coords_shubert.csv";
        lod_file = "../../data/reps/SEED_00__F_Shubert__MUT_00001/lod.csv";
        edges_file = "../../data/reps/SEED_00__F_Shubert__MUT_00001/edges.csv";
        load_landscape(landscape_file, lod_file, edges_file);
    }

)


