import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "31576348"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "b036c1a134fcbf3f5b3cc2f9af2415ac")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "9080858036:AAGALTHYw1l52RDWzTiffYHqM_x4CqOVlI0")

OWNER_ID = int(os.environ.get("OWNER_ID", "5999785669"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003958253583"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "")  # Optional here you'll get all logs
