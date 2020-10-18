#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /question4/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /question4/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /question4/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../Parking_Violations_Issued_-_Fiscal_Year_2020.csv /question4/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file ../../part1/question4/mapper.py -mapper ../../part1/question4/mapper.py \
-file ../../part1/question4/reducer.py -reducer ../../part1/question4/reducer.py \
-file ../../part1/question4/combiner.py -combiner ../../part1/question4/combiner.py \
-input /question4/input/* -output /question4/output/
/usr/local/hadoop/bin/hdfs dfs -cat /question4/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /question4/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /question4/output/
../../stop.sh
