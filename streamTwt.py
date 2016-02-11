import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import ConfigParser
import json

parser = ConfigParser.ConfigParser()
parser.read('key_tokens.config')
CONSUMER_KEY = parser.get('critical_information', 'CONSUMER_KEY')
CONSUMER_SECRET = parser.get('critical_information', 'CONSUMER_SECRET')
ACCESS_TOKEN = parser.get('critical_information', 'ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = parser.get('critical_information', 'ACCESS_TOKEN_SECRET')


class MyListener(StreamListener):
    #receiving stream of data
 
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
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

def test():
    return 0

if __name__ == '__main__':
    listener = MyListener()
    stream = Stream(do_auth(), listener)
    #stream.filter(follow=[#id], track=['#python']) #getting all tweet of following id having hashtag as "python"
    stream.filter(track=['#python'])
    #stream.userstream()


