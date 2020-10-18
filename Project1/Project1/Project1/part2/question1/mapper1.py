#!/usr/bin/python
# --*-- coding:utf-8 --*--
import re
import sys

for line in sys.stdin:
    valueString = str(line) # input comes from STDIN(Standard input)
    SingleShotData = valueString.split(',') # split csv document into different columns
    if len(SingleShotData) == 23:
        if len(SingleShotData[14])>0 and len(SingleShotData[15])>0 and len(SingleShotData[16])>0 and len(SingleShotData[21])>0:
            player = SingleShotData[21]
            defenderLastName = SingleShotData[15]
            defenderFirstName = SingleShotData[16]
            defender = defenderLastName + ', ' + defenderFirstName
            defender = defender.strip('\"')
            if SingleShotData[14] == "made":
                shot = 1
            else:
                shot = 0
            print('%s\t%s\t%s' % (player + '--' + defender, 1, shot))
