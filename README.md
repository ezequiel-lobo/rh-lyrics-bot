# Radiohead Lyrics Bot
A Python bot that tweets random lyrics from one of my favorite bands. Built with:
- **[Python 3.9](https://www.python.org/)**
- **[Tweepy](https://www.tweepy.org/)**
- **[gspread](https://gspread.readthedocs.io/)**
- **[oauth2client](https://oauth2client.readthedocs.io/)**
- **[schedule](https://schedule.readthedocs.io/)** 
- **[Heroku](https://www.heroku.com/)**

## Features

- Tweets random lyrics from a specified band (Supports multiple bands by adding more `.txt` files to the `data` folder)
- Tracks recently tweeted lyrics to avoid repetition using Google Sheets as a database

## Setup

- [Create an X app](https://developer.x.com/en) with your bot's account
- Set access tokens in your Heroku app:
    ```sh
    heroku config:set GOOGLE_CREDENTIALS_JSON=XXXXX
    heroku config:set TWITTER_API_KEY=XXXXX
    heroku config:set TWITTER_API_SECRET=XXXXX
    heroku config:set TWITTER_ACCESS_TOKEN=XXXXX
    heroku config:set TWITTER_ACCESS_TOKEN_SECRET=XXXXX
    ```
- Add your lyrics files to the `data` folder (one line per lyric). The bot will automatically detect available bands based on the `.txt` files.
- Schedule the bot using Heroku Scheduler or edit 'scheduler.py'
- Create a Google Sheet to use as a database and connect it with your Google Service Account

---

Checkout this cool examples: [@radioheadbot_](https://x.com/radioheadbot_), [@qotsalyricsbot_](https://x.com/qotsalyricsbot_) and [@fontainesdcbot_](https://x.com/fontainesdcbot_)
