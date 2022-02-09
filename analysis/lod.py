import ALifeStdDev.phylogeny as phylodev
import networkx as nx
import math
import csv
import collections
from decimal import Decimal


def lod_dict_from_phylo(filepath):
    # create ordered dictionary from lod
    phylo = phylodev.load_phylogeny_to_networkx(filepath)
    extant_ids = phylodev.get_extant_taxa_ids(phylo, not_destroyed_value=math.inf)
    lod = phylodev.extract_asexual_lineage(phylo,extant_ids[0])
    lod_dict = dict(lod.nodes(data="taxon_info"))
    lod_chrono = collections.OrderedDict(sorted(lod_dict.items()))
    return lod_chrono

def export_lod(lod, dims, lodpath="lod.csv"):
    # create line of descent: lod.csv
    with open(lodpath, "w") as lod_file:
        if (dims==3):
            lod_file.write("id,x,y,z\n")
        elif (dims==2):
            lod_file.write("id,x,y\n")
        else:
            print("Dims invalid")
            return 0
    for gen, vals in lod.items():
        vals = ",".join(vals.lstrip('[ ').rstrip(' ]').split())
        line = str(gen) + "," + vals + "\n"
        with open(lodpath, "a") as lod_file:
            lod_file.write(line) 

def export_edges(lod, edgepath="edges.csv"):
    # create single string for edges for meshline: edges.csv
    edge_list = []
    for vals in lod.values():
        # multiply string values by 10 and convert back to string
        vals = " ".join([str(Decimal(x)*10) for x in vals.lstrip('[ ').rstrip(' ]').split()])
        edge_list.append(vals)
    with open(edgepath, "w") as edge_file:
        edge_file.write(",".join(edge_list))

def lod_gen(dims, first=0, last=10):

    datapath = "./../data/"
    reppath = datapath + "reps/"

    fcns = ["Shubert", "Vincent", "CF3", "CF4"]
    mutrates = ["01", "001", "0001", "00001"]
    tournament_sizes = [2, 4, 8, 16]
    digs = len(str(last-first))

    filename = "phylogeny_1000.csv"
    lodname = "lod.csv"
    genname = "genome.csv"
    edgename = "edges.csv"

    for fcn in fcns:
        for mut in mutrates:
            for t in tournament_sizes:
                for rep in range(first, last):
                    dirpath = reppath + "SEED_" + str(rep).rjust(2, '0') + "__F_" + fcn + "__D_" + str(dims) + "__MUT_" + mut + "__T_" + str(t).rjust(2, '0') + "/" 
                    filepath = dirpath + filename
                    lodpath = dirpath + lodname 
                    edgepath = dirpath + edgename

                    lod = lod_dict_from_phylo(filepath)
                    export_lod(lod, dims, lodpath)
                    export_edges(lod, edgepath)

lod_gen(2)
lod_gen(3)



