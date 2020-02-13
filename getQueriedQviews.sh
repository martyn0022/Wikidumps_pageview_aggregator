#!/bin/bash


Sort Qnumbers.txt AggregatedQviews.txt -r -u | python PageviewGenerator.py | sort -g -k 2 -r > Qviews.txt 

