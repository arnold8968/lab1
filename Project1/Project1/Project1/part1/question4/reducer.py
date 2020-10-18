#!/usr/bin/python
import sys
from collections import Counter

dict_parking_count = {}

for line in sys.stdin:
    line = line.strip()
    color, num = line.split('\t')
    try:
        num = int(num)
        dict_parking_count[color] = dict_parking_count.get(color, 0) + num # save time and num in the dictionary
    
    except ValueError:
        pass

count_dict = Counter(dict_parking_count)
top_dict = count_dict.most_common(3) # choose the top 3
for i in top_dict:
    print '%s\t%s' % (i[0], i[1])
