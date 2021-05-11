# import functions from niching space
from niching.python3.cec2013.functions import shubert
from niching.python3.cec2013.functions import vincent
from niching.python3.cec2013.CF3 import CF3
from niching.python3.cec2013.CF4 import CF4

# import other packages
import numpy as np
import csv

# filenames

shubert_file = "../data/shubert.csv"
vincent_file = "../data/vincent.csv"
cf3_file = "../data/cf3.csv"
cf4_file = "../data/cf4.csv"

# other globals

header_row = ["x", "y", "z", "fitness"]

# how many points to sample
pts = 10

# ranges!

shubert_range = np.linspace(start=-10, stop=10, num=pts)
vincent_range = np.linspace(start = 0.25, stop=10.25, num=pts)

fcn_range = {"shubert": shubert_range, "vincent": vincent_range}
functions = [shubert, vincent]

for fcn in functions:
    fname = "../data/" + fcn.__name__ + ".csv"
    frange = fcn_range[fcn.__name__]
    with open(fname, 'w') as fname:
        fcn_writer = csv.writer(fname, delimiter=",", quotechar='"')
        fcn_writer.writerow(header_row)
        for i in range(pts):
            x = y = z = frange[i]
            fitness = fcn([x, y, z])
            fcn_writer.writerow([x, y, z, fitness])
    