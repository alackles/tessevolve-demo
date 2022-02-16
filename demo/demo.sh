#!/bin/bash

# Bash script to zip up HTML, JS, and CSV files
#  which can then be fully unzipped into a working demo
# 
# This is helpful if you want to demo things yourself
#  without worrying too much about what's going on in the
#  rest of the files, and also to sync the latest changes
#  in here with the demo hosted at 
#  https://alackles.github.io/landscapes

rm demo.zip
zip -r0 demo.zip index.html ../source/pages/landscape.js ../source/js/* ../source/css/* ../data/reps/*/edges.csv ../data/reps/*/lod.csv 