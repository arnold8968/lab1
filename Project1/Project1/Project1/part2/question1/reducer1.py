#!/usr/bin/python

#!/usr/bin/env python
import sys
from operator import itemgetter

dict_count = {}
dict_avg = {}

for line in sys.stdin:
    line = line.strip()
    pair, count, avg  = line.split('\t')
    try:
        count = int(count)
        avg = float(avg)
        player, defender = pair.split('--')
        if player in dict_count:
            if defender in dict_count[player]:
                avg_shot = (((dict_count[player][defender])*1.0*(dict_avg[player][defender])) + (count*1.0*avg)) / (dict_count[player][defender] + count)
                dict_avg[player][defender] = avg_shot
                dict_count[player][defender] = dict_count[player][defender] + count
            else:
                avg_shot = (count*1.0*avg) / count
                dict_avg[player][defender] = avg_shot
                dict_count[player][defender] = count
        else:
            dict_avg[player] = {}
            dict_count[player] = {}
            avg_shot = (count*1.0*avg) / count
            dict_avg[player][defender] = avg_shot
            dict_count[player][defender] = count
    except ValueError:
        pass

sorted_count = sorted(dict_count.items(), key=itemgetter(0))
for players,defenders in sorted_count:
    for d in defenders:
        print('%s\t%s\t%s' % (players + '--' + d, dict_count[players][d], dict_avg[players][d]))
