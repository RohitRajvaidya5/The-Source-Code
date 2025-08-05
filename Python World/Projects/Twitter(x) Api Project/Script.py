import tweepy
import os


def authenticate_twitter():
    try:
        # Authenticate with Twitter API using environment variables
        client = tweepy.Client(
            bearer_token=os.getenv("BEARER_TOKEN"),
            consumer_key=os.getenv("CONSUMER_KEY"),
            consumer_secret=os.getenv("CONSUMER_SECRET"),
            access_token=os.getenv("ACCESS_TOKEN"),
            access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
        )
        return client

    except Exception as error:
        print(f"Authentication failed: {error}")


def get_tweet_text():
    try:
        # Read tweet content from text file
        with open("tweet.txt", "r", encoding="utf-8") as tweet_file:
            tweet_text = tweet_file.read().strip()
            print(f"Tweet text ({len(tweet_text)} chars):", repr(tweet_text))

        if not tweet_text:
            raise ValueError("Tweet text is empty. Please add content to tweet.txt.")

        return tweet_text

    except FileNotFoundError:
        print("Error: tweet.txt file not found.")
    except ValueError as ve:
        print("ValueError:", ve)
    except Exception as e:
        print("An unexpected error occurred while reading tweet:", e)

    return None


def tweet_with_text(client, tweet_text):
    try:
        # Post the tweet using Twitter API
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


if __name__ == "__main__":
    # Main execution flow
    twitter_client = authenticate_twitter()

    if twitter_client:
        tweet_content = get_tweet_text()

        if tweet_content:
            tweet_with_text(twitter_client, tweet_content)