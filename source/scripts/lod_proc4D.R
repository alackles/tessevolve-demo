library(dplyr)
library(tidyr)

proj_path <- "/home/acacia/Documents/research/project-viz-3D/"
fnames_path <- paste(proj_path, "data/filenames.csv", sep="")
rep_paths <- paste(proj_path, as.list(read.csv(fnames_path, header=F)),sep="")
files <- paste(rep_paths, "lod_md.csv", sep="") %>% .[matches("D_4", vars=.)] # https://stackoverflow.com/questions/44169164/dplyr-filter-on-a-vector-rather-than-a-dataframe-in-r

proc_4D <- function(fname) {
  df <- read.csv(fname) %>%
    pivot_wider(
      names_from=x3, 
      values_from=fitness,
      names_prefix="fitness")
  write.csv(x=df, file=fname, row.names = FALSE, quote = FALSE)
  return(fname)
}

lapply(files, proc_4D)
