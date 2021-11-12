import ALifeStdDev.phylogeny as phylodev
import networkx as nx
import matplotlib.pyplot as plt


filename = "../data/reps/SEED_00__F_CF3/phylogeny_1000.csv"

phylo = phylodev.load_phylogeny_to_networkx(filename)
lod = phylodev.extract_asexual_lod(phylo, not_destroyed_value="inf")
print(lod)