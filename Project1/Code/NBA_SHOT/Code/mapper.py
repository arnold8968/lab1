#!/usr/bin/python
# --*-- coding:utf-8 --*--
import re
import sys

for line in sys.stdin:
    valueString = str(line) # input comes from STDIN(Standard input)
    shot_df = valueString.split(',') # split csv document into different columns
    
    if len(shot_df[8]) > 0: # cleaning the empty columns, SHOT_CLOCK is 20th columns
        
#        time = SingleParkingData[20]
#        try:
#            hour = int(time[0:2]) # avoid illegal or wrong input
#        except ValueError:
#            continue
#        complete =  lambda x: 12 if (x[-1] == 'P') else 0 # exchange A and P into 24th hour scale
#        
#        hours = hour + complete(time)
        
#       player_id        20
#        CLOSEST_DEFENDER_PLAYER_ID 15
#        SHOT_RESULT  13
        play_id = shot_df[20]
        defender_id = shot_df[15]
        shot_result = shot_df[13]
        print "%d\t%d\t%s" % (play_id, defender_id, shot_result)