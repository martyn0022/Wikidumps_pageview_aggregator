#!/bin/bash

mkfifo Alist
mkfifo Blist

curl https://dumps.wikimedia.org/other/pagecounts-ez/merged/pagecounts-2019-12-views-ge-5-totals.bz2 | bunzip2 | python step2.py| head -n 100000 >> Alist & curl https://dumps.wikimedia.org/wikidatawiki/entities/latest-all.json.bz2 | bunzip2 | python step1.py| head -n 100000 >> Blist & sort Alist Blist | python runstep4ab.py  | sort -k 1 | python Step5.py > AggregatedQviews.txt
