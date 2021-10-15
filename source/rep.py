#
#  @note This file is part of MABE, https://github.com/mercere99/MABE2
#  @copyright Copyright (C) Michigan State University, MIT Software license; see doc/LICENSE.md
#  @date 2021
#
#  @file  rep.py
#  @brief Quick & dirty way to run multiple replicates in MABE and save the data.
#

import os
from pathlib import Path 

buildpath = "./third-party/MABE2/build/"
runpath = buildpath + "MABE"
reppath = "../data/reps/"

genfile = "./third-party/MABE2/settings/GECCO.gen"
mabefile = "./third-party/MABE2/settings/GECCO.mabe"

firstrep = 0
lastrep = 100
fcns = {"Shubert": (-5, 5), 
  "Vincent": {0.25, 10.25}, 
  "CF3": (-5, 5), 
  "CF4": (-5, 5)}

digs = len(str(lastrep-firstrep))

# clean build of MABE
os.system("cd " + buildpath + "&& make clean && make && cd ../../../")

for fcn, minmax in fcns.items():
  minval = minmax[0]
  maxval = minmax[1]
  for rep in range(firstrep, lastrep):
      # random seeds and folder creation
      randseed = rep
      dirname = reppath + "SEED_" + str(randseed).rjust(digs, '0') + "__F_" + fcn + "/" 
      print(dirname)
      Path(dirname).mkdir(parents=True, exist_ok=True)

      #variables 
      fcn_var = 'eval_gecco.fcn_name=\\"' + fcn
      min_var = 'vals_org.min_value=\\"' + str(minval)
      max_var = 'vals_org.max_value=\\"' + str(maxval)

      randseed_var = "random_seed=" + str(randseed)
      outpath_var = 'output.filename=\\"' + dirname + 'output.csv\\"'
      genpath_var = 'eval_nkmixed.genome_file=\\"' + dirname + 'genome.csv\\"'

      settings = fcn_var + "\;" + min_var + "\;" + max_var + "\;" +randseed_var + "\;" + outpath_var + "\;" + genpath_var
      os.system(runpath + " -f " + mabefile + " -s " + settings)