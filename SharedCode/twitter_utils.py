# Packages
import tweepy
import pandas as pd
import os

# Class for Twitter operations ----
class TwitterOperations():

    '''
    Functions to grab Twitter IDs (for replying to celebs), functions 
    to push to Twitter, and whatever else is needed for Twitter ops!

    Calling Twitter API keys in the constructor method so that they can be
    passed by self all the way through, instead of making them a class variable
    that would have to be passed to every single method that needs them (I think
    this is the smart route, lol)
    '''   

    # Constructor function - authorization and keys
    def __init__(self):

        # Twitter keys
        self.consumer_key = os.getenv('TwitterConsumerKey1')
        self.consumer_secret = os.getenv('TwitterConsumerSecretKey1')
        self.access_token = os.getenv('TwitterAccessTokenKey1')
        self.access_token_secret = os.getenv('TwitterAccessTokenSecret1')

        # Twitter authorization
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(self.auth)


    # Push to Twitter method
    def twit_push(self, tweet_text):

        # push Tweet to Twitter (just tweet, no media)
        self.api.update_status(tweet_text, tweet_mode = 'extended')

        # push Tweet to Twitter WITH media
        # api.update_with_media(tweet_text, tweet_mode = 'extended') 


    # Reply to specific Tweets method
    def get_tweet_id(self, twitter_handle):

        # grabbing last Tweet of user (max_id, from Tweepy)
        tweet_id = self.api.user_timeline(screen_name = twitter_handle) 
        tweet_id = tweet_id[0].id_str
        # print(tweet_id)

        # return the ID
        return tweet_id

    def reply_to_tweet(self, reply_text, twitter_handle, tweet_id):

        # set up the reply    

# Testing
TwitterOperations().get_tweet_id('@bad_celeb_names')        
