#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    columns = line.split(',')
    if len(columns[14]) >0:
        try:
           streetnum = int(columns[14])
           if streetnum >0:
              print  "%s\t%s" % (columns[14],1)
        except ValueError:
           pass
        
