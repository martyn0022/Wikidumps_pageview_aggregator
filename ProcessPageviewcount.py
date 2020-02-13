import sys
import bz2
import json
import fileinput

def generatepageview():
    
    try:
        for i, line in enumerate(fileinput.input()):
            wiki_code, title, count = line.split(' ')
            count = int(count)
            lang, *mobile, project = wiki_code.split('.')
            assert mobile == ['m'] or mobile == []
            if project != 'z':
                continue
            print(lang ,title.lower(), 'A', count)
    except:
        pass

if __name__ == '__main__':
    generatepageview()