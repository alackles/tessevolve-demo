This folder contains the scripts necessary for data pre-processing for the visualization. 

Follow this guide to execute scripts in the appropriate order.


# Replicate Generation
1. `repparse.py` : generates names of rep folders
2. `rep_names.py` : generates names of replicate folders
3. `rep.py` : generates data
4. `fcn_outputs.py` : generates function coordinates

At this point you should have:
- data/filenames.csv : all replicate folder names
- data/reps/*/phylogeny_1000.csv : all replicate phylogenies

- source/scripts/data/coords/*.csv : 2D, 3D, and 4D coordinates
# LOD Analysis
1. `lod_gen.py` : generate initial LODs ("phylogeny_1000.csv" => "lod_init.csv")
2. `lod_fitness.py` : add fitnesses to LODs ("lod_init.csv" => "lod_fit.csv")
3. `lod_round.py` : round LOD after fitness calc ("lod_fit.csv => lod_round.csv")
4. `lod_proc4D.R` : process LODs for 4D and pass through others with new name ("lod_round.csv" => "lod.csv")

# Generate Edges
1. `edge_gen.py` : generate final edge data ("lod.csv" => "edges.csv")