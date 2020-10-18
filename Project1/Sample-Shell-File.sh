#!/bin/sh

../start.sh

/usr/local/hadoop/bin/hdfs dfs -rm -r /nba/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /nba/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /nba/input/
/usr/local/hadoop/bin/hdfs dfs copyFromLocal /project1/nba/part2/data/* /nba/input/

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
			     -file /project1/nba/part2/mapper_init_centroids.py \
			     -mapper "/project1/nba/part2/mapper_init_centroids.py $1" \
			     -file /project1/nba/part2/reducer_init_centroids.py \
			     -reducer /project1/nba/part2/reducer_init_centroids.py \
			     -input /nba/input/* -output /nba/output/centroids/

/usr/local/hadoop/bin/hdfs dfs -get /nba/output/centroids/* .
/usr/local/hadoop/bin/hdfs dfs -rm /nba/output/centroids/*
mv part-00000 "$1_centroids.txt"

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
			     -file /project1/nba/part2/mapper_filter_player.py \
			     -mapper "/project1/nba/part2/mapper_filter_player.py $1" \
			     -file /project1/nba/part2/reducer_filter_player.py \
			     -reducer /project1/nba/part2/reducer_filter_player.py \
			     -input /nba/input/* -output /nba/output/results/

/usr/local/hadoop/bin/hdfs dfs -mv /nba/output/results/part-00000 /nba/input/"$1_results.txt"

iter=0
while [ $iter -lt 20 ]
do  
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
			     -file /project1/nba/part2/mapper_kmeans.py \
			     -mapper /project1/nba/part2/mapper_kmeans.py \
			     -file /project1/nba/part2/reducer_kmeans.py \
			     -reducer /project1/nba/part2/reducer_kmeans.py \
			     -file /project1/nba/part2/centroids.txt \
			     -input /nba/input/"$1_results.txt" -output /nba/output/results

/usr/local/hadoop/bin/hdfs dfs -rm /nba/input/"$1_results.txt"
/usr/local/hadoop/bin/hdfs dfs -mv /nba/output/results/* /nba/input/
/usr/local/hadoop/bin/hdfs dfs -mv /nba/input/part-00000 /nba/input/"$1_results.txt"
/usr/local/hadoop/bin/hdfs dfs -rm /nba/output/results/*

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
			     -file /project1/nba/part2/mapper_write_centroids.py \
			     -mapper /project1/nba/part2/mapper_write_centroids.py \
			     -file /project1/nba/part2/reducer_write_centroids.py \
			     -reducer /project1/nba/part2/reducer_write_centroids.py \
			     -input /nba/input/"$1_results.txt" -output /nba/output/centroids/

/usr/local/hadoop/bin/hdfs dfs -get /nba/output/centroids/centroids.txt .
/usr/local/hadoop/bin/hdfs dfs -rm /nba/output/centroids/*
mv part-00000 "$1_centriods.txt"
iter=$((iter+1))
done

/usr/local/hadoop/bin/hdfs dfs -get /nba/input/* ./outputs
/usr/local/hadoop/bin/hdfs dfs -rm -r /nba/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /nba/output/

../stop.sh
