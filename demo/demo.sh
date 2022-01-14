#!/bin/bash

# Bash script to zip up HTML, JS, and CSV files
#  which can then be fully unzipped into a working demo
# 
# This is helpful if you want to demo things yourself
#  without worrying too much about what's going on in the
#  rest of the files, and also to sync the latest changes
#  in here with the demo hosted at 
#  https://alackles.github.io/landscapes
# 
# It does NOT include the index.html
#  because the demo has a different landing page

rm demo.zip
zip -r0 demo.zip ../source/*.html ../source/pages/*.js ../data/*