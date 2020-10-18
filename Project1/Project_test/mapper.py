#!/usr/bin/python
# --*-- coding:utf-8 --*--
import re
import sys

#pat = re.compile('(?P<ip>\d+.\d+.\d+.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*? ')
for line in sys.stdin:
    valueString = line.toString()
    SingleParkingData = valueString.split(',')
    print SingleParkingData[20]