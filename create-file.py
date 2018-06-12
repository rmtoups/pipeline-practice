#!/usr/bin/env python

import sys
import os

ls = os.listdir()
print(ls)

os.chdir("rmtoups-github")

cwd = os.getcwd()
print(cwd)

file = open("file_"+sys.argv[1]+".txt",'w+')
file.write("hello?")
file.close()

os.listdir()

print("hello")