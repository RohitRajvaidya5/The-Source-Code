import tweepy

# Authenticate
client = tweepy.Client(bearer_token='YOUR_BEARER_TOKEN',
                       consumer_key='YOUR_API_KEY',
                       consumer_secret='YOUR_API_SECRET',
                       access_token='YOUR_ACCESS_TOKEN',
                       access_token_secret='YOUR_ACCESS_SECRET')

# Post a tweet
response = client.create_tweet(text="Hello Twitter from Tweepy!")
print("Tweet posted:", response)
