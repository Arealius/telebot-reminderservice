import os
import mysql.connector

mydb = mysql.connector.connect(
    host=os.environ.get("DB_HOST"),
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASSWORD"),
    database=os.environ.get("DB_NAME")
)

api_token = os.environ.get("BOT_TOKEN")

if not api_token:
    raise Exception("❌ BOT_TOKEN is not set in environment variables")
else:
    print("✅ BOT_TOKEN loaded successfully")

