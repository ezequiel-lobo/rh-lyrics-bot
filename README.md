# rh-lyrics-bot
A Python bot that tweets random lyrics from on of my favorite bands

## Features

- Tweets random lyrics from a specified band.
- Supports multiple bands by adding more `.txt` files to the `data` folder.
- Tracks recently tweeted lyrics to minimize repeats.
- Uses Google Sheets as a lightweight database.

## Setup

The bot requires several environment variables for configuration:

- `GOOGLE_CREDENTIALS_JSON`: The JSON credentials for your Google Service Account (as a single line string).
- `TWITTER_API_KEY`, `TWITTER_API_SECRET`, `TWITTER_ACCESS_TOKEN`, `TWITTER_ACCESS_TOKEN_SECRET`: Your Twitter API credentials (if tweeting).
- Any other variables your app needs.

### Setting Environment Variables on Heroku

1. Go to your app dashboard on [Heroku](https://dashboard.heroku.com/).
2. Click on your app, then go to **Settings**.
3. Click **Reveal Config Vars**.
4. Add each variable and its value (copy the entire JSON for `GOOGLE_CREDENTIALS_JSON` as a single line).

## Deploying to Heroku

1. **Clone your repository:**
    ```sh
    git clone https://github.com/yourusername/rh-lyrics-bot.git
    cd rh-lyrics-bot
    ```

## Usage

- Add your lyrics files to the `data` folder (one line per lyric).
- The bot will automatically detect available bands based on the `.txt` files.
- Schedule the bot using Heroku Scheduler or another method if you want periodic tweets.

---

**Note:**  
Make sure your Google Service Account has access to the Google Sheet you want to use as a database.