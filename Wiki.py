import Wiki
import bz2
import json


def generatewiki():
    with bz2.open('latest-all.json.bz2') as f:
        filename = input('Enter file name to save wiki data into:  ')
        with open(f'{filename}.txt' , 'w' , encoding = 'utf-8') as file:
            for i, line in enumerate(f):
                line = line.decode()
                if i == 0:
                    assert line == '[\n'
                else:
                    try:
                        assert line.endswith(',\n')
                        wikidata_item = json.loads(line[:-2])
                        qnr = wikidata_item['id']
                        sitelinks = json.loads(line[:-2])['sitelinks']
                        for k,v in sitelinks.items():
                            if k.endswith('wiki'):
                                processed = v['title'].replace(" ","_")
                                processed = processed.replace(",","")
                                processed = processed.lower() 
                                
                                print(k[:-4], processed, 'B', qnr , file = file)
                    except:
                        print(k[:-4], v['title'], 'B', qnr )
                        pass


def generatepageview():
    year = input('Which year of pageview counts do you want to load:  ')
    with open('pagecounts-{year}-views-ge-5-totals','r', encoding = 'utf-8') as infile:
        with open('pageviews_{year}.txt' , 'w', encoding = 'utf-8') as outfile: 
            for i, line in enumerate(infile):
                wiki_code, title, count = line.split(' ')
                count = int(count)
                lang, *mobile, project = wiki_code.split('.')
                assert mobile == ['m'] or mobile == []
                if project != 'z':
                    continue
                print(lang ,title.lower(), 'A', count, file = outfile)

    

