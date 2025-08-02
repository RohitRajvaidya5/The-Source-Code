import tweepy
import os

# Authenticate
client = tweepy.Client(bearer_token= os.getenv("BEARER_TOKEN"),
                       consumer_key= os.getenv("CONSUMER_KEY"),
                       consumer_secret=os.getenv("CONSUMER_SECRET"),
                       access_token= os.getenv("ACCESS_TOKEN"),
                       access_token_secret=os.getenv("ACCESS_TOKEN_SECRET"))

with open("tweet.txt", "r", encoding="utf-8") as tweet_file:
    tweet_text = tweet_file.read().strip()
    print(f"Tweet text ({len(tweet_text)} chars):", repr(tweet_text))

print(tweet_text)

# Post a tweet
response = client.create_tweet(text= tweet_text)
print("Tweet posted:", response)