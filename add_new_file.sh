#!/bin/sh
cd updated-github

git config --global user.email "rmtoups@gmail.com"
git config --global user.name "rmtoups"

git add *.txt
git commit -m "added new text file"