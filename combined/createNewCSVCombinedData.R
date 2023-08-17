# read in all the CSVs with the combined data
two <- read.csv('combined_data_2D.csv')
three <- read.csv('combined_data_3D.csv')
four <- read.csv('combined_data_4D_without_vincent.csv')

# combine the the above files (four is not working)
combined_allResults_minus_4D_data <- rbind(two, three)
write.csv(combined_allResults_minus_4D_data, "combined_allResults_minus_4D_data.csv", row.names = FALSE)