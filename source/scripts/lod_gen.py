import collections
import itertools as it
import math
from decimal import Decimal

import ALifeStdDev.phylogeny as phylodev
from repparse import parameters

# Create an ordered dictionary of a line of descent from the phylogeny
# This allows us to put the LOD in time order
def lod_dict_from_phylo(filepath):
    phylo = phylodev.load_phylogeny_to_networkx(filepath)
    extant_ids = phylodev.get_extant_taxa_ids(phylo, not_destroyed_value=math.inf)
    lod = phylodev.extract_asexual_lineage(phylo,extant_ids[0])
    lod_dict = dict(lod.nodes(data="taxon_info"))
    lod_chrono = collections.OrderedDict(sorted(lod_dict.items()))
    return lod_chrono

# Create the line of descent file
# Columns: ID (generation), values 
def export_lod(lod, dims, lodpath="lod.csv"):

    assert dims in [2, 3, 4]

    with open(lodpath, "w") as lod_file:
        xcoords = ",".join(["x" + str(d) for d in range(dims)])
        lod_file.write("id," + xcoords + "\n")

    for gen, vals in lod.items():
        vals = ",".join(vals.lstrip('[ ').rstrip(' ]').split())
        line = str(gen) + "," + vals + "\n"
        with open(lodpath, "a") as lod_file:
            lod_file.write(line) 

# Turn the line of descent file into a single string for the purposes of creating a "meshline"
# Format is val1, val2, [val3, val4]; val1, val2, val3, val4;
def export_edges(lod, edgepath="edges.csv"):
    edge_list = []
    for vals in lod.values():
        # multiply string values by 10 and convert back to string
        # this helps the spacing visually
        vals = " ".join([str(Decimal(x)*10) for x in vals.lstrip('[ ').rstrip(' ]').split()])
        edge_list.append(vals)
    with open(edgepath, "w") as edge_file:
        edge_file.write(",".join(edge_list))

def main():

    phyloname = "phylogeny_1000.csv"
    lodname = "lod.csv"
    edgename = "edges.csv"
    
    params = parameters()

    for p in params:
        dirpath = p["path"]
        dim = p["dim"]
        filepath = dirpath + phyloname
        lodpath = dirpath + lodname 
        edgepath = dirpath + edgename
        
        lod = lod_dict_from_phylo(filepath)
        export_lod(lod, int(dim), lodpath)
        export_edges(lod, edgepath)
        print(dirpath)
    
if __name__=="__main__":
    main()

