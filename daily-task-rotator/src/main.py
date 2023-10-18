import os
from dotenv import load_dotenv
from rotator.daily_task_rotator import get_database, get_task_due_today

load_dotenv()
database_id = os.environ.get("DB_TASKS")
token = os.environ.get("NOTION_SECRET")

if __name__ == "__main__":
    # get_database(database_id, token)
    get_task_due_today(database_id, token)
