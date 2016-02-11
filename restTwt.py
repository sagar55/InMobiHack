import tweepy
import json
import ConfigParser
from tweepy import OAuthHandler


parser = ConfigParser.ConfigParser()
parser.read('key_tokens.config')
CONSUMER_KEY = parser.get('critical_information', 'CONSUMER_KEY')
CONSUMER_SECRET = parser.get('critical_information', 'CONSUMER_SECRET')
ACCESS_TOKEN = parser.get('critical_information', 'ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = parser.get('critical_information', 'ACCESS_TOKEN_SECRET')

#2208027565
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

		#getting tweet data 
		for tweet in public_tweets: 
			f.write(json.dumps(tweet._json,indent=4)+"\n\n\n\n\n") 

		# way of getting first 10 tweets text appearing in our home feed 
		for tweet in tweepy.Cursor(api.home_timeline).items(10):
			print tweet.text

    	#gettng all the followers 
		for friend in tweepy.Cursor(api.friends).items():
			f.write(json.dumps(friend._json,indent=4)+"\n\n\n\n\n")

		#Iterate through the first 20 statuses in the friends timeline
		for tweet in tweepy.Cursor(api.friends_timeline).items(20):
			f.write(json.dumps(tweet._json,indent=4)+"\n\n\n\n\n")

		#getting all the tweets a user has tweets (if user id not provided then get tweet by defaul of registered api key account/authorised acc)
		for tweet in tweepy.Cursor(api.user_timeline).items():
			f.write(json.dumps(tweet._json,indent=4)+"\n\n\n\n\n")

		for status in tweepy.Cursor(api.user_timeline,id="505452845").items():
			f.write(json.dumps(status._json,indent=4)+"\n\n\n\n\n")


def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)

def test2(api):
	with open('mytweets.json', 'w') as f:
		cnt=1
		# for page in tweepy.Cursor(api.user_timeline).pages():
		# 	f.write(str(cnt))
		# 	cnt=cnt+1
		# 	for status in page:
		# 		f.write(json.dumps(status._json,indent=4)+"\n\n\n\n\n")
		# 	f.write("#########################")

		# f.write("###########################################")
		# for status in tweepy.Cursor(api.user_timeline,id="134758540").items():
		# 	f.write(json.dumps(status._json,indent=4)+"\n\n\n\n\n")

		user = api.me()
		print user.name




api = do_auth()
test2(api)
