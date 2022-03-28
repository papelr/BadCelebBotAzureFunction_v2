# Packages
import os
import sys
import datetime
import logging
import azure.functions as func
from SharedCode import name_twit_handle_select as dc 
from SharedCode import random_name_gen_bot
from SharedCode import (twitter_push, slack_notifications)
from BadCelebReply import last_tweet_reply


# Twitter keys ----
consumer_key = os.getenv('TwitterConsumerKey1')
consumer_secret = os.getenv('TwitterConsumerSecretKey1')
access_token = os.getenv('TwitterAccessTokenKey1')
access_token_secret = os.getenv('TwitterAccessTokenSecret1')

# pick a random celeb from the list, run the same processes as the other func,
# but in a reply format

# Function ----
def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)


    # Class instantiation for the handling celeb name/twitter username ----
    name_handle_instance = dc.NameHandle()

    # Call random name generator script ----
    random_gen = random_name_gen_bot.name_gen()

    # Pull in randomly choosen celeb name and twitter handle + sentence ----
    celeb_tweet = name_handle_instance.name_and_handle_reply(random_gen)
    print(celeb_tweet)

    # Pull the handle only ----
    bare_handle = name_handle_instance.handle_only()
    print(bare_handle)

    # Get last Tweet and set up the reply Tweeet
    last_tweet = last_tweet_reply.last_celeb_tweet(consumer_key, 
                                                   consumer_secret,
                                                   access_token, 
                                                   access_token_secret,
                                                   bare_handle)