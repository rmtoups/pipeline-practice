#!/bin/sh
git clone rmtoups-github updated-github
pwd
# ls
# cd rmtoups-github
# ls
# cd ..
# ls
cd updated-github
ls
#cd rmtoups-github
./create-file.py
git config --global user.email "rmtoups@gmail.com"
git config --global user.name "rmtoups"

git add .
git status
git commit -m "added new text file"
#git push