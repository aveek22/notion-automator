import os
from dotenv import load_dotenv
from rotator.daily_task_rotator import get_database, get_task_due_today, get_task_due_yesterday, udpate_task_due_date
from rotator.util import get_yesterday, get_today

load_dotenv()
database_id = os.environ.get("DB_TASKS")
token = os.environ.get("NOTION_SECRET")

if __name__ == "__main__":
    # get_database(database_id, token)
    # get_task_due_today(database_id, token)
    task_details = get_task_due_yesterday(database_id, token)
    # print(task_details["task_id"])
    udpate_task_due_date(task_id=task_details["task_id"], due_date=get_today(), token=token)
