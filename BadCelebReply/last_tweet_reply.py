
# Packages
import tweepy

# Twitter keys ----


# user = api.get_user('apoorv__tyagi')
# need to get tweet id, and then can reply to that

def last_celeb_tweet(consumer_key, consumer_secret,
                     access_token, access_token_secret,
                     twit_handle):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    statuses = api.user_timeline(screen_name=twit_handle)
    test_id = api.get_status(statuses[1])
    print(test_id)

    return statuses[0].text, test_id

# Main function ----
if __name__ == '__main__':
    last_celeb_tweet()    

last_celeb_tweet(consumer_key, consumer_secret,
                     access_token, access_token_secret,
                     '@bad_celeb_names')