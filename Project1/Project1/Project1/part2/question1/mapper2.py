#!/usr/bin/python
# --*-- coding:utf-8 --*--
import re
import sys

for line in sys.stdin:
    line = line.strip() # input comes from STDIN(Standard input)
    pair, count, avg = line.split('\t') # split line
    if int(count) > 5:
        print('%s\t%s\t%s' % (pair, count, avg))
