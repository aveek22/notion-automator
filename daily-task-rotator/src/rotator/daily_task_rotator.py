import requests
import json


def get_database(database_id: str, token: str):
    url = f"https://api.notion.com/v1/databases/{database_id}"
    headers = {
        'Authorization': f'Bearer {token}',
        'Notion-Version': '2022-06-28',
        'Content-Type': 'application/json'
    }
    print(f"Using token: {token} and database: {database_id}")
    response = requests.get(headers=headers, url=url)

    if response.status_code == 200:
        response_json = json.loads(response.text)
        print(f"Database name: {response_json['title'][0]['text']['content']}")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)


def get_task_due_today(database_id: str, token: str):
    url = f"https://api.notion.com/v1/databases/{database_id}/query"
    headers = {
        'Authorization': f'Bearer {token}',
        'Notion-Version': '2022-06-28',
        'Content-Type': 'application/json'
    }
    data = {
        "filter": {
            "property": "Due Date",
            "date": {
                "equals": "2023-10-18"
            }
        }
    }
    print(f"Using token: {token} and database: {database_id}")
    response = requests.post(headers=headers, url=url, json=data)

    if response.status_code == 200:
        response_json = json.loads(response.text)
        print(f"Task Name: {response_json['results'][0]['properties']['Name']['title'][0]['text']['content']}")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
