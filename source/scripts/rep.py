#
#  @note This file is part of MABE, https://github.com/mercere99/MABE2
#  @copyright Copyright (C) Michigan State University, MIT Software license; see doc/LICENSE.md
#  @date 2021
#
#  @file  rep.py
#  @brief Quick & dirty way to run multiple replicates in MABE and save the data.
#  TODO: parallelize (or just extend into an actual MABE2 functionality)

import os
from pathlib import Path

from repparse import parameters

def buildmabe(buildpath):
  os.system("cd " + buildpath + "&& make clean && make && cd ../../../scripts/")

def runmabe(exec, mabefile, params):
  # exec: path to MABE executable
  # params: command-line parameters
  # first: first replicate
  # last: last replicate (works like python, so not inclusive)
  os.system(exec + " -f " + mabefile + " -s " + params)

def make_settings(param, mabepath):


  reppath = param["path"]
  seed = str(int(param["rep"])) # remove leading 0s
  fcn = param["fcn"]
  dim = param["dim"]
  mutrate = param["mutrate"][0] + "." + param["mutrate"][1:]
  tourny = str(int(param["tourny"])) # remove leading 0s
  
  datpath = mabepath + "source/tools/DataGECCO/" # path for GECCO niching function .dat file

  fcn_range = {
    "shubert": (-5, 5), 
    "vincent": (0.5, 10.5), 
    "CF1": (-5, 5), 
    "CF2": (-5, 5)
    }

  fcn_min = fcn_range[param["fcn"]][0]
  fcn_max = fcn_range[param["fcn"]][1]

  settings = []
  
  # RANDOM SEED
  settings.append('random_seed=\\"' + seed + '\\"')
  
  # OUTPUT
  settings.append('output.filename=\\"' + reppath + 'output.csv\\"')
  
  # TOURNAMENT SIZE
  settings.append('select_tourny.tournament_size=\\"' + tourny + '\\"')
 
  
  # EVAL_GECCO
  settings.append('eval_gecco.fcn_name=\\"' + fcn + '\\"')      # function of interest
  settings.append('eval_gecco.dims=\\"' + dim + '\\"')          # how many dimensions
  settings.append('eval_gecco.dat_path=\\"' + datpath + '\\"')           # where data is stored
  
  # VALS_ORG
  settings.append('vals_org.N=\\"' + dim + '\\"')                  # number of dimensions
  settings.append('vals_org.min_value=\\"' + str(fcn_min) + '\\"')          # min function value
  settings.append('vals_org.max_value=\\"' + str(fcn_max) + '\\"')          # max function value
  settings.append('vals_org.mut_size=\\"' + mutrate + '\\"')       # mutation 'rate' (size)
  settings.append('vals_org.mut_prob=\\"' + str(1) + '\\"')       # mutation 'prob' (always on)

  # SYSTEMATICS MANAGER
  settings.append('sys.snapshot_file_root_name=\\"' + reppath + 'phylogeny\\"')
  settings.append('sys.data_file_name=\\"' + reppath + 'phylogenetic_data.csv\\"')

  return "\;".join(settings) 

def main():

  mabepath = "./../third-party/MABE2/" # path for MABE2 repository
  mabefile = mabepath + "settings/GECCO.mabe" # path for .mabe config file (old)

  buildpath = mabepath + "build/" # path for MABE2 build folder
  runfile = buildpath + "MABE" # path for MABE executable

  params = parameters()

  buildmabe(buildpath)

  for param in params:
    Path(param["path"]).mkdir(parents=True, exist_ok=True)
    setting = make_settings(param, mabepath)
    runmabe(runfile, mabefile, setting)

if __name__=="__main__":
  main()