#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /question1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /question1/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /question1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../shot_logs.csv /question1/input/

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file ../../part2/question1/mapper1.py -mapper ../../part2/question1/mapper1.py \
-file ../../part2/question1/reducer1.py -reducer ../../part2/question1/reducer1.py \
-input /question1/input/* -output /question1/output/result1/

/usr/local/hadoop/bin/hdfs dfs -mv /question1/output/result1/part-00000 /question1/input/result1.txt

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file ../../part2/question1/mapper2.py -mapper ../../part2/question1/mapper2.py \
-file ../../part2/question1/reducer2.py -reducer ../../part2/question1/reducer2.py \
-input /question1/input/result1.txt -output /question1/output/result2/

/usr/local/hadoop/bin/hdfs dfs -cat /question1/output/result2/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /question1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /question1/output/*
../../stop.sh
