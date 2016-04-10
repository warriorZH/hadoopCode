#!/usr/bin/python
#-*- coding: UTF-8 -*-

#filename: mapre_script.py
#description: excute map reduce for matrix multiplication
#author: warrior  ,mail: oowarrioroo@163.com
#data: 2016-4-1
#log:
import commands
outputs = commands.getoutput("hadoop fs -rmr hdfs://warrior:9000/user/warrior/testData/hadoopMMResult")
outputs = commands.getoutput("hadoop jar $HADOOP_HOME/hadoop-streaming-2.6.0.jar \
-files mapper.py,reducer.py \
-mapper ./mapper.py  \
-reducer ./reducer.py  \
-input testData/matrixdata.txt \
-output testData/hadoopMMResult \
")
#outputs = commands.getoutput("hadoop fs -rmr hdfs://warrior:9000/user/warrior/testData/hadoopMMResult")
