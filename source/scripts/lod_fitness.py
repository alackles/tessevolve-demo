#  @file  lod_fitness.py
#  @brief Take the generated lod files and run them through the fitness functions to append fitness to them 
# import functions from niching space

from pylandscapes.functions import shubert
from pylandscapes.functions import vincent
from pylandscapes.cfunctions import CF1
from pylandscapes.cfunctions import CF2
import inspect
import itertools as it

def parse_line(line):
    return [float(x) for x in line.strip().split(",")[1:]] # get only the parts that are the actual input 

def eval_lod_fitness(fname, fcn, precision=3):
    with open(fname, 'r') as f:
        header = f.readline().strip() + ",fitness\n" # skip header and append fitness
        lines = f.readlines() # get every line
        for i, line in enumerate(lines):
            fcn_input = parse_line(line)
            dims = len(fcn_input)
            if inspect.isclass(fcn):
                fitness = round(fcn(dims).evaluate(fcn_input), precision)
            else:
                fitness = round(fcn(fcn_input), precision)
            lines[i] = line.strip() + "," + str(fitness) + "\n"
    with open(fname, "w") as f:
        f.write(header)
        f.writelines(lines)
        

def main():

    # reps
    first = 0
    last = 2

    datapath = "./../../data/"
    reppath = datapath + "reps/"

    lodname = "lod.csv"

    fcn_map = {
        "Shubert": shubert,
        "Vincent": vincent,
        "CF1": CF1,
        "CF2": CF2
    }

    reps = [str(x).rjust(2, '0') for x in range(first, last)]
    fcns = ["Shubert", "Vincent", "CF1", "CF2"]
    dims = ["2", "3", "4"]
    mutrates = ["01", "001", "0001", "00001"]
    tournament_sizes = ["02", "04", "08", "16"]

    parameters = it.product(reps, fcns, dims, mutrates, tournament_sizes)
    for param in parameters:
        rep, fcn, dim, mutrate, tourny = param
        parampath = "SEED_" + rep + "__F_" + fcn + "__D_" + dim + "__MUT_" + mutrate + "__T_" + tourny + "/"
        dirpath = reppath + parampath 
        lodpath = dirpath + lodname 
        eval_lod_fitness(lodpath, fcn_map[fcn])
        print(dirpath)

if __name__=="__main__":
    main()
