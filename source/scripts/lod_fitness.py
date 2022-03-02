#  @file  lod_fitness.py
#  @brief Take the generated lod files and run them through the fitness functions to append fitness to them 
# import functions from niching space

from pylandscapes.functions import shubert
from pylandscapes.functions import vincent
from pylandscapes.CF1 import CF1
from pylandscapes.CF2 import CF2
import inspect
import itertools as it


def eval_lod_fitness(fname, fcn, precision=3):
    with open(fname, 'r') as f:
        f.readline() # skip header
        all_lines = f.readlines()
        print(all_lines)

def main():

    # reps
    first = 0
    last = 2

    datapath = "./../data/"
    reppath = datapath + "reps/"

    lodname = "lod.csv"

    fcn_map = {
        "Shubert": shubert,
        "Vincent": vincent,
        "CF1": CF1,
        "CF2": CF2
    }

    # toy
    reps = ["00"]
    fcns = ["Shubert"]
    dims = ["3"]
    mutrates = ["01"]
    tournament_sizes = ["16"]

    #reps = [str(x).rjust(2, '0') for x in range(first, last)]
    #fcns = ["Shubert", "Vincent", "CF1", "CF2"]
    #dims = ["2", "3", "4"]
    #mutrates = ["01", "001", "0001", "00001"]
    #tournament_sizes = ["02", "04", "08", "16"]

    parameters = it.product(reps, fcns, dims, mutrates, tournament_sizes)
    for param in parameters:
        rep, fcn, dim, mutrate, tourny = param
        parampath = "SEED_" + rep + "__F_" + fcn + "__D_" + dim + "__MUT_" + mutrate + "__T_" + tourny + "/"
        dirpath = reppath + parampath 
        lodpath = dirpath + lodname 
        eval_lod_fitness(lodpath, fcn_map[fcn])

if __name__=="__main__":
    main()
