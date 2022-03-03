import pandas as pd

from repparse import parameters

def round_nearest(x, nearest=0.5):
    inv = 1/nearest
    return round(x*inv)/inv

def contract_df(df, xcols):
    
    df_round = pd.DataFrame(columns = df.columns)

    # Set the first row in the dataframe to a reference row
    # Start at the second row in the dataframe
    # Compare each row to the reference
    # While each row is identical to the reference row, add the fitness to a cumulative average
    # When the row is new, set that row to the reference,
    #       add the reference row and cumulative average to the rounded dataframe
    # Then return the rounded dataframe

    ref_row = df.iloc[0]
    cur_idx = 1
    
    while cur_idx < len(df.index):
        cumul_fit = ref_row["fitness"]
        cur_row = df.iloc[cur_idx]
        num_ident = 0
        while df.equals(cur_row, ref_row): # this doesn't work; need to check xcols only
            cumul_fit += cur_row["fitness"]
            cur_idx += 1
            num_ident += 1
        fit_avg = cumul_fit/num_ident
        ref_row["fitness"] = fit_avg
        df_round = pd.concat(df_round, ref_row)
    
    return df_round
        
def main():
    params = parameters() 
    lodname = "lod.csv"
    roundname = "lod_round.csv"

    for p in params:
        dirpath = p["path"]
        dim = p["dim"]
        lodpath = dirpath + lodname 
        roundpath = dirpath + roundname

        xcols = ["x" + str(d) for d in range(int(dim))]

        df = pd.read_csv(lodpath)

        for col in xcols:
            df[col] = df[col].apply(round_nearest, args=(0.25,))
        
        df = contract_df(df, xcols)
        
        df.to_csv(roundpath, index=False)


if __name__=="__main__":
    main()