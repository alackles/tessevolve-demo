$.getScript("./landscape-2d.js", function()
    {;
        landscape_file = "../../data/coords_shubert_2D.csv";
        lod_file = "../../data/reps/SEED_09__F_Shubert__D_2__MUT_0001__T_16/lod.csv";
        edges_file = "../../data/reps/SEED_09__F_Shubert__D_2__MUT_0001__T_16/edges.csv";
        load_landscape(landscape_file, lod_file, edges_file);
    }

)


