# import functions from niching space
from pylandscapes.functions import shubert
from pylandscapes.functions import vincent
from pylandscapes.CF1 import CF1
from pylandscapes.CF2 import CF2

# import other packages
import numpy as np
import csv
import itertools as it
import inspect 

DIMS = [2, 3, 4]

def fcn_pts(dims=3, n=20, precision=3):
    shubert_range = cf1_range = cf2_range = np.round(np.linspace(start=-5, stop=5, num=n), precision)
    vincent_range = np.round(np.linspace(start = 0.25, stop=10.25, num=n), precision)
    

    fcn_pts_dict = {"shubert": it.product(shubert_range, repeat=dims), 
             "vincent": it.product(vincent_range, repeat=dims),
             "CF1": it.product(cf1_range, repeat=dims),
             "CF2": it.product(cf2_range,repeat=dims)}

    return fcn_pts_dict

def fcn_outputs(dims=3, n=20, precision=3, header="", functions=[shubert, vincent, CF1, CF2]):

    assert(dims in DIMS)
    
    fcn_pts_dict = fcn_pts(dims=dims, n=n)

    for fcn in functions:
        fname = "../../data/coords_" + fcn.__name__ + "_" + str(dims) + "D.csv"
        fcoords = list(fcn_pts_dict[fcn.__name__])
        with open(fname, 'w') as f:
            fcn_writer = csv.writer(f, delimiter=",", quotechar='"')
            fcn_writer.writerow(header)
            for coords in fcoords:
                if inspect.isclass(fcn):
                    fitness = round(fcn(dims).evaluate(coords), precision)
                else:
                    fitness = round(fcn(coords), precision)
                row = list(coords) + [fitness]
                fcn_writer.writerow(row)
        print(fname)

fcn_outputs(dims=2, header=["x1", "x2", "fitness"])
fcn_outputs(dims=3, header=["x1", "x2", "x3", "fitness"])
fcn_outputs(dims=4, header=["x1", "x2", "x3", "x4", "fitness"])