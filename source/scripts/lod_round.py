import pandas as pd

from repparse import parameters

def round_nearest(x, nearest=0):
    if nearest == 0:
        return round(x)
    inv = 1/nearest
    return round(x*inv)/inv

def contract_df(df, xcols):

    dfx = df.copy() # Best practice

    df_round = pd.DataFrame(columns = dfx.columns)

    # Set the first row in the dataframe to a reference row
    # Start at the second row in the dataframe
    # Compare each row to the reference
    # While each row is identical to the reference row, add the fitness to a cumulative average
    # When the row is new, set that row to the reference,
    #       add the reference row and cumulative average to the rounded dataframe
    # Then return the rounded dataframe

    ref_row = dfx.iloc[[0]]
    cur_idx = 1
    cur_row = dfx.iloc[[cur_idx]].reset_index(drop=True)
    
    while cur_idx < len(dfx.index):
        cumul_fit = ref_row.at[0, "fitness"]
        num_ident = 1
        while ref_row[xcols].equals(cur_row[xcols]): 
            cumul_fit += cur_row.at[0, "fitness"]
            num_ident += 1
            cur_idx += 1
            try: 
                cur_row = dfx.iloc[[cur_idx]].reset_index(drop=True) 
            except IndexError: # When we hit the last row in the dataframe
                break
        fit_avg = cumul_fit/num_ident
        ref_row.at[0, "fitness"] = fit_avg
        df_round = pd.concat([df_round, ref_row])
        ref_row = cur_row
    
    return df_round.reset_index(drop=True)
 
def main():
    params = parameters() 
    lodname = "lod_fit.csv"

    for p in params:
        dirpath = p["path"]
        dim = p["dim"]
        lodpath = dirpath + lodname 

        xcols = ["x" + str(d) for d in range(int(dim))]

        df = pd.read_csv(lodpath)
        df_round = df.copy()
        
        roundname = "lod_round.csv"
        roundpath = dirpath + roundname

        for col in xcols:
            df_round[col] = df_round[col].apply(round_nearest, args=(0.5,))
    
        df_round = contract_df(df_round, xcols)

        df_round.to_csv(roundpath, index=False)

        print(dirpath)

if __name__=="__main__":
    main()