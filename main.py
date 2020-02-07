import Wiki
import counter

import bz2
import json
import os

mode = input("input 1 if wikidumps document hasn't been generated:  ")
if mode =='1':
    Wiki.wikigenerator()                # B list
    print("Wiki document generated")
else:
    Wiki.generatepageview()              #A list
    print("Pageview document generated")


#unix command to sort both list



test = Counter()
test.count()