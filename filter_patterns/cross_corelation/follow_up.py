"""
       File : follow_up.py
     Author : Drew Verlee
       Date : 14.04.14.
      Email : drew.verlee@gmail.com
     GitHub : https://github.com/Midnightcoffee/
Description : sorts the hash tags and finds out what they were hashing about
"""


import json
import sys
from hashtags import get_hash_tags, get_user_id

coorelation = []

def find_most_coorelated_hash_tags(n):
    with open('output.txt') as output:
        for line in output:
            line = line.strip().split("\t")
            ids, count = line
            count = float(count)
            coorelation.append(ids)

    coorelation.sort(reverse=True)
    return set(coorelation[0:n])

def mapper(_, streaming_tweets):
        find_most_coorelated_hash_tags(5)
        for i in streaming_tweets:
            i_id = get_user_id(i)
            i_hashtags = get_hash_tags(i)
            if i_id and i_hashtags:
                for j in streaming_tweets:
                    j_id = get_user_id(j)
                    if j_id != i_id:
                        j_hashtags = get_hash_tags(j)
                        if j_id and j_hashtags:
                            if i_hashtags.intersection(j_hashtags):
                                print "{0}\t{1}".format( (i_id,j_id), 1)
