import ALifeStdDev.phylogeny as phylodev
import networkx as nx
import math
import csv

datapath = "./../data/"
reppath = datapath + "reps/"

firstrep = 0
lastrep = 10
fcns = ["Shubert", "CF3", "CF4"]

digs = len(str(lastrep-firstrep))

filename = "phylogeny_10000.csv"
lodname = "lod.csv"
edgename = "edges.csv"

for fcn in fcns:
    for rep in range(firstrep, lastrep):
        dirpath = reppath + "SEED_" + str(rep).rjust(2, '0') + "__F_" + fcn + "/" 
        filepath = dirpath + filename
        lodpath = dirpath + lodname 
        edgepath = dirpath + edgename

        phylo = phylodev.load_phylogeny_to_networkx(filepath)
        extant_ids = phylodev.get_extant_taxa_ids(phylo, not_destroyed_value=math.inf)
        lod = phylodev.extract_asexual_lineage(phylo, extant_ids[0])
        
        lod_dict = dict(lod.nodes(data="taxon_info"))
        edges_num = lod.edges()
        edges_pts = []
        for a, b in edges_num:
            start = lod_dict[a]
            end = lod_dict[b]
            edges_pts.append([start, end])

        with open(lodpath, "w") as lod_file:
            lod_file.write("id,x,y,z\n")
        with open(edgepath, "w") as edge_file:
            edge_file.write("id,x1,y1,z1,x2,y2,z2\n")

        for gen, vals in lod_dict.items():
            vals = ",".join(vals.lstrip('[ ').rstrip(' ]').split())
            line = str(gen) + "," + vals + "\n"
            with open(lodpath, "a") as lod_file:
                lod_file.write(line)
        
        for i, edge in enumerate(edges_pts):
            start = ",".join(edge[0].lstrip('[ ').rstrip(' ]').split())
            end = ",".join(edge[1].lstrip('[ ').rstrip(' ]').split())
            line = str(i) + "," + start + "," + end + "\n"
            with open(edgepath, "a") as edge_file:
                edge_file.write(line)