import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import ConfigParser
import json
import sys
import time
import datetime

parser = ConfigParser.ConfigParser()
parser.read('key_tokens.config')
CONSUMER_KEY = parser.get('critical_information', 'CONSUMER_KEY')
CONSUMER_SECRET = parser.get('critical_information', 'CONSUMER_SECRET')
ACCESS_TOKEN = parser.get('critical_information', 'ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = parser.get('critical_information', 'ACCESS_TOKEN_SECRET')

def get_file_name():
    dir_ = 'python-'
    current_day = datetime.datetime.now().strftime("%Y-%m-%d")
    file_name = dir_ + current_day
    return file_name


class MyListener(StreamListener):
    #receiving stream of data
    

    def __init__(self):
        self.start = time.time()
        self.current = self.start
        self.count = 0
        self.tweet_limit = 10
        self.time_limit = 24*60*60 # 24 hour
        self.file_name = get_file_name()

    def on_data(self, data):
        parsed_data = json.loads(data)
        #self.current = time.time()
        #elapse_time = self.current - self.start
        
        self.count = self.count + 1

        if self.count>self.tweet_limit:
            print "No. of tweets per day limit exceeded"
            sys.exit()

        file_name = get_file_name()

        if file_name!=self.file_name:
            print " No. of tweets for the day " + self.file_name[-10:], str(self.count)
            self.file_name = file_name
        try:
            with open(self.file_name, 'a') as f:
                #f.write(data+"\n")
                f.write(json.dumps(parsed_data,indent=4)+"\n\n\n\n")
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_status(self, status):
        # Prints the text of the tweet
        print('Tweet text: ' + status.text)
        for hashtag in status.entries['hashtags']:
            print(hashtag['text'])
        return true
 
    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening
 
    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening
 

def do_auth():
    auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
    return auth

def fetch_tweet(userid):
    if not userid:
        stream.userstream()
    else:
        stream.sitestream(follow=[userid])


if __name__ == '__main__':
    listener = MyListener()
    stream = Stream(do_auth(), listener)
    #stream.filter(follow=[#id], track=['#python']) #getting all tweet of following id having hashtag as "python"
    #stream.filter(track=['#python'])
    fetch_tweet("")
    #stream.userstream()


