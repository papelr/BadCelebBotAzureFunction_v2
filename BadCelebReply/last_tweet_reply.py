# Packages
import tweepy

testx = "@bad_celeb_names"

# Twitter developer keys ----
consumer_key = 'MJs1HeiWKZHZTXxsZka8aUwjf'
consumer_secret = 'SMLMVUkC0zF9AgGUffLviqaEE3lws2kk1vseSupfLh30KL80Lj'
access_token = '1362119469854818309-AzG0Lnfe5LTBZYDbEhrDlBXG55XStF'
access_token_secret = 'KhFbUlbNZQ38X78JQmAb3rqjva49xeQhEWzynsQ3gGLzJ'

def last_celeb_tweet(twitter):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    statuses = api.user_timeline(screen_name=twitter)
    return statuses[0].text

# Main function ----
if __name__ == '__main__':
    last_celeb_tweet(testx)    
