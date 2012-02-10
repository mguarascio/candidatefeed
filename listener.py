from django.core.management import setup_environ
from candidatefeed import settings
setup_environ(settings)

import tweepy
import json
from gatherdata.models import Candidate, Tweet, URL
from tweepy.streaming import StreamListener, Stream

class TweetParser:
	def __init__(self, status):
		self.status = status

	def save(self):
		for url in self.status.entities['urls']:
			urlstr = url['expanded_url']
		print self.status.text

		url = URL(url=urlstr)
		url.save()
		candidate = Candidate.objects.filter(name__endswith='Obama')
		newtweet = Tweet(created_at=self.status.created_at, text=self.status.text, user=self.status.user.screen_name, raw_json=self.status.json, urls=[url], candidates=[candidate])
		newtweet.save()
		

class Listener (StreamListener):
	def on_status(self, status):
		tweet = TweetParser(status)
		tweet.save()
		return 

def get_tweets(keyword):
        init_tweepy()
	auth = tweepy.OAuthHandler('QxpECDyg9eM6inD0jo7Q','a0A8OE2ZN7imCg6WR5ygkrGvKG6tNtoZIChQXQ8NIf4')
	auth.set_access_token('18752311-FXmc9zaPGcszH1bdDNJQa0MY2XRYfYzT3nBRnMqgB','tzXURgYPAbsD1VgmchkoKH9QOJ80qGgSSL13K5A3rY')
	api = tweepy.API(auth)
	listener = Listener()
	stream = Stream(auth, listener)
	stream.filter(track=[keyword])

@classmethod
def parse(cls, api, raw):
	status = cls.first_parse(api, raw)
	setattr(status, 'json', json.dumps(raw))
	return status

def init_tweepy():
        print 'Extending tweepy'
	tweepy.models.Status.first_parse = tweepy.models.Status.parse
	tweepy.models.Status.parse = parse

if __name__ == "__main__":	
	get_tweets('Obama')
