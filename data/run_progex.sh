#!/bin/sh

mkdir -p json-progex-result

for file in /codingbat-data/*
do
	java -jar progex.jar $file -format $1 -lang java -cfg -outdir ./json-progex-result/
done
