#!/usr/bin/env python3

import sys
import bz2
import json
import fileinput

def generatewiki():
    for i, line in enumerate(fileinput.input(openhook=fileinput.hook_encoded('utf-8'))):
        #line = line.decode()
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
                        
                        print(k[:-4], processed, 'B', qnr )
                #return filename
            except:
                print(k[:-4], v['title'], 'B', qnr , file=sys.stderr)
                raise

if __name__ == '__main__':
    generatewiki()