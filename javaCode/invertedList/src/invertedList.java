import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.FileSplit;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

import java.io.IOException;
import java.util.Iterator;
import java.util.StringTokenizer;

/**
 * Created by warrior on 16-4-20.
 */
public class invertedList {
    public static class ILMapper
    extends Mapper<Object, Text, Text, Text>{
        public void map(Object key, Text value, Context context)
        throws IOException, InterruptedException{
            FileSplit fileSplit = (FileSplit) context.getInputSplit();
            String fileName = fileSplit.getPath().getName();
            Text fileName_lineOffset = new Text(fileName+"#"+key.toString());
            StringTokenizer iter = new StringTokenizer(value.toString());
            Text word = new Text();
            for(;iter.hasMoreTokens();){
                word.set(iter.nextToken());
                context.write(word, fileName_lineOffset);
            }
        }
    }

    public static class ILReducer
    extends Reducer<Text, Text, Text, Text>{
        public void reduce(Text key, Iterable<Text> values, Context context)
        throws IOException, InterruptedException{
            Iterator<Text> it = values.iterator();
            StringBuilder all = new StringBuilder();
            if(it.hasNext()){
                all.append(it.next().toString());
            }
            for(;it.hasNext();){
                all.append(";");
                all.append(it.next().toString());
            }
            context.write(key, new Text(all.toString()));
        }
    }

    public static void main(String[] args) throws Exception{
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "inverted list");
        job.setJarByClass(invertedList.class);
        job.setMapperClass(ILMapper.class);
        job.setReducerClass(ILReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(Text.class);
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        System.exit(job.waitForCompletion(true)?0:1);
    }
}
