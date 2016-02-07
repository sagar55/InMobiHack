import tweepy
import json
from tweepy import OAuthHandler

CONSUMER_KEY = "IP67a8Cxt1E0qnUQFl1BUsvs7"
CONSUMER_SECRET = "mSZmpdGnw4g0r4TB5BhEtKg792H7qaY2IWiW494QMbKAD5NEfk"
ACCESS_TOKEN = "858315636-XICCgkb31jiaKFURwuUHHu3ZlAUlZGP4Y7lN4pD5"
ACCESS_TOKEN_SECRET = "O0EkfIV3pVCmR6r653BJNkNpH31X2HTevaNOMWyKVjHIZ"

def do_auth():
	auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)
	return api

def test(api):

	public_tweets = api.home_timeline()
	
	with open('mytweets.json', 'w') as f:
		user = api.me()
		print user.name #my user name
		for tweet in public_tweets:
			f.write(json.dumps(tweet._json,indent=4)+"\n\n\n\n\n")

		for friend in tweepy.Cursor(api.friends).items():
			f.write(json.dumps(friend._json,indent=4)+"\n\n\n\n\n")
			
		for tweet in tweepy.Cursor(api.user_timeline).items():
			f.write(json.dumps(tweet._json,indent=4)+"\n\n\n\n\n")
	

api = do_auth()
test(api)


