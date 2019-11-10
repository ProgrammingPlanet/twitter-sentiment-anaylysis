#!/usr/bin/env python3

import tweepy

from textblob import TextBlob

import matplotlib.pyplot as plt

from twitterapi import TwApi

def percentage(part,whole):
	return 100 * float(part)/float(whole)

searchTerm = input("Enter keyword/hashtag to search about: ")
NoOfserachTerms = int(input("Enter How many tweets to analyze: "))

api = TwApi().connect()

tweets = tweepy.Cursor(api.search, q=searchTerm, lang="en").items(NoOfserachTerms)

positive = negetive = neutral = totalpolarity = 0

print('Please Wait While We Are Fetching And Analysing The Tweets....')

for tweet in tweets:

	analysis = TextBlob(tweet.text)

	polarity = analysis.sentiment.polarity

	if (polarity == 0):
		neutral += 1

	elif (polarity < 0):
		negetive += 1

	elif (polarity > 0):
		positive += 1

	totalpolarity += polarity

positive = format(percentage(positive,NoOfserachTerms), '.2f')
negetive = format(percentage(negetive,NoOfserachTerms), '.2f')
neutral = format(percentage(neutral,NoOfserachTerms), '.2f')

print('Close The PieChart Window To Exit....')

lables = ['Positive ['+str(positive)+'%]', 'Neutral ['+str(neutral)+'%]', 'Negetive ['+str(negetive)+'%]']

sizes = [positive,neutral,negetive]

colors = ['green','gold','red']

patches, texts = plt.pie(sizes, colors=colors, startangle=90)

plt.legend(patches, lables, loc="best")

plt.title('How People are reacting on {'+searchTerm+'} by analyzing '+str(NoOfserachTerms)+' Tweets.')

plt.axis('equal')

plt.tight_layout()

plt.show()
