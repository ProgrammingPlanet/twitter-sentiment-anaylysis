#!/usr/bin/env python3

import json
import tweepy

#for importing this class use 'from twitterapi import TwApi' and than
#for connecting to api simply call TwApi().connect() and it will return an api instance, if connection success otherwise 'None'


class TwApi:

	api = None

	def __init__(self):
		
		# Variables that contains the user credentials to access Twitter API
		ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
		ACCESS_SECRET = 'YOUR_ACCESS_SECRET'
		CONSUMER_KEY = 'YOUR_CONSUMER_KEY'
		CONSUMER_SECRET = 'YOUR_CONSUMER_SECRET'

		# Setup tweepy to authenticate with Twitter credentials:
		auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
		auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

		# Create the api to connect to twitter with your creadentials
		self.api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

		#---------------------------------------------------------------------------------------------------------------------
		# wait_on_rate_limit= True;  will make the api to automatically wait for rate limits to replenish
		# wait_on_rate_limit_notify= Ture;  will make the api  to print a notification when Tweepyis waiting for rate limits to replenish
		# compression= True;	allow data compression
		#---------------------------------------------------------------------------------------------------------------------

	def connect(self):

		return self.api


