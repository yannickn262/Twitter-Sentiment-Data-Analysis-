#this code is based off "Javapolcalypse's" Youtube Twitter Sentiment Analysis Tutorial

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
noOfSearchTerms = int(input("Enter how many tweets to analyze: "))
tweets = tweepy.Cursor(api.search, q = keywordSearch, lang = "English").items(noOfSearchTerms)
#above line is responsible for creating filters as to how to narrow down search results

pos = 0
neg = 0
neutral = 0
polarity = 0
for tweet in tweets:
    analysis = TextBlob(tweet.text)
    if(analysis.sentiment.polarity == 0):
        neutral +=1
    elif(analysis.sentiment.polarity > 0.00):
        pos += 1
    elif(analysis.sentiment.polarity < 0.00):
        neg += 1
pos = percentage(pos,noOfSearchTerms)
pos = format(pos, '.2f')
#converts sentiment to a percentage and formats to two decimal places
neg = percentage(neg,noOfSearchTerms)
neg = format(neg, '.2f')
neutral = percentage(neutral,noOfSearchTerms)
neutral = format(neutral, '.2f')

print("Based off of " + str(noOfSearchTerms) + " Tweets on " + keywordSearch + ",people are ")
if (polarity == 0):
    print("Neutral")
elif(polarity > 0.00):
    print("Positive")
elif(polarity < 0.00):
    print("Negative")

#this creates the pie chart
labels = ['Positive ['+str(pos)+ '%]'], 'Neutral [' + str(neutral) + '%]', 'Negative [' + str(neg) +'%]'
sizes = [pos, neutral, neg]
colors = ['yellowgreen', 'gold', 'red']
patches, texts = plt.pie(sizes, colors = colors, startangle = 90)
plt.legend(patches, labels, loc = "best")
plt.title('How people are reacting on ' + keywordSearch + ' by analyzing ' + str(noOfSearchTerms) + ' Tweets.')
plt.axis('equal')
plt.tight_layout()
plt.show()
