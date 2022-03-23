#  @file  lod_fitness.py
#  @brief Take the generated lod files and run them through the fitness functions to append fitness to them
# import functions from niching space

import inspect

from pylandscapes.cfunctions import CF1, CF2
from pylandscapes.functions import shubert, vincent
from repparse import parameters


def parse_line(line):
    return [
        float(x) for x in line.strip().split(",")[1:]
    ]  # get only the parts that are the actual input


def eval_lod_fitness(path, fcn, infile="lod_init.csv", outfile="lod_fit.csv", precision=3):
    fname = path + infile
    with open(fname, "r") as f:
        header = f.readline().strip() + ",fitness\n"  # skip header and append fitness
        lines = f.readlines()  # get every line
        for i, line in enumerate(lines):
            fcn_input = parse_line(line)
            dims = len(fcn_input)
            if inspect.isclass(fcn):
                fitness = round(fcn(dims).evaluate(fcn_input), precision)
            else:
                fitness = round(fcn(fcn_input), precision)
            lines[i] = line.strip() + "," + str(fitness) + "\n"
    outname = path + outfile
    with open(outname, "w") as f:
        f.write(header)
        f.writelines(lines)


def main():

    fcn_map = {"shubert": shubert, "vincent": vincent, "CF1": CF1, "CF2": CF2}

    params = parameters()

    for p in params:
        dirpath = p["path"]
        fcn = p["fcn"]
        eval_lod_fitness(path=dirpath, fcn=fcn_map[fcn])
        print(dirpath)


if __name__ == "__main__":
    main()
