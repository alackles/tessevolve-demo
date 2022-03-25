library(dplyr)
library(tidyr)

proj_path <- "/home/acacia/Documents/research/tessevolve/"
fnames_path <- paste(proj_path, "data/filenames.csv", sep="")
rep_paths <- paste(proj_path, as.list(read.csv(fnames_path, header=F)),sep="")
files <- paste(rep_paths, "lod_round.csv", sep="") 

proc_4D <- function(fname) {
  df <- read.csv(fname)
  if (grepl("D_4", fname)) {
    df <- df %>%
      pivot_wider(
        names_from=x3, 
        values_from=fitness,
        names_prefix="fitness"
      )
  } 
  stripped_name <- unlist(strsplit(fname, split="_round.csv"))
  outname <- paste0(stripped_name, ".csv")
  write.csv(x=df, file=outname, row.names = FALSE, quote = FALSE)
  return(outname)
}

lapply(files, proc_4D)
