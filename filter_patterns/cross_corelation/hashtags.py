import json

def get_hash_tags(tweet):
    # tweet = json.loads(tweet)
    hash_tags = set()
    if 'entities' in tweet and 'lang' in tweet:
        if tweet['lang'] == 'en':
            entities = tweet['entities']
            if 'hashtags' in entities:
                hashtags = entities['hashtags']
                if hashtags:
                    for hashtag in hashtags:
                        if 'text' in hashtag:
                            text = hashtag['text']
                            try:
                                text = str(text)
                            except:
                                continue
                            hash_tags.add(text)
    return hash_tags

def get_user_id(tweet):
    # tweet = json.loads(tweet)
    return tweet['user']['id'] if 'user' in tweet else None


if __name__ == '__main__':
    tweets = "../../../tweets.txt"
