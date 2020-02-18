#!/usr/bin/env bash

mkfifo Alist
mkfifo Blist

curl https://dumps.wikimedia.org/other/pagecounts-ez/merged/pagecounts-2019-12-views-ge-5-totals.bz2 | bunzip2 | python ProcessPageviewcount.py >> Alist & curl https://dumps.wikimedia.org/wikidatawiki/entities/latest-all.json.bz2 | bunzip2 | python ProcessWikidump.py >> Blist & sort Alist Blist | python GenerateRawQviewsApp.py  | sort -k 1 | python GetAggregatedQviews.py > AggregatedQviews.txt
