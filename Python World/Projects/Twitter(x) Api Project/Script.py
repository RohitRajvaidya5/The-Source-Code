import tweepy
import os

# Authenticate
client = tweepy.Client(bearer_token= os.getenv("BEARER_TOKEN"),
                       consumer_key= os.getenv("CONSUMER_KEY"),
                       consumer_secret=os.getenv("CONSUMER_SECRET"),
                       access_token= os.getenv("ACCESS_TOKEN"),
                       access_token_secret=os.getenv("ACCESS_TOKEN_SECRET"))

# Post a tweet
response = client.create_tweet(text="Hello Twitter from Tweepy!")
print("Tweet posted:", response)
