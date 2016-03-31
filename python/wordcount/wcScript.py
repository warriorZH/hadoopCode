#!/usr/bin/env python

import commands
outputs = commands.getoutput("hadoop fs -rmr hdfs://warrior:9000/user/warrior/testData/hadoopWCResult")
outputs = commands.getoutput("hadoop jar $HADOOP_HOME/hadoop-streaming-2.6.0.jar \
-files mapper.py,reducer.py \
-mapper ./mapper.py  \
-reducer ./reducer.py  \
-input testData/new01 \
-output testData/hadoopWCResult \
 ")
print outputs

#-files ./reducer.py \
#-files ./mapper.py  \
