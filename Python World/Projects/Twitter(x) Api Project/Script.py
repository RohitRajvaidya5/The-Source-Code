import tweepy
import os

try:
    # Authenticate
    client = tweepy.Client(
        bearer_token=os.getenv("BEARER_TOKEN"),
        consumer_key=os.getenv("CONSUMER_KEY"),
        consumer_secret=os.getenv("CONSUMER_SECRET"),
        access_token=os.getenv("ACCESS_TOKEN"),
        access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
    )

    # Read tweet from file
    with open("tweet.txt", "r", encoding="utf-8") as tweet_file:
        tweet_text = tweet_file.read().strip()
        print(f"Tweet text ({len(tweet_text)} chars):", repr(tweet_text))

    if not tweet_text:
        raise ValueError("Tweet text is empty. Please add content to tweet.txt.")

    # Post a tweet
    response = client.create_tweet(text=tweet_text)
    print("Tweet posted successfully:", response)

except tweepy.errors.Forbidden as e:
    print("Forbidden error (possibly duplicate tweet or restricted content):", e)
except tweepy.errors.TooManyRequests as e:
    print("Rate limit exceeded. Try again later:", e)
except tweepy.TweepyException as e:
    print("Tweepy error occurred:", e)
except FileNotFoundError:
    print("Error: tweet.txt file not found.")
except ValueError as ve:
    print("ValueError:", ve)
except Exception as e:
    print("An unexpected error occurred:", e)
