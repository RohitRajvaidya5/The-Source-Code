import tweepy

# Authenticate
client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAIRs3QEAAAAADy2ef%2FfbQy%2BWK5QJyxFy600PlFQ%3D3N2dmQe3Al8zGGwi9dCCtyKt7cxSh96g28hORMnj4NkVxKKZ3s',
                       consumer_key='LMEUaIxAjA3bSqXrxUUDbYeDV',
                       consumer_secret='o8qf02oBlIlHPSeooGCX5FagCRHACRnMkbXmcWb8i4R3AX0XNB',
                       access_token='1950948712840052736-rAUX1GE1kJumstSbw4HMM2pbVe9qRz',
                       access_token_secret='G4ntHvtbcE9bP81XXd2tqvcr3BB3JGpZRXrx4UFRyNK6j')

# Post a tweet
response = client.create_tweet(text="Hello Twitter from Tweepy!")
print("Tweet posted:", response)
