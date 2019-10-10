#!/bin/sh

mkdir -p json-progex-result

for file in ../codingbat-data/*
do
	java -jar progex.jar $file -format json -lang java -cfg -outdir ./json-progex-result/
done
