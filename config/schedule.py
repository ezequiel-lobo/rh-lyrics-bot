import schedule
import logging
from bot.lyrics_bot import tweet_lyrics, test

# Configure logging once at the top-level
logging.basicConfig(level=logging.INFO)

# Schedule for the Radiohead bot. Timezone is set to UTC.
schedule_times = {
    "radiohead": ["03:15", "07:15", "11:15", "15:15", "19:15", "23:15", "01:15"]
    # You can add more bots and their respective times here if needed
    # Example:
    # "depeche_mode": ["02:00", "06:00", "10:00", "14:00", "18:00", "22:00"]
}

def setup_schedules():
    """
    Setup the schedules for the application.
    This function is called to initialize all scheduled tasks.
    """
    for bot, times in schedule_times.items():
        for time_str in times:
            # Schedule the tweet_lyrics function for each bot at its specified times (UTC)
            schedule.every().day.at(time_str, tz="UTC").do(tweet_lyrics, bot) 
    # Add logging to confirm schedules are set up
    logging.info(
        "Schedules have been set up successfully for bots: %s",
        {bot: times for bot, times in schedule_times.items()}
    )

def test_schedules():
    """
    Test the schedules by running them immediately.
    This is useful for debugging and ensuring that the scheduled tasks work as expected.
    """
    schedule.every(10).seconds.do(test, "radiohead")