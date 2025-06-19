from utils.auth.twitter_auth import get_twitter_client
from utils.reader import reader
from utils.db import save_lyric, get_last_lyrics
from datetime import datetime, timezone
import random

def last_lyrics_assigner(bot, selected_lyrics):
    save_lyric(bot, selected_lyrics)

def generate_lyrics(bot, lyrics=None):
    """
    Generates a random lyrics from the provided lyrics list. 
    """
    if lyrics is None:
        lyrics = reader(bot)
    last_lyrics = get_last_lyrics(bot)
    
    while True: 
        selected_lyrics = random.choice(lyrics)
        if selected_lyrics not in last_lyrics:
            break
    
    if len(last_lyrics) >= 96:
        last_lyrics[:] = last_lyrics[-48:]
        # Persist the truncated history if needed
        if hasattr(save_lyric, "save_history"):
            save_lyric.save_history(bot, last_lyrics)
    last_lyrics_assigner(bot, selected_lyrics)
    
    return selected_lyrics, lyrics

# Tweet lyrics 
def tweet_lyrics(bot): 
    """
    Calls the Twitter API to share the lyrics
    """
    lyrics = reader(bot)
    selected_lyrics, _ = generate_lyrics(bot, lyrics)
    client, _ = get_twitter_client(bot)
    if not client:
        print("Failed to authenticate Twitter client.")
        return
    client.create_tweet(text=selected_lyrics)
    # Log the lyrics index for debugging
    print(f"Tweeted lyrics: {selected_lyrics} Bot: {bot} at {datetime.now(timezone.utc).replace(microsecond=0).isoformat(sep=' ')}")

def test(bot):
    """
    Test function to tweet lyrics immediately.
    This is useful for debugging and ensuring that the tweet_lyrics function works as expected.
    """
    lyrics = reader(bot)
    selected_lyrics, _ = generate_lyrics(bot, lyrics)
    print(selected_lyrics)