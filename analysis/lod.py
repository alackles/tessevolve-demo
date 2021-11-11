import ALifeStdDev.phylogeny as phylodev
import networkx as nx
import matplotlib.pyplot as plt


filename = "../data/reps/SEED_00__F_CF3/phylogeny_1000.csv"

phylo = phylodev.load_phylogeny_to_networkx(filename)
print(phylodev.get_leaf_taxa_ids(phylo))