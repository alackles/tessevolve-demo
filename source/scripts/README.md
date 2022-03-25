This folder contains the scripts necessary for data pre-processing for the visualization. 

Follow this guide to execute scripts in the appropriate order.
# Generate Replicates
1. `rep_names.py` : generates names of replicate folders (=> data/filenames.csv)
2. `rep.py` : generates data (=> scripts/data/reps/SEED_*/phylogeny_1000.csv)
# Generate Funtion Coordinates
1. `fcn_outputs.py` : generates function coordinates (=> scripts/data/coords/coords_*.csv)
2. `fcn_proc4D.R` : process coordinates for 4D (scripts/data/coords/coords_*.csv => data/coords/coords/coords_*.csv)
# Generate LOD (all in scripts/data/reps/SEED_*/)
1. `lod_gen.py` : generate initial LODs (phylogeny_1000.csv => lod_init.csv)
2. `lod_fitness.py` : add fitnesses to LODs (lod_init.csv => lod_fit.csv)
3. `lod_round.py` : round 4D LOD after fitness calc (lod_fit.csv => lod_round.csv)
4. `lod_proc4D.R` : process LODs for 4D and pass through others with new name (lod_round.csv => lod.csv)
# Generate Edges
1. `edge_gen.py` : generate final edge data (lod.csv => edge.csv)