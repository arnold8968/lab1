#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 16:56:59 2020

@author: james
"""

from __future__ import print_function

import sys
from operator import add

from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
import re
from collections import Counter
import pandas as pd


# df = sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true').load('cars.csv')
# df.select('year', 'model').write.format('com.databricks.spark.csv').save('newcars.csv')

sys.setdefaultencoding('utf8')
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        sys.exit(-1)

    spark = SparkSession\
        .builder\
        .appName("PythonWordCount")\
        .getOrCreate()

    df = spark.read.format("csv").options(header='true', inferschema='true').load(sys.argv[1])

    dict_word = {}
    csv_words = df['review_text'].apply(lambda x: re.sub(r'[^\w\s]','', x))
    
    for line in csv_words:
        word = line.split(' ')
        for i in word:
            try:
                if len(i) > 0:
                    # word_list.append(i)
                    dict_word[i] = dict_word.get(i, 0) + 1
            except:
                pass
    
    count_dict = Counter(dict_word)
    output = count_dict.most_common(50)
    
    outputdf = df.DataFrame(dict_word)
    df.write.format('com.databricks.spark.csv').save('wordcountoutput.csv')


    for (word, count) in output:
        print("%s: %i" % (word, count))

    spark.stop()