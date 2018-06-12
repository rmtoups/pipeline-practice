#!/usr/bin/env python

import sys
import os

os.chdir("rmtoups-github")

file = open("file_"+sys.argv[1]+".txt",'w+')
file.write("hello?")
file.close()
print("hello")