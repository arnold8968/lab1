#!/usr/bin/env python
import sys
from collections import Counter

dict_parking_count = {}

for line in sys.stdin:
    line = line.strip()
    time, num = line.split('\t')
    try:
        num = int(num)
        dict_parking_count[time] = dict_parking_count.get(time, 0) + num # save time and num in the dictionary
    
    except ValueError:
        pass

for i in dict_parking_count:
    print('%s\t%s' % (i, dict_parking_count[i]))
