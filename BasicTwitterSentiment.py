from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt


def percentage (part, whole):
    return 100 * float(part)/float(whole)

consumerKey = 'lylabb2p87T18drYKDSM19kWE'
consumerSecret = 'pYBUzAwYMTWfLT0YMdnKvKLg0lkMFjyL8hMoa7I1UwY7F7RxHt'
access_token = '55873887-ntL1yMFwCKaGjA7EwlFdXvVw4Kcsv2T6lD2285SzR'
access_secret = 'fwxUYWHAF7XdmJmjpq3V2FWZ1yQqYsiZvyg0DdEDTbTJ1'

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

keywordSearch = input("Enter a keyword/hashtag:  ")
noOfSearchTerms = int(input("Enter how many tweets to analyze"))
tweets = tweepy.Cursor(api.search, q = keywordSearch, lang = "English").items(noOfSearchTerms)
#above line is responsible for creating filters as to how to narrow down search results

for tweet in public_tweets:

    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
