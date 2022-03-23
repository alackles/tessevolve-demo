library(dplyr)
library(tidyr)

proj_path <- "/home/acacia/Documents/research/project-viz-3D/"
tempdata_path <-paste(proj_path, "source/scripts/data/coords/", sep="")
data_path <- paste(proj_path, "data/coords/", sep="")

fcn_names <- c("shubert", "vincent", "CF1", "CF2")

coords_2D <- paste("coords_", fcn_names, "_2D.csv", sep="")
coords_3D <- paste("coords_", fcn_names, "_3D.csv", sep="")
coords_4D <- paste("coords_", fcn_names, "_4D.csv", sep="")

# just passing through
move_coords <- function(fname) {
  inpath <- paste(tempdata_path, fname, sep="")
  outpath <- paste(data_path, fname, sep="")
  df <- read.csv(inpath)
  write.csv(x=df, file=outpath, row.names=F, quote=F)
}

# doing some actual processing
proc_4D <- function(fname) {
  inpath <- paste(tempdata_path, fname, sep="")
  outpath <- paste(data_path, fname, sep="")
  df <- read.csv(inpath) %>%
    pivot_wider(
      names_from=x3, 
      values_from=fitness,
      names_prefix="fitness")
  write.csv(x=df, file=outpath, row.names = FALSE, quote = FALSE)
  return(outpath)
}

lapply(coords_2D, move_coords)
lapply(coords_3D, move_coords)
lapply(coords_4D, proc_4D)

