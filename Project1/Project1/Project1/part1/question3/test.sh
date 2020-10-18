#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /question3/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /question3/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /question3/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../Parking_Violations_Issued_-_Fiscal_Year_2020.csv /question3/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file ../../part1/question3/mapper.py -mapper ../../part1/question3/mapper.py \
-file ../../part1/question3/reducer.py -reducer ../../part1/question3/reducer.py \
-file ../../part1/question3/combiner.py -combiner ../../part1/question3/combiner.py \
-input /question3/input/* -output /question3/output/
/usr/local/hadoop/bin/hdfs dfs -cat /question3/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /question3/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /question3/output/
../../stop.sh

