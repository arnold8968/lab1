#!/usr/bin/env python
import sys
from collections import Counter
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
            if defender not in dict_count[player]:
                dict_avg[player][defender] = avg
                dict_count[player][defender] = count
        else:
            dict_avg[player] = {}
            dict_count[player] = {}
            dict_avg[player][defender] = avg
            dict_count[player][defender] = count
    except ValueError:
        pass


for players,defenders in dict_avg.items():
    count_dict = Counter(defenders)
    top_dict = count_dict.most_common()[:-2:-1]
    for i in top_dict:
        print('%s\t%s\t%s' % (players + "--" + i[0], dict_count[players][i[0]], i[1]))
