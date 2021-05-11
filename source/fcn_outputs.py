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
shubert_x = np.linspace(start=-10, stop=10, num=pts)
shubert_y = np.linspace(start=-10, stop=10, num=pts)
shubert_z = np.linspace(start=-10, stop=10, num=pts)

with open(shubert_file, 'w') as f:
    shubert_writer = csv.writer(f, delimiter=",",quotechar='"')
    shubert_writer.writerow(header_row)
    for i in range(0, pts):
        x = shubert_x[i]
        y = shubert_y[i]
        z = shubert_z[i]
        fitness = shubert([x, y, z])
        shubert_writer.writerow([x, y, z, fitness])