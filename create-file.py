#!/usr/bin/env python

import sys
import os

ls = os.listdir()
print(ls)
if 'updated-github' not in ls:
	os.mkdir("updated-github")
os.chdir("updated-github")
print(os.listdir())

cwd = os.getcwd()
print(cwd)

file = open("file_"+sys.argv[1]+".txt",'w+')
file.write("hello?")
file.close()

ls2 = os.listdir()
print(ls2)

print("hello")