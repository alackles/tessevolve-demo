# import functions from niching space
import csv
import inspect
import itertools as iter
import numpy as np

from pylandscapes.cfunctions import CF1, CF2
from pylandscapes.functions import shubert, vincent

DIMS = [2, 3, 4]


def fcn_pts(dims=3, n=21, precision=3):
    shubert_range = cf1_range = cf2_range = np.round(
        np.linspace(start=-5, stop=5, num=n), precision
    )
    vincent_range = np.round(np.linspace(start=0.25, stop=10.25, num=n), precision)

    fcn_pts_dict = {
        "shubert": iter.product(shubert_range, repeat=dims),
        "vincent": iter.product(vincent_range, repeat=dims),
        "CF1": iter.product(cf1_range, repeat=dims),
        "CF2": iter.product(cf2_range, repeat=dims),
    }

    return fcn_pts_dict


def fcn_outputs(dims=3, n=21, precision=3, functions=[shubert, vincent, CF1, CF2]):

    assert dims in DIMS

    fcn_pts_dict = fcn_pts(dims=dims, n=n)

    xcoords = ["x" + str(d) for d in range(dims)]
    if dims==2:
        xcoords.append("x2")
    header = xcoords + ["fitness"]

    for fcn in functions:
        fname = "./data/coords/coords_" + fcn.__name__ + "_" + str(dims) + "D.csv"
        fcoords = list(fcn_pts_dict[fcn.__name__])
        with open(fname, "w") as f:
            fcn_writer = csv.writer(f, delimiter=",", quotechar='"')
            fcn_writer.writerow(header)
            for coords in fcoords:
                if inspect.isclass(fcn):
                    fitness = round(fcn(dims).evaluate(coords), precision)
                else:
                    fitness = round(fcn(coords), precision)
                coords_list = list(coords)
                if dims == 2:
                    coords_list.append(0)
                row = coords_list + [fitness]
                fcn_writer.writerow(row)
        print(fname)


fcn_outputs(dims=2)
fcn_outputs(dims=3)
fcn_outputs(dims=4)
