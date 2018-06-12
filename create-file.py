#!/usr/bin/env python

import sys

file = open("updated-github/file_"+sys.argv[1]+".txt",'w+')
file.close()
print("hello")