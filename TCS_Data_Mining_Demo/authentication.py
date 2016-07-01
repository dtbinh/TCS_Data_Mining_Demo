import tweepy

consumer_key = "NM3ODIGJ7iDTwISr7mRdIe60Y" # To get a key go to apps.twitter.com 
consumer_secret = "Mu6rMnPHeLNkNP1nfLa3kChtDDqiH4e28UISS18h4GPdTojkhi"

auth = tweepy.OAuthHandler(consumer_key = consumer_key, consumer_secret = consumer_secret)
api = tweepy.API(auth)

#@param - tweet 
# Prints the screen name, username, date of tweet and text
def print_tweet(tweet):
	print(tweet.user.screen_name + " " + tweet.user.name + " " + str(tweet.created_at))
	print((tweet.text).encode('utf-8')) #unicode

#Default 15 results unless specified in count
# results = api.search(q="happy", count = 100, result_type = "recent")

# print(len(results)) 

# for tweet in results:
# 	print_tweet(tweet)


#dir(tweet) -->lists everything inside the tweet object

#Using curor for pagination

print("--------------------------------------")
results2 = []
searchWord = "iphone7"

for tweet in tweepy.Cursor(api.search, q=searchWord, count = 1000).items():
	print((tweet.text).encode('utf-8'))
	results2.append(tweet)