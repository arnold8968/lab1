#!/usr/bin/python

#!/usr/bin/env python
import sys
from collections import Counter

dict_parking_count = {}

for line in sys.stdin:
    line = line.strip()
    play_id, defender_id, shot_resul = line.split('\t')
    try:
        num = int(num)
        dict_parking_count[time] = dict_parking_count.get(time, 0) + num # save time and num in the dictionary 
    
    except ValueError:
        pass

count_dict = Counter(dict_parking_count)
top_dict = count_dict.most_common(3) # choose the top 3
for i in top_dict:
    print '%s\t%s' % (i[0], i[1])