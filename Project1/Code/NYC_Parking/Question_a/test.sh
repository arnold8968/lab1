#!/bin/sh 
../../project1/start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /project1/parking3_1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /project1/parking3_1/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /project1/parking3_1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../project1/data/Parking_Violation.csv /project1/parking3_1/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file ../../project1/parking3_1/mapper.py -mapper  ../../project1/parking3_1/mapper.py \
-file ../../project1/parking3_1/reducer.py -reducer  ../../project1/parking3_1/reducer.py \
-file ../../project1/parking3_1/combiner.py -combiner  ../../project1/parking3_1/combiner.py \
-input /project1/parking3_1/input/* -output /project1/parking3_1/output/   
/usr/local/hadoop/bin/hdfs dfs -cat /project1/parking3_1/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /project1/parking3_1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /project1/parking3_1/output/
../../project1/stop.sh
