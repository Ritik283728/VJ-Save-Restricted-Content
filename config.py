import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "29290111"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "f6a2bd2b9aa6aa06fbba8c14a3fba29d")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://kimari8965:arskumarok@cluster0.gm4qa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
