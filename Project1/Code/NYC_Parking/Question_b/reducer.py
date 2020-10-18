#!/usr/bin/python

#!/usr/bin/env python
import sys
from collections import Counter

dict_body_year_count = {}

for line in sys.stdin:
    line = line.strip()
    body_year, num = line.split('\t')
    try:
        num = int(num)
        dict_body_year_count[body_year] = dict_body_year_count.get(body_year, 0) + num # save body_year and num in the dictionary
    
    except ValueError:
        pass

count_dict = Counter(dict_body_year_count)
top_dict = count_dict.most_common(3) # choose the top 3
for i in top_dict:
    print('%s\t%s' % (i[0], i[1]))
