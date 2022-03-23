import csv
from repparse import parameters

filepath = "./../../data/filenames.csv"
fnames = []

for p in parameters():
    fnames.append(p["path"].split("../")[-1])

print(fnames)

with open(filepath, 'w') as f:
    fwriter = csv.writer(f, delimiter=',')
    fwriter.writerow(fnames)