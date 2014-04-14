#!/usr/bin/python

import json
import sys

for line in sys.stdin:
    jline = json.loads(line)
    if 'text' in jline and 'place' in jline:
        jplace = jline['place']
        if jplace:
            country = jplace['country']
            try:
                print "{0}\t{1}".format(country, 1)
            except:
                continue
