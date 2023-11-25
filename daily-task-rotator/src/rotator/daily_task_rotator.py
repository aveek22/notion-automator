from typing import Optional, Dict, Any, List

from datetime import date
import requests
import json

from rotator.util import get_yesterday, get_today
from rotator.task import Task


class DailyTaskRotator:

    def __init__(self, config):
        self.config = config

    def get_task_due_today(self):
        due_date = get_today()
        return self.get_incomplete_tasks_by_due_date(due_date)

    def udpate_task_due_date_to_today(self, task: Task):
        task_id = task.task_id
        due_date = get_today()
        url = f"{self.config.BASE_URI}pages/{task_id}"
        data = {
            "properties": {
                "Due Date": {
                    "date": {"start": f"{due_date}"}
                }
            }
        }
        print(f"Updating due date for: {task.task_name}")
        response = requests.patch(headers=self.config.HEADERS, url=url, json=data)

        if response.status_code == 200:
            response_json = json.loads(response.text)
            task_title = response_json['properties']['Name']['title'][0]['text']['content']
            print(f"Updated due date for: {task_title}")
        else:
            print(f"Error: {response.status_code}")
            print(response.text)

    def get_tasks_due_yesterday(self) -> Optional[List[Task]]:
        due_date = get_yesterday()
        return self.get_incomplete_tasks_by_due_date(due_date)

    def get_incomplete_tasks_by_due_date(self, due_date) -> Optional[List[Task]]:
        """
        Connects to a Notion database and fetch all tasks by due date
        with a status "Not Started" or "In Progress".
        :return: List of Task
        """

        # TODO: Add filter for incomplete tasks

        url = f"{self.config.BASE_URI}databases/{self.config.database_id}/query"
        data = {
            "filter": {
                "property": "Due Date",
                "date": {
                    "equals": f"{due_date}"
                }
            }
        }
        print(f"Using token: {self.config.token} and database: {self.config.database_id}")
        response = requests.post(headers=self.config.HEADERS, url=url, json=data)

        if response.status_code == 200:
            response_json = json.loads(response.text)
            tasks = response_json["results"]

            return [
                Task(task['id'], task['properties']['Name']['title'][0]['text']['content'])
                for task in tasks if task
            ]

        else:
            print(f"Error: {response.status_code}")
            print(response.text)
            return None
