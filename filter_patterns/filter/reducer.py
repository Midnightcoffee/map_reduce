#!/usr/bin/python

import sys

oldKey = None
total_count = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, count = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", total_count
        oldKey = thisKey
        total_count = 0

    oldKey = thisKey
    total_count += float(count)

if oldKey != None:
    print oldKey, "\t", total_count
