#imports
import tweepy
import pymongo
import numpy as np
#import pandas as pd
import matplotlib as plt
#import ipwidgets as wgt
from datetime import datetime

#listener
class MyStreamListener(tweepy.StreamListener):

	counter = 0

	def __init__(self, max_tweets = 1000, *args, **kwargs):
		self.max_tweets = max_tweets
		self.counter = 0
		super().__init__(*args, **kwargs)

		def on_connect(self):
			self.counter = 0
			self.start_time = datetime.now()

	def on_status(self, status):
		self.counter += 1

		#store tweet to mongoDB
		col.insert_one(status._json)

consumer_key = "LIBzsGBt3vlY1mUbpM8vJjbq0" # To get a key go to apps.twitter.com 
consumer_secret = "HF1IKSattNKhHH69fvqfD2ShCnGISlHnkqPS8dZuok6G8aq16Y"

access_token = 	"745440108891934720-U0WwTMrQ5kZl6B4GqByUPXrP66myX5t"
access_token_secret = "OOheJ0XzhfAwfQbvKiaunB0tbwBDDEQ6BpuwitOQp6wUZ"

auth = tweepy.OAuthHandler(consumer_key = consumer_key, consumer_secret = consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#collection
col = pymongo.MongoClient()["tweets"]["sentimentAnalysis"] #db name and collection name
print(col.count())

myStreamListener = MyStreamListener(max_tweets=1000)
myStream = tweepy.Stream(api.auth, listener = myStreamListener)

#keywords for which we will find tweets
keywords = ["iphone6", "iphone7"]

#starting a filter

for error_counter in range(20):
	try: 
		myStream.filter(track = keywords)
		print("Tweets collected: %s" % myStream.listener.counter)
		print("Total tweets in collection: %s" %col.count())
		break
	except:
		print("ERROR # %s" % (error_counter + 1))