import ALifeStdDev.phylogeny as phylodev
import networkx as nx
import math
import csv
import collections

datapath = "./../data/"
reppath = datapath + "reps/"

firstrep = 0
lastrep = 10
fcns = ["Shubert", "Vincent", "CF3", "CF4"]

digs = len(str(lastrep-firstrep))

filename = "phylogeny_10000.csv"
lodname = "lod.csv"
edgename = "edges.csv"

for fcn in fcns:
    for rep in range(firstrep, lastrep):
        dirpath = reppath + "SEED_" + str(rep).rjust(2, '0') + "__F_" + fcn + "/" 
        filepath = dirpath + filename
        lodpath = dirpath + lodname 

        phylo = phylodev.load_phylogeny_to_networkx(filepath)
        extant_ids = phylodev.get_extant_taxa_ids(phylo, not_destroyed_value=math.inf)
        lod = phylodev.extract_asexual_lineage(phylo, extant_ids[0])
        
        lod_dict = dict(lod.nodes(data="taxon_info"))
        lod_chrono = collections.OrderedDict(sorted(lod_dict.items()))

        with open(lodpath, "w") as lod_file:
            lod_file.write("id,x,y,z\n")

        for gen, vals in lod_chrono.items():
            vals = ",".join(vals.lstrip('[ ').rstrip(' ]').split())
            line = str(gen) + "," + vals + "\n"
            with open(lodpath, "a") as lod_file:
                lod_file.write(line) 