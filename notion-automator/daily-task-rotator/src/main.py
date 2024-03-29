from rotator.daily_task_rotator import DailyTaskRotator
import rotator.config as config


# TODO: Implement logger
# TODO: Send update to slack / email for due today
# TODO: Implement code to read secrets from AWS Secret Manager
# TODO: Manual Terraform deploy to AWS - INPROGRESS
# TODO: Figure out the entire build process and CICD for Lambda

def handler(event, context):
    rotator = DailyTaskRotator(config)

    tasks_due_yesterday = rotator.get_tasks_due_yesterday()
    for task in tasks_due_yesterday:
        rotator.udpate_task_due_date_to_today(task)


if __name__ == "__main__":
    handler("", "")
