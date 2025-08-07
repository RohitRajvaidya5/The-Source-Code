import pytest
from unittest.mock import patch, MagicMock, mock_open
import tweepy
import builtins
from tweepy.errors import Forbidden, TooManyRequests
from requests.models import Response
from Script import authenticate_twitter, get_tweet_text, tweet_with_text


def test_authenticate_twitter_success(monkeypatch):
    # Mock environment variables
    monkeypatch.setenv("BEARER_TOKEN", "dummy_bearer")
    monkeypatch.setenv("CONSUMER_KEY", "dummy_ck")
    monkeypatch.setenv("CONSUMER_SECRET", "dummy_cs")
    monkeypatch.setenv("ACCESS_TOKEN", "dummy_at")
    monkeypatch.setenv("ACCESS_TOKEN_SECRET", "dummy_ats")

    client = authenticate_twitter()
    assert isinstance(client, tweepy.Client)


def test_get_tweet_text_success(monkeypatch):
    tweet_content = "Hello from Pytest"
    m = mock_open(read_data=tweet_content)
    monkeypatch.setattr(builtins, "open", m)

    result = get_tweet_text()
    assert result == tweet_content


def test_get_tweet_text_empty(monkeypatch):
    m = mock_open(read_data="   ")
    monkeypatch.setattr(builtins, "open", m)

    result = get_tweet_text()
    assert result is None


def test_get_tweet_text_file_not_found(monkeypatch):
    monkeypatch.setattr(builtins, "open", lambda f, *args, **kwargs: (_ for _ in ()).throw(FileNotFoundError()))
    result = get_tweet_text()
    assert result is None


def test_tweet_with_text_success():
    client = MagicMock()
    client.create_tweet.return_value = {"data": {"id": "123", "text": "Hello"}}

    tweet_text = "Mocked tweet"
    tweet_with_text(client, tweet_text)

    client.create_tweet.assert_called_once_with(text=tweet_text)


def test_tweet_with_text_forbidden_error():
    client = MagicMock()

    # Create a fake response object
    response = Response()
    response.status_code = 403

    # Raise the Forbidden error with response
    client.create_tweet.side_effect = Forbidden(response=response)

    tweet_with_text(client, "Test forbidden")


def test_tweet_with_text_rate_limit():
    client = MagicMock()

    # Create a fake response object
    response = Response()
    response.status_code = 429

    # Raise the TooManyRequests error with response
    client.create_tweet.side_effect = TooManyRequests(response=response)

    tweet_with_text(client, "Test rate limit")


def test_tweet_with_text_generic_error():
    client = MagicMock()
    client.create_tweet.side_effect = Exception("Something went wrong")

    tweet_with_text(client, "Generic error")
