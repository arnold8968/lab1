#!/usr/bin/python
# --*-- coding:utf-8 --*--
import re
import sys

for line in sys.stdin:
    valueString = str(line) # input comes from STDIN(Standard input)
    SingleParkingData = valueString.split(',') # split csv document into different columns
    if len(SingleParkingData[6]) > 0 and len(SingleParkingData[35]) > 0: # cleaning the empty columns and years with value 0
        body = SingleParkingData[6]
        tempYear = SingleParkingData[35]
        try:
            year = int(tempYear) # avoid illegal or wrong input
        except ValueError:
            continue
    
        if(year != 0):
            print('%s\t%s' % (str(year) + '-' + body, 1))
