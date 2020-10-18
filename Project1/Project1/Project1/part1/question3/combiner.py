#!/usr/bin/env python

from operator import itemgetter
import sys
from collections import Counter

street_num_dict = {}
for line in sys.stdin:
    line = line.strip()
    streetcode, num = line.split('\t')
    try:
       num = int(num)
       street_num_dict[streetcode] = street_num_dict.get(streetcode,0) + num   
    except ValueError:
       pass
for streetcode in street_num_dict:
    print '%s\t%s'% (streetcode, street_num_dict[streetcode])
