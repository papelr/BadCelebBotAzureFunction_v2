import sys
import os
import datetime
import logging
from BadCelebTimer import random_name_gen_bot 
from BadCelebTimer import name_twit_handle_select as dc
# from BadCelebTimer import slack_notifications
from BadCelebTimer import twitter_push
from BadCelebTimer.all_keys import consumer_key, consumer_secret, access_token, access_token_secret # pylint: disable=relative-beyond-top-level
import azure.functions as func


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
    celeb_tweet = name_handle_instance.name_and_handle(random_gen)
    print(celeb_tweet)

    # Use the name_insurance function in the scraping script ----
    plain_name = name_handle_instance.name_insurance()
    print(plain_name)

    # Create hashtags ----
    celeb_tweet = celeb_tweet + ' #' + plain_name.replace(
        ' ', '') + ' #' + plain_name.split()[0] + ' #' + plain_name.split()[1] + ' #RealCelebrityNames' +  ' #bad_celeb_names'

    # Call twitter push script (with error handling & notifs) ----
    attempts = 0
    while attempts < 2:
        try:
            twitter_push.twit_push(consumer_key, consumer_secret,
                                   access_token, access_token_secret,
                                   celeb_tweet)
            # slack_notifications.post_worked()
            print('Tweet Posted!')
            break
        except:
            attempts += 1
            # slack_notifications.post_failed()
            print('Tweet did NOT post')
