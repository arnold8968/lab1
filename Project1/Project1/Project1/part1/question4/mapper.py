#!/usr/bin/python
# --*-- coding:utf-8 --*--
import re
import sys

for line in sys.stdin:
    valueString = str(line) # input comes from STDIN(Standard input)
    SingleParkingData = valueString.split(',') # split csv document into different columns
    if len(SingleParkingData[33]) > 0: # cleaning the empty columns, VEHICLE COLOR is 34th columns
        color = SingleParkingData[33]
        print "%s\t%s" % (color, 1)
