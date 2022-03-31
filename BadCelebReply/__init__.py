# Packages
import os
import sys
import datetime
import logging
import azure.functions as func
from SharedCode import name_utils as dc 
from SharedCode import twitter_utils as tu
from SharedCode import slack_utils as su
from SharedCode import random_name_gen_bot

# NOTES:
# 1) pick a random celeb from the list, run the same processes as the other func,
# but in a reply format - DONE
# 2) ALSO - create a HASHTAG function/class... maybe randomize?
# 3) Create a Kanban board....

# TimerTrigger Function ----
def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)


    # CLASS instantiation: handles / Twitter ops / Slack ----
    name_handle_instance = dc.NameHandle()
    twitter_ops_instance = tu.TwitterOperations()
    slack_notifications = su.SlackNotifications()

    # Call random name generator script ----
    random_gen = random_name_gen_bot.name_gen()
    print(random_gen)

    # Pull in randomly choosen celeb name and twitter handle + sentence ----
    celeb_tweet = name_handle_instance.name_and_handle_reply(random_gen)
    print(celeb_tweet)

    # Pull the handle only ----
    bare_handle = name_handle_instance.handle_only()
    print(bare_handle)

    # Get latest Tweet ID from bare handle ----
    latest_id = twitter_ops_instance.get_tweet_id(bare_handle)
    print(latest_id)

    # Create some hashtags (eventually make function) ----
    celeb_tweet = celeb_tweet + ' |  #' + bare_handle.replace('@', '') 
    celeb_tweet = celeb_tweet + '  #' + 'RealCelebrityNames'
    celeb_tweet = celeb_tweet + '  #' + 'oops'
    #add random tag from list of popular tags

    # Add Twitter ID and reply Tweet to reply function ----
    try:
        twitter_ops_instance.reply_to_tweet(celeb_tweet, latest_id)
        slack_notifications.reply_post_win()
    except:
        slack_notifications.reply_post_loss()    