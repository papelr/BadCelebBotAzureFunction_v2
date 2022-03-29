
# Packages
import tweepy

# Twitter keys ----


# will put this into a Twitter/Tweepy CLASS - and move the auth parts
# into the __init__ function (I think that is right...)

def last_celeb_tweet(consumer_key, consumer_secret,
                     access_token, access_token_secret,
                     twit_handle):

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    statuses = api.user_timeline(screen_name = twit_handle) 
    statuses = statuses[0].id_str
    # print(statuses)

    return statuses   

last_celeb_tweet(consumer_key, consumer_secret,
                     access_token, access_token_secret,
                     '@bad_celeb_names')