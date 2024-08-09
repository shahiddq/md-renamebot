import os

class Config(object):
    BANNED_USERS = []
    DOWNLOAD_LOCATION = "./DOWNLOADS" 
    API_ID = int(os.environ.get("API_ID", "29343670"))
    API_HASH = os.environ.get("API_HASH" "28010be97096919fe9511f8ddf1bfc54")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6880909457:AAGIMSvHx7GZzwuf-gvVEhYgzIvpdn4Sy78")
    OWNER_ID = int(os.environ.get("OWNER_ID", "6436690546"))
    AUTH_CHANNEL = os.environ.get("AUTH_CHANNEL", "-1002205632774")
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://ericabraham016:ericabraham016@cluster0.wrdspg0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
