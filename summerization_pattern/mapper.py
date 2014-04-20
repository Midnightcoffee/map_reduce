#!/usr/bin/python

import json
import sys

for line in sys.stdin:
    tweet = json.loads(line)
    if 'text' in tweet and 'id' in tweet:
        text = tweet['text']
        tid = tweet['id']
    print "{0}\t{1}".format(tid, len(text))
