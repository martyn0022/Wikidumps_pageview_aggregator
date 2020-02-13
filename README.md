# Wikidumps_pageview_aggregator
App that generates a list of Q numbers with its aggregated pageviews (across languages) into a .txt document which could be used to extract page views for whatever entity the user queries

## Instructions

1. Go to this [Dropbox link](https://www.dropbox.com/s/9d6cbvhdvpmov4o/AggregatedQviews.txt?dl=0) and download the AggregatedPageview.txt file to query for wikipedia page views on 2019-12 be sure to add this file into the same folder directory

2. Open a Git Bash terminal in the folder directory and input the following :
```shell
python GenerateQviews.py
```
3. Specify if you want to use a location ID or bbox coordinates to determine the area you want to query on OpenStreetMap as prompted on the console.

4. Specify the OpenStreetMap Key-Value pair (ie. historic-castle) as prompted by the console

5. Hit enter. The following sorted list of Qnumber-Views should be saved into a file named ```Qviews.txt```.

## Querying other time periods
The list in the Dropbox link was generated from Wikipedia page views in Decemeber 2019. However if you have to query the page views in a different time period, heres how:

1. Open GenerateAggregatedQviews.sh in any editor.

2. On ``` Line 6 ``` of the script, in the first ``` curl ``` statement, you could change the time period in ```https://dumps.wikimedia.org/other/pagecounts-ez/merged/pagecounts-2019-12-views-ge-5-totals.bz2``` to another time period by changing the "2019-12" to any time period available in this [link](https://dumps.wikimedia.org/other/pagecounts-ez/merged/).

3. For example if you want to query the page views in July of 2015 you would change ```https://dumps.wikimedia.org/other/pagecounts-ez/merged/pagecounts-```**2019-12**```-views-ge-5-totals.bz2``` 
 <br> to <br>
```https://dumps.wikimedia.org/other/pagecounts-ez/merged/pagecounts-```**2015-07**```-views-ge-5-totals.bz2```
resulting ```curl``` statement should be <br> ```curl https://dumps.wikimedia.org/other/pagecounts-ez/merged/pagecounts-2019-12-views-ge-5-totals.bz2 | etc```

4. Lastly open a Git Bash terminal in the folder directory and input the follow:
```shell
./GenerateAggregatedQviews.sh
```
This will take a very long while as in generates a list of Wikidata Qnumbers against its corresponding number of views across all Wikipedia page languages. 

5. The consolidated file should be saved as ```AggregatedQviews.txt```.
