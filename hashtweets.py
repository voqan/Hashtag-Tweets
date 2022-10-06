# OAuth2.0 Version 
import tweepy
import csv
import sys
import json
from json2html import *
from bson.json_util import dumps
from bson import json_util
import time

# Authentication data (need to be hidden before putting on github)
consumer_key = "FILL ME IN"
consumer_secret = "FILL ME IN"
access_token = "FILL ME IN"
access_token_secret = "FILL ME IN"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Get tweets that contain a hashtag

query = "Kenya"+' -filter:retweets'


tweets = tweepy.Cursor(api.search, q=query,
                              tweet_fields=['context_annotations', 'created_at'], count=100).items(120)

with open('tweets.csv', "a") as csv_file:
    fieldnames = ['Username', 'Name', 'Followers', 'Following', 'Retweets', 'Likes','Tweet_date', 'Tweet']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

for tweet in tweets:
    print("Username         : " + tweet.user.screen_name)
    print("Name         : " + tweet.user.name)
    print("Followers         : " + str(tweet.user.followers_count))
    print("Following         : " + str(tweet.user.friends_count))
    print("Retweets         : " + str(tweet.retweet_count))
    print("Likes         : " + str(tweet.favorite_count))
    print("Tweet date         : " + str(tweet.created_at))
    print("Tweet         : " + tweet.text, end = "\n\n")

    if tweet is not None:
        try:
            data = {'Username': tweet.user.screen_name, 'Name': tweet.user.name, 'Followers': str(tweet.user.followers_count), 'Following': str(tweet.user.friends_count), 'Retweets': str(tweet.retweet_count), 'Likes': str(tweet.favorite_count), 'Tweet_date': str(tweet.created_at), 'Tweet': tweet.text}

            with open('tweets.csv', "a") as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writerow(data)
        except:
            print("ERROR : No Tweets")

