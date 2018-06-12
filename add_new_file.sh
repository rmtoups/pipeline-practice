#!/bin/sh

ls
git config --global user.email "rmtoups@gmail.com"
git config --global user.name "rmtoups"

git add .
git status
git commit -m "added new text file"
git push