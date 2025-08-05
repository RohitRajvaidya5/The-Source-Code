import tweepy
import os
import emoji


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
            tweet_texts = tweet_file.read().strip()
            print(f"Tweet text ({len(tweet_texts)} chars):", repr(tweet_texts))

        if not tweet_texts:
            raise ValueError("Tweet text is empty. Please add content to tweet.txt.")

        return tweet_texts

    except FileNotFoundError:
        print("Error: tweet.txt file not found.")
    except ValueError as ve:
        print("ValueError:", ve)
    except Exception as e:
        print("An unexpected error occurred while reading tweet:", e)
    return None


def tweet_with_text(client, tweet_texts):
    try:
        # Post the tweet using Twitter API
        response = client.create_tweet(text=tweet_texts)
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


def is_emoji(char):
    return char in emoji.EMOJI_DATA


def check_tweet_length():
    word_count = 0
    with open("tweet.txt", "r", encoding="utf-8") as tweet_file:
        for tweet_line in tweet_file:
            for tweet_char in tweet_line:
                if is_emoji(tweet_char):
                    word_count += 2
                else:
                    word_count += 1

        tweet_limit = 280
        if word_count <= tweet_limit:
            return True
        return False


def get_validated_tweet_text(file_path="tweet.txt", tweet_limit=280):
    try:
        # Read tweet content
        with open(file_path, "r", encoding="utf-8") as tweet_file:
            tweet_text = tweet_file.read().strip()
            print(f"Tweet text ({len(tweet_text)} raw chars):", repr(tweet_text))

        if not tweet_text:
            print("Error: Tweet text is empty. Please add content to tweet.txt.")
            return None

        # Calculate weighted character count
        total_count = 0
        for char in tweet_text:
            total_count += 2 if char in emoji.EMOJI_DATA else 1

        print(f"Calculated tweet length: {total_count} characters (limit: {tweet_limit})")

        if total_count > tweet_limit:
            print(f"Error: Tweet exceeds {tweet_limit} character limit.")
            return None

        return tweet_text

    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return None


def main():
    tweet_text = get_validated_tweet_text()
    if not tweet_text:
        return  # Exit if tweet is invalid

    tweet_client = authenticate_twitter()
    if not tweet_client:
        print("Authentication failed.")
        return

    try:
        tweet_with_text(tweet_client, tweet_text)
        print("Tweet posted successfully.")
    except Exception as e:
        print(f"Failed to post tweet: {e}")


if __name__ == "__main__":
    main()