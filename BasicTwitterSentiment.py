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



keywordSearch = input("Enter a keyword/hashtag:  ")
public_tweets = api.search(keywordSearch)
noOfSearchTerms = int(input("Enter how many tweets to analyze: "))
tweets = tweepy.Cursor(api.search, q = keywordSearch, lang = "English").items(noOfSearchTerms)
#above line is responsible for creating filters as to how to narrow down search results

pos = 0
neg = 0
neutral = 0
polarity = 0

polarityTotal = 0
for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    polarityTotal += analysis.sentiment.polarity
    if(analysis.sentiment.polarity == 0):
        neutral +=1
    elif(analysis.sentiment.polarity > 0.00):
        pos += 1
    elif(analysis.sentiment.polarity < 0.00):
        neg +=1

print("Based off of " + str(noOfSearchTerms) + " Tweets on " + keywordSearch + ",people are ")
#polarityTotal = polarityTotal/noOfSearchTerms

if (polarityTotal == 0):
    print("Neutral")
elif(polarityTotal > 0.00 and polarityTotal < 0.33):
    print("Slightly Positive")
elif(polarityTotal > 0.33 and polarityTotal < 0.66):
    print("Mostly Positive")
elif(polarityTotal > 0.66 and polarityTotal < 1):
    print("Overwhelmingly Positive")
elif(polarityTotal < 0.00):
    print("Negative")


#this creates the pie chart
labels = ['Positive ['+str(pos)+ '%]'], 'Neutral [' + str(neutral) + '%]', 'Negative [' + str(neg) +'%]'
sizes = [pos, neutral, neg]
colors = ['yellowgreen', 'gold', 'red']
plt.pie(sizes, colors = colors, startangle = 90, autopct='%1.1f%%')
plt.axis('equal')
plt.legend(labels=['Positive', 'Neutral', 'Negative'], loc="best")
plt.title('How people are reacting on ' + keywordSearch + ' by analyzing ' + str(noOfSearchTerms) + ' Tweets.')
plt.axis('equal')
plt.tight_layout()
plt.show()
