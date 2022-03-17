proj_path <- "/home/acacia/Documents/research/project-viz-3D/"
data_path <- paste(proj_path, "data/", sep="")

library(dplyr)
library(tidyr)

fcns <- c("coords_CF1_4D.csv", "coords_CF2_4D.csv", "coords_shubert_4D.csv", "coords_vincent_4D.csv")

proc_4D <- function(fname) {
  fpath = paste(data_path, fname, sep="")
  df <- read.csv(fpath) %>%
    pivot_wider(
      names_from=x3, 
      values_from=fitness,
      names_prefix="fitness")
  write.csv(x=df, file=fpath, row.names = FALSE, quote = FALSE)
  return(fpath)
}

lapply(fcns, proc_4D)

