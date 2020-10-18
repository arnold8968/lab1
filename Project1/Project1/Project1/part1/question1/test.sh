#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /question1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /question1/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /question1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../Parking_Violations_Issued_-_Fiscal_Year_2020.csv /question1/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file ../../part1/question1/mapper.py -mapper ../../part1/question1/mapper.py \
-file ../../part1/question1/reducer.py -reducer ../../part1/question1/reducer.py \
-file ../../part1/question1/combiner.py -combiner ../../part1/question1/combiner.py \
-input /question1/input/* -output /question1/output/
/usr/local/hadoop/bin/hdfs dfs -cat /question1/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /question1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /question1/output/
../../stop.sh
