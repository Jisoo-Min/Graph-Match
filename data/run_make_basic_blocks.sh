#!/bin/sh


for file in progex-result/json-progex-result/*
do
	echo $file
	python3 make_basic_blocks.py $file $1
done
