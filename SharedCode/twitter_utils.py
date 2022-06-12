# Packages
import tweepy
import pandas as pd
import os

# Class for Twitter operations ----
class TwitterOperations():

    """
    Functions to grab Twitter IDs (for replying to celebs), functions 
    to push to Twitter, and whatever else is needed for Twitter ops!

    Calling Twitter API keys in the constructor method so that they can be
    passed by self all the way through, instead of making them a class variable
    that would have to be passed to every single method that needs them (I think
    this is the smart route, lol)
    """   

    # Constructor function - authorization and keys
    def __init__(self):

        # Twitter keys from Azure Key Vault
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


    # Reply to specific Tweets (by TWEET ID)
    def get_tweet_id(self, twitter_handle):

        # grabbing last Tweet of user (from Tweepy)
        tweet_info = self.api.user_timeline(screen_name=twitter_handle, 
                                            count=1,
                                            tweet_mode="extended")
        
        #code only latest reply, more strict 
        tweet_id = tweet_info[0].id_str
        # print(tweet_id)

        # return the ID
        return tweet_id

    # Store and return celeb TWEET TEXT
    def get_tweet_text(self, twitter_handle):

        # grabbing last Tweet of user (from Tweepy)
        tweet_info = self.api.user_timeline(screen_name=twitter_handle, 
                                            count=1,
                                            tweet_mode="extended")
        
        # code only latest reply, more strict 
        tweet_text = tweet_info[0].full_text
        # print(tweet_text)

        # return the ID
        return tweet_text

    # Reply to Celeb Tweet, separate from timeline post
    def reply_to_tweet(self, reply_text, tweet_id):

        # set up the reply
        self.api.update_status(reply_text, in_reply_to_status_id=tweet_id,
                               auto_populate_reply_metadata=True) 


    # Puts Tweet metadata into a table, for later push to Azure Storage Table
    def tweet_metadata_table(self, twitter_handle, tweet_id, tweet_text,
                             reply_text):

        # code to pull tweet text, tweet id, handle, & response
        # build pandas df
        data = {'Celeb Handle': [twitter_handle],
                'Celeb Tweet ID': [tweet_id],
                'Celeb Tweet Text': [tweet_text],
                'Bot Reply': [reply_text]}

        # ye olde dataframe creation
        df = pd.DataFrame(data)
        return df


# TwitterOperations().get_tweet_id('bad_celeb_names')
# TwitterOperations().tweet_metadata_table('bad_celeb_names', '1510723841756119047',
# "Taraji P. Henson's real name is Yentil Icenicz. @TherealTaraji |  #TherealTaraji #RealCelebrityNames",
# 'test reply')



