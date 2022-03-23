# Import packages
import pip
import tweepy
import time

# Authenticate to Twitter
consumer_key = ''
consumer_secret = ''
access_key = ''
access_secret = ''

# Create API object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = 'savingstips'
num_of_tweets = 1000

for tweet in tweepy.Cursor(api.search, search).items(num_of_tweets):
    try:
        tweet.retweet()
        print("Retweet")
        time.sleep(30)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

