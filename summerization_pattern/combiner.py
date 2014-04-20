#!/usr/bin/python

import sys

oldKey = None
total_length = 0.0
total_count = 0.0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, tlen = data_mapped
    tlen = float(tlen)

    if oldKey and oldKey != thisKey:
        print total_count, "\t", total_length/total_count
        oldKey = thisKey
        total_count = 0.0
        total_length = 0.0

    oldKey = thisKey
    total_count += 1.0
    total_length += tlen

if oldKey != None:
    print total_count, "\t", total_length/total_count
