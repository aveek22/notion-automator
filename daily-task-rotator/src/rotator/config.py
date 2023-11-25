import os
from dotenv import load_dotenv

load_dotenv()
database_id = os.environ.get("DB_TASKS")
token = os.environ.get("NOTION_SECRET")

BASE_URI = "https://api.notion.com/v1/"
HEADERS = {
    'Authorization': f'Bearer {token}',
    'Notion-Version': '2022-06-28',
    'Content-Type': 'application/json'
}
