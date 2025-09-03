# config.py

import os

# Get bot token from Replit Secrets or environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN", "PUT-YOUR-BOT-TOKEN-HERE")

# You can add admin IDs or log channel here later
ADMINS = []
LOG_CHANNEL_ID = None
DATABASE = "database.json"
