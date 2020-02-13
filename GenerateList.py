# USE GeneratAggregatedQviews.sh INSTEAD

import Wiki
import counter
import subprocess


import bz2
import json
import os

mode = input("input 1 if wikidumps document and Pageview document haven't been generated:  ")
if mode =='1':
    filename = Wiki.wikigenerator()                # B list
    print("Wiki document generated")
    year = Wiki.generatepageview()              #A list
    print("Pageview document generated")
else:
    continue


subprocess.run(args = [r'C:\Users\mlee\AppData\Local\Programs\Git\usr\bin\sort.exe', f'{filename}.txt', f'pageviews_{year}.txt','-o' , 'ABlist.txt' ],  encoding = 'utf-8')


test = Counter()
test.count()

#TODO: Sort the resulting list of Qviews by its Qnumbers
subprocess.run(args = [r'C:\Users\mlee\AppData\Local\Programs\Git\usr\bin\sort.exe', '-k' , '1' , 'Qviews.txt', '-o' , 'sorted_qviews.txt'])

#Aggregates all the views in repeated Qnrs and writes them as a single entry into another file
Qviews.AggregateQviews()


'''#This step queries on Overpass to produce a list of Qnumbers
OSMquery = OSMquery()

choice = input("Press 1 for to use AreaID and 2 for bbox choice: ")
if choice =='1':
    Key = input("Input Key: ")
    Value = input("Input Value: ")
    Location = input("Input Location: ")
    result = OSMquery.query( Key , Value , Location )
else:
    Key = input("Input Key: ")
    Value = input("Input Value: ")
    bbox = []
    while len(bbox) < 4:
        coordinate = float(input("input bbox coordinates: "))
        bbox.append(coordinate)
    result = OSMquery.boundbox( Key , Value , bbox )
 
print(result)


#Accessing the Q numbers from the large chucnk of JSON files produced from the API 
listofQnumbers = [( data['tags']['wikidata'] ) for data in result['elements'] if data['tags'].get('wikidata',) ]
print(listofQnumbers)
with open("Qnumbers.txt" , 'w' , encoding = 'utf-8') as f:
    for qnr in listofQnumbers:
        f.write(qnr + '\n')
print('file saved as Qnumbers.txt')

#TODO: Unix sort the queried OSM qnumbers and the superlist
subprocess.run(args = [r'C:\Users\mlee\AppData\Local\Programs\Git\usr\bin\sort.exe', 'Qnumbers.txt', 'AggregatedQviews.txt' ,'-o' , 'jointlist.txt' ],  encoding = 'utf-8')

#TODO: step 8
Qviews.generateQviews()'''


