import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, timezone

# Load and fix credentials
credentials_raw = os.getenv("GOOGLE_CREDENTIALS_JSON")
credentials_info = json.loads(credentials_raw)
credentials_info["private_key"] = credentials_info["private_key"].replace("\\n", "\n")

# Define scopes and authorize
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials_info, scope)
client = gspread.authorize(creds)
sheet = client.open("lyrics-db").sheet1 # Open the first sheet of the "lyrics-db" spreadsheet

def save_lyric(bot, lyric_index):
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat(sep=' ')
    sheet.append_row([bot, lyric_index, now])

def get_last_lyrics(bot, limit=50):
    records = sheet.get_all_records()
    filtered = [r for r in records if r['bot'] == bot]
    filtered.sort(key=lambda r: r['timestamp'], reverse=True)
    return [(r['lyrics']) for r in filtered[:limit]]