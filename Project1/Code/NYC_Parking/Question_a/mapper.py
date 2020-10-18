#!/usr/bin/python
# --*-- coding:utf-8 --*--
import re
import sys

for line in sys.stdin:
    valueString = str(line) # input comes from STDIN(Standard input)
    SingleParkingData = valueString.split(',') # split csv document into different columns
    if len(SingleParkingData[20]) > 0: # cleaning the empty columns, Violation Time is 20th columns
        time = SingleParkingData[20]
        try:
            hour = int(time[0:2]) # avoid illegal or wrong input
        except ValueError:
            continue
        complete =  lambda x: 12 if (x[-1] == 'P') else 0 # exchange A and P into 24th hour scale
        
        hours = hour + complete(time)
        print "%s\t%s" % (str(hours) + ':' + '00', 1)