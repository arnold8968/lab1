#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /question2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /question2/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /question2/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../Parking_Violations_Issued_-_Fiscal_Year_2020.csv /question2/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file ../../part1/question2/mapper.py -mapper ../../part1/question2/mapper.py \
-file ../../part1/question2/reducer.py -reducer ../../part1/question2/reducer.py \
-file ../../part1/question2/combiner.py -combiner ../../part1/question2/combiner.py \
-input /question2/input/* -output /question2/output/
/usr/local/hadoop/bin/hdfs dfs -cat /question2/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /question2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /question2/output/
../../stop.sh
