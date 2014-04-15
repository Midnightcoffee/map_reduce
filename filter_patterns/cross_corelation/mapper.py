#!/usr/bin/python

import json
import sys
from hashtags import get_hash_tags, get_user_id

# This will only mimic mapping function because I'm not sure its possible
 # with streaming


def mapper(_, streaming_tweets):
        for i in streaming_tweets:
            i_id = get_user_id(i)
            i_hashtags = get_hash_tags(i)
            if i_id and i_hashtags:
                for j in streaming_tweets:
                    j_id = get_user_id(j)
                    if j_id != i_id:
                        j_hashtags = get_hash_tags(j)
                        if j_id and j_hashtags:
                            # normalize
                            i_hashtags = {i.strip().lower() for i in i_hashtags}
                            j_hashtags = {j.strip().lower() for j in j_hashtags}
                            # whitespace
                            i_hashtags = {i for i in i_hashtags if i}
                            j_hashtags = {j for j in j_hashtags if j}

                            shared_hash_tags = i_hashtags.intersection(j_hashtags)
                            if shared_hash_tags:
                                print "{0}\t{1}".format( (i_id,j_id), tuple(shared_hash_tags))

if __name__ == '__main__':
    tweet_file = "../../../tweets.txt"
    # tweet_file ="sample.txt"
    tweets = [json.loads(t) for t in open(tweet_file)]
    mapper(None, tweets)
