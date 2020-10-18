#!/usr/bin/python

#!/usr/bin/env python
import sys
from collections import Counter

#dict_parking_count = {}
made = 0
total = 0

for line in sys.stdin:
    line = line.strip()
    play_id, defender_id, shot_result = line.split('\t')
    try:
        if shot_result == 'made':# count the number of made 
            made += 1
        total += 1
    except ValueError:
        pass

print('%s' % (made / total))