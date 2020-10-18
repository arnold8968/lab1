#!/usr/bin/python

#!/usr/bin/env python
import sys
from collections import Counter
from operator import itemgetter

dict_body_year_count = {}

for line in sys.stdin:
    line = line.strip()
    body_year, num = line.split('\t')
    try:
        num = int(num)
        dict_body_year_count[body_year] = dict_body_year_count.get(body_year, 0) + num # save body_year and num in the dictionary
    
    except ValueError:
        pass


sorted_dict_count = sorted(dict_body_year_count.items(), key=itemgetter(0))
for bodyYear, count in sorted_dict_count:
    print '%s\t%s' % (bodyYear, count)
