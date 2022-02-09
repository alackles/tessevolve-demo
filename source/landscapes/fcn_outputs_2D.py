# import functions from niching space
from functions import shubert
from functions import vincent
from CF3 import CF3
from CF4 import CF4

# import other packages
import numpy as np
import csv

# header for output

header_row = ["x", "y", "fitness"]

# how many points to sample per dimension
# number of points generated is pts^2
pts = 20

# ranges!

shubert_range = np.linspace(start=-5, stop=5, num=pts)
vincent_range = np.linspace(start = 0.25, stop=10.25, num=pts)
cf3_range = np.linspace(start=-5, stop=5, num=pts)
cf4_range = np.linspace(start=-5, stop=5, num=pts)
fcn_range = {"shubert": shubert_range, 
             "vincent": vincent_range,
             "CF3": cf3_range,
             "CF4": cf4_range}

# list the functions that we imported
# but we also need to know which ones need to be handled as classes
functions = [shubert, vincent, CF3, CF4]
classes = [CF3, CF4]

for fcn in functions:
    fname = "../../data/coords_" + fcn.__name__ + "_2D.csv"
    frange = fcn_range[fcn.__name__]
    with open(fname, 'w') as fname:
        fcn_writer = csv.writer(fname, delimiter=",", quotechar='"')
        fcn_writer.writerow(header_row)
        for i in range(pts):
            x = round(frange[i],2)
            for j in range(pts):
                y = round(frange[j],2)
                if fcn in classes:
                    fitness = round(fcn(2).evaluate([x, y]),2)
                else:
                    fitness = round(fcn([x, y]),2)
                fcn_writer.writerow([x, y, fitness])
