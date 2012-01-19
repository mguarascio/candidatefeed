import tweepy
from tweepy.streaming import StreamListener, Stream

class Listener (StreamListener):
	def on_status(self, status):
		print status.text 
		print status.retweet_count
		return 

def get_tweets():
	auth = tweepy.OAuthHandler('QxpECDyg9eM6inD0jo7Q','a0A8OE2ZN7imCg6WR5ygkrGvKG6tNtoZIChQXQ8NIf4')
	auth.set_access_token('18752311-FXmc9zaPGcszH1bdDNJQa0MY2XRYfYzT3nBRnMqgB','tzXURgYPAbsD1VgmchkoKH9QOJ80qGgSSL13K5A3rY')
	api = tweepy.API(auth)
	listener = Listener()
	stream = Stream(auth, listener)
	stream.filter(track=['Obama'])

if __name__ == "__main__":
	get_tweets();
