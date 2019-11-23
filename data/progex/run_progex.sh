#!/bin/sh


for file in ../codingbat_solution/*
do
	java -jar progex.jar $file -format json -lang java -cfg 
done
