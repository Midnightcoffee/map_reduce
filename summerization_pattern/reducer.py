#!/usr/bin/python

import sys

oldKey = None
total_length = 0.0
total_count = 0.0
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    count, tlen = data_mapped
    tlen = float(tlen)
    count = float(count)

    total_count += count
    total_length += tlen

print(total_length/total_count)
    

