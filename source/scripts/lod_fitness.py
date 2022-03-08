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


def eval_lod_fitness(fname, fcn, precision=3):
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
    with open(fname, "w") as f:
        f.write(header)
        f.writelines(lines)


def main():

    lodname = "lod.csv"

    fcn_map = {"Shubert": shubert, "Vincent": vincent, "CF1": CF1, "CF2": CF2}

    params = parameters()

    for p in params:
        dirpath = p["path"]
        fcn = p["fcn"]
        lodpath = dirpath + lodname
        eval_lod_fitness(lodpath, fcn_map[fcn])
        print(dirpath)


if __name__ == "__main__":
    main()
