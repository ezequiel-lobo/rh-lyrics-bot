import tweepy
import os

def get_twitter_client(bot):
    """
    Returns a Tweepy client authenticated with the provided credentials.
    """
    bot = bot.upper()
    BEARER_TOKEN = os.getenv(f"{bot}_BEARER_TOKEN")
    API_KEY = os.getenv(f"{bot}_API_KEY")
    API_SECRET = os.getenv(f"{bot}_API_SECRET")
    ACCESS_KEY = os.getenv(f"{bot}_ACCESS_KEY")
    ACCESS_SECRET = os.getenv(f"{bot}_ACCESS_SECRET")
    client = tweepy.Client(BEARER_TOKEN, API_KEY, API_SECRET, ACCESS_KEY, ACCESS_SECRET)
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    return client, api