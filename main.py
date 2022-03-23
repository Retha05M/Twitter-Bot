# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

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

search = 'financialliteracy'
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

