import itertools as iter

def parameters(first=0, last=2):

    # List of dictionaries of parameters
    params = []

    # reps
    datapath = "./../../data/"
    reppath = datapath + "reps/"

    reps = [str(x).rjust(2, '0') for x in range(first, last)]
    fcns = ["Shubert", "Vincent", "CF1", "CF2"]
    dims = ["2", "3", "4"]
    mutrates = ["01", "001", "0001", "00001"]
    tournament_sizes = ["02", "04", "08", "16"]

    parameters = iter.product(reps, fcns, dims, mutrates, tournament_sizes)
    for param in parameters:
        info = {}
        rep, fcn, dim, mutrate, tourny = param
        parampath = "SEED_" + rep + "__F_" + fcn + "__D_" + dim + "__MUT_" + mutrate + "__T_" + tourny + "/"
        dirpath = reppath + parampath 
        info["path"] = dirpath
        info["fcn"] = fcn
        info["dim"] = dim
        params.append(info)
    
    return params