import tweepy
import os
import emoji
import logging
import time

logging.basicConfig(
    filename="tweet_log.log",           # Log file name
    level=logging.INFO,                 # Log level
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filemode='a'                        # Append mode; use 'w' to overwrite each run
)


def retry_tweet(client, tweet_texts, retries=3, delay=5):
    for attempt in range(retries):
        try:
            client.create_tweet(text=tweet_texts)
            logging.info("Tweet posted successfully.")
            print("Tweet posted successfully.")
            return
        except tweepy.errors.TooManyRequests as e:
            logging.warning("Rate limit hit. Retrying...")
            time.sleep(delay * (attempt + 1))
        except Exception as e:
            logging.error(f"Failed to post tweet: {e}")
            return

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
        logging.error(f"Authentication failed: {error}")
        return None

def get_tweet_text():
    try:
        # Read tweet content from text file
        with open("tweet.txt", "r", encoding="utf-8") as tweet_file:
            tweet_texts = tweet_file.read().strip()
            logging.info(f"Tweet text ({len(tweet_texts)} chars): {repr(tweet_texts)}")

        if not tweet_texts:
            raise ValueError("Tweet text is empty. Please add content to tweet.txt.")

        return tweet_texts

    except FileNotFoundError:
        logging.error("Error: tweet.txt file not found.")
    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred while reading tweet: {e}")
    return None

def tweet_with_text(client, tweet_texts):
    try:
        # Post the tweet using Twitter API
        response = client.create_tweet(text=tweet_texts)
        logging.info(f"Tweet posted successfully: {response}")
        print("Tweet posted successfully")

    except tweepy.errors.Forbidden as e:
        logging.error(f"Forbidden error (possibly duplicate tweet or restricted content): {e}")
    except tweepy.errors.TooManyRequests as e:
        logging.error(f"Rate limit exceeded. Try again later: {e}")
    except tweepy.TweepyException as e:
        logging.error(f"Tweepy error occurred: {e}")
    except FileNotFoundError:
        logging.error("Error: tweet.txt file not found.")
    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

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
        return word_count <= tweet_limit

def get_validated_tweet_text(file_path="tweet.txt", tweet_limit=280):
    try:
        # Read tweet content
        with open(file_path, "r", encoding="utf-8") as tweet_file:
            tweet_text = tweet_file.read().strip()
            logging.info(f"Tweet text ({len(tweet_text)} raw chars): {repr(tweet_text)}")

        if not tweet_text:
            logging.error("Error: Tweet text is empty. Please add content to tweet.txt.")
            return None

        # Calculate weighted character count
        total_count = 0
        for char in tweet_text:
            total_count += 2 if char in emoji.EMOJI_DATA else 1

        logging.info(f"Calculated tweet length: {total_count} characters (limit: {tweet_limit})")

        if total_count > tweet_limit:
            logging.error(f"Error: Tweet exceeds {tweet_limit} character limit.")
            return None

        return tweet_text

    except FileNotFoundError:
        logging.error(f"Error: {file_path} not found.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

    return None

def main():
    tweet_text = get_validated_tweet_text()
    if not tweet_text:
        return

    tweet_client = authenticate_twitter()
    if not tweet_client:
        logging.error("Authentication failed.")
        return

    try:
        tweet_with_text(tweet_client, tweet_text)
    except Exception as e:
        logging.error(f"Failed to post tweet: {e}")

if __name__ == "__main__":
    main()
