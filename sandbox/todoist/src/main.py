import requests
from todoist_api_python.api import TodoistAPI
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ.get("ACCESS_TOKEN")

def main():
    print(f"Using token {TOKEN}")
    get_tasks_sync()


def get_tasks_sync():
    api = TodoistAPI(TOKEN)
    try:
        tasks = api.get_tasks()
        for task in tasks:
            print(task)
            print("\n")
    except Exception as error:
        print(error)


def get_projects_sync():
    api = TodoistAPI(TOKEN)
    try:
        projects = api.get_projects()
        print(projects)
    except Exception as error:
        print(error)

if __name__ == "__main__":
    main()