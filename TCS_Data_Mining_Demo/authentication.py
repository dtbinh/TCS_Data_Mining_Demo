import tweepy

consumer_key = "LIBzsGBt3vlY1mUbpM8vJjbq0" # To get a key go to apps.twitter.com 
consumer_secret = "HF1IKSattNKhHH69fvqfD2ShCnGISlHnkqPS8dZuok6G8aq16Y"

auth = tweepy.OAuthHandler(consumer_key = consumer_key, consumer_secret = consumer_secret)
api = tweepy.API(auth)

#@param - tweet 
# Prints the screen name, username, date of tweet and text
def print_tweet(tweet):
	#print(tweet.user.screen_name + " " + tweet.user.name + " " + str(tweet.created_at))
	print((tweet.text).encode('utf-8')) #unicode

#Default 15 results unless specified in count

#dir(tweet) -->lists everything inside the tweet object

#Using cursor for pagination

print("--------------------------------------")
results2 = []
searchWord = "iPhone7"

for tweet in tweepy.Cursor(api.search, q=searchWord, count = 1000).items():
	print_tweet(tweet)