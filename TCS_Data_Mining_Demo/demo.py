#imports
import tweepy
import pymongo
import numpy as np
import pandas as pd
import matplotlib as plt
import ipwidgets as wgt
from datetime import datetime

consumer_key = "LIBzsGBt3vlY1mUbpM8vJjbq0" # To get a key go to apps.twitter.com 
consumer_secret = "HF1IKSattNKhHH69fvqfD2ShCnGISlHnkqPS8dZuok6G8aq16Y"

access_token = 	"745440108891934720-U0WwTMrQ5kZl6B4GqByUPXrP66myX5t"
access_token_secret = "OOheJ0XzhfAwfQbvKiaunB0tbwBDDEQ6BpuwitOQp6wUZ"

auth = tweepy.OAuthHandler(consumer_key = consumer_key, consumer_secret = consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#collection
col = pymongo.MongoClient() #db name and collection name
col.count()