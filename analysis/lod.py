import ALifeStdDev.phylogeny as phylodev
import networkx as nx
import math
import csv

rep_path = "../data/reps/"
filename = "../data/reps/SEED_01__F_Shubert/phylogeny_10000.csv"
lod_path = "../data/reps/SEED_01__F_Shubert/lod.csv"

phylo = phylodev.load_phylogeny_to_networkx(filename)
extant_ids = phylodev.get_extant_taxa_ids(phylo, not_destroyed_value=math.inf)
lod = phylodev.extract_asexual_lineage(phylo, extant_ids[0])
lod_dict = dict(lod.nodes(data="taxon_info"))
with open(lod_path, "w") as lod_file:
    lod_file.write("id,x,y,z\n")
for gen, vals in lod_dict.items():
    vals = ",".join(vals.lstrip('[ ').rstrip(' ]').split())
    line = str(gen) + "," + vals + "\n"
    with open(lod_path, "a") as lod_file:
        lod_file.write(line)