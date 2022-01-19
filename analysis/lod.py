import ALifeStdDev.phylogeny as phylodev
import networkx as nx
import math
import csv
import collections
from decimal import Decimal

datapath = "./../data/"
reppath = datapath + "reps/"

firstrep = 0
lastrep = 3
fcns = ["Shubert", "Vincent", "CF3", "CF4"]

digs = len(str(lastrep-firstrep))

filename = "phylogeny_10000.csv"
lodname = "lod.csv"
edgename = "edges.csv"

for fcn in fcns:
    for rep in range(firstrep, lastrep):
        dirpath = reppath + "SEED_" + str(rep) + "__F_" + fcn + "/" 
        filepath = dirpath + filename
        lodpath = dirpath + lodname 
        edgepath = dirpath + edgename

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
        
        edge_list = []
        for vals in lod_chrono.values():
            # multiply string values by 10 and convert back to string
            vals = " ".join([str(Decimal(x)*10) for x in vals.lstrip('[ ').rstrip(' ]').split()])
            edge_list.append(vals)
        with open(edgepath, "w") as edge_file:
            edge_file.write(",".join(edge_list))