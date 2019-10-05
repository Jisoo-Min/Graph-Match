#!/bin/sh


for file in ../codingbat-data/*
do
	java -jar progex.jar $file -format json -lang java -cfg 
done