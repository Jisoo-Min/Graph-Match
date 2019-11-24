#!/bin/sh


for file in progex_output/*
do
	echo $file
	python3 make_basic_blocks.py $file $1
done
