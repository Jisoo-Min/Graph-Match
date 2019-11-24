#/bin/sh


for file in ../codingbat-solution/*
do
	java -jar progex.jar $file -format json -lang java -cfg -outdir ../progex_output
 
done
