#!/usr/bin/python
# --*-- coding:utf-8 --*--
import re
import sys

for line in sys.stdin:
    valueString = str(line) # input comes from STDIN(Standard input)
    SingleParkingData = valueString.split(',') # split csv document into different columns
    if len(SingleParkingData[34]) > 0: # cleaning the empty columns, VEHICLE COLOR is 34th columns
        color = SingleParkingData[34]
#        try:
#            hour = int(time[0:2]) # avoid illegal or wrong input
#        except ValueError:
#            continue
#        complete =  lambda x: 12 if (x[-1] == 'P') else 0 # exchange A and P into 24th hour scale
        
#        hours = hour + complete(time)
        print "%s\t%s" % (color, 1)