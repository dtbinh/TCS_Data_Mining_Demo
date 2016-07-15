# This program is used for all the data mining purposes. 
# It uses the Tweepy api for python to retrieve tweets and store it on a local database
# Although data mining can be implemented on R as well, Python allows better integration with web apps
# Author: Priya Bhatnagar

#imports
import tweepy #twitter api for python
import pymongo #save tweets on a mongo database
import xlsxwriter #write tweets to excel sheet 
#import nltk.sentiment as s
import time
import datetime
from datetime import datetime

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
			self.data.append(status)
			return True
		else:
			return False

#set keys
consumer_key = "************" # To get a key go to apps.twitter.com 
consumer_secret = "***************"
access_token = 	"**************"
access_token_secret = "************"

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
streamListener = MyStreamListener(max_tweets = 1000000,  data = myTweetData)
stream = tweepy.Stream(auth = auth, listener = streamListener)

#start the stream 
stream.filter(track = ['president'], languages=["en"])

row = 0
col = 0

worksheet.write(row, col, "TWEET")
row += 1
for tweet in myTweetData:
	worksheet.write(row, col, tweet.text)
	row += 1


workbook.close()
