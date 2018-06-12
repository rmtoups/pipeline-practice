#!/usr/bin/env python

import sys
import os

ls = os.listdir()
print(ls)

os.chdir("updated-github")

cwd = os.getcwd()
print(cwd)

file = open("file_"+sys.argv[1]+".txt",'w+')
file.write("hello?")
file.close()

ls2 = os.listdir()
print(ls2)

print("hello")