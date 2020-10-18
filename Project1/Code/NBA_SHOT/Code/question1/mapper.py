#!/usr/bin/python
# --*-- coding:utf-8 --*--
import re
import sys

for line in sys.stdin:
    valueString = str(line) # input comes from STDIN(Standard input)
    shot_df = valueString.split(',') # split csv document into different columns
    play_id = shot_df[20]
    defender_id = shot_df[15]
    shot_result = shot_df[13]
#    2225	tony parker	101108	Paul, Chris

    if play_id == 2225 and defender_id == 101108:
        print('%d\t%d\t%s' % (play_id, defender_id, shot_result))