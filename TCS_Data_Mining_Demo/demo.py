# This program is used for all the data mining purposes. 
# It uses the Tweepy api for python to retrieve tweets and store it on a local database
# Author: Priya Bhatnagar

#imports
import tweepy #twitter api for python
import pymongo #save tweets on a mongo database
import xlsxwriter #write tweets to excel sheet 
#import nltk.sentiment as s
import time
import datetime
from datetime import datetime

#connect to mongoDB
collection = pymongo.MongoClient()["tweets"]["sentimentAnalysis"]

#this class inherits from tweepy.StreamListener and overrides the constructor and on_status method
class MyStreamListener(tweepy.StreamListener):

	def __init__(self, max_tweets = None, data = [], *args, **kwargs):
		self.counter = 0
		self.max_tweets = max_tweets
		self.data = data

		super().__init__(*args, **kwargs)

	def on_error(self ,status):
		print(status)

	def on_status(self, status):
		self.counter += 1
		if self.counter <= self.max_tweets:
			print("-----" + str(self.counter) + "------")
			print((status.text).encode('utf-8'))
			if(str(status.place) != "None"):
				self.data.append(status)
			#collection.insert_one(status._json) #storing tweet on db with json format
			return True
		else:
			return False

#set keys
consumer_key = "LIBzsGBt3vlY1mUbpM8vJjbq0" # To get a key go to apps.twitter.com 
consumer_secret = "HF1IKSattNKhHH69fvqfD2ShCnGISlHnkqPS8dZuok6G8aq16Y"
access_token = 	"745440108891934720-U0WwTMrQ5kZl6B4GqByUPXrP66myX5t"
access_token_secret = "OOheJ0XzhfAwfQbvKiaunB0tbwBDDEQ6BpuwitOQp6wUZ"

#set configuration
auth = tweepy.OAuthHandler(consumer_key = consumer_key, consumer_secret = consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#get current time
time = time.time()
timestamp = datetime.fromtimestamp(time).strftime('%Y_%m_%d_%H_%M_%S')
timestamp = str(timestamp)
path = 'C:\\Users\\priyabhatnagar\\TCS_Data_Mining_Demo\\data\\' + timestamp + '.xlsx'

#create an excel sheet
workbook = xlsxwriter.Workbook(path)
worksheet = workbook.add_worksheet()

#stream
#create a stream by creating an instance of the listener and passing it as a parameter
myTweetData = []
streamListener = MyStreamListener(max_tweets = 10000,  data = myTweetData)
stream = tweepy.Stream(auth = auth, listener = streamListener)

#start the stream 
stream.filter(track = ['iphone'], languages=["en"])

row = 0
col = 0

worksheet.write(0, 0, "TWEET")
worksheet.write(0, 1, "TIME")
row += 1
for tweet in myTweetData:
	worksheet.write(row, col, tweet.text)
	worksheet.write(row, col + 1, str(tweet.place.full_name))
	row += 1


workbook.close()
