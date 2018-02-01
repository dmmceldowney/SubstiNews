import tweepy
from data import twitter

def sendTweet(s):
    auth = tweepy.OAuthHandler(twitter['consumer_key'], twitter['consumer_secret'])
    auth.set_access_token(twitter['access_token'],twitter['access_secret'])
    api = tweepy.API(auth)
    api.update_status(s)

