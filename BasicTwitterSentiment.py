import tweepy
from textblob import TextBlob

consumer_key = 'lylabb2p87T18drYKDSM19kWE'
consumer_secret = 'pYBUzAwYMTWfLT0YMdnKvKLg0lkMFjyL8hMoa7I1UwY7F7RxHt'
access_token = '55873887-ntL1yMFwCKaGjA7EwlFdXvVw4Kcsv2T6lD2285SzR'
access_secret = 'fwxUYWHAF7XdmJmjpq3V2FWZ1yQqYsiZvyg0DdEDTbTJ1'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:

    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
