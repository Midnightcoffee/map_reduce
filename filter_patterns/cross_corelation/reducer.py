#!/usr/bin/python

import sys

oldKey = None
total_hash_tags = set()

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    # thisKey, count = data_mapped
    thisKey, hash_tags = data_mapped
    hash_tags = set(hash_tags.strip().replace('(', '').replace(')','').split(','))
    hash_tags = {h for h in hash_tags if h} # possible blank causes by one tuple

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", (len(total_hash_tags), total_hash_tags)
        oldKey = thisKey
        total_hash_tags = set()

    oldKey = thisKey
    total_hash_tags.update(hash_tags)

if oldKey != None:
    print oldKey, "\t", (len(total_hash_tags), total_hash_tags)
