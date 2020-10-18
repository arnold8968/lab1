#!/bin/sh 
../../project1/start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /project1/nba_shot/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /project1/nba_shot/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /project1/nba_shot/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../project1/data/Parking_Violation.csv /project1/nba_shot/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file ../../project1/nba_shot/mapper.py -mapper  ../../project1/nba_shot/mapper.py \
-file ../../project1/nba_shot/reducer.py -reducer  ../../project1/nba_shot/reducer.py \
-input /project1/nba_shot/input/* -output /project1/nba_shot/output/   
/usr/local/hadoop/bin/hdfs dfs -cat /project1/nba_shot/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /project1/nba_shot/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /project1/nba_shot/output/
../../project1/stop.sh
