#!/usr/bin/env python

import sys
import os

os.listdir()

os.chdir("rmtoups-github")

os.getcwd()

file = open("file_"+sys.argv[1]+".txt",'w+')
file.write("hello?")
file.close()

os.listdir()

print("hello")