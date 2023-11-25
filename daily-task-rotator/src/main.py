from rotator.daily_task_rotator import DailyTaskRotator
import rotator.config as config


# TODO: Implement logger

def main():
    rotator = DailyTaskRotator(config)

    tasks_due_yesterday = rotator.get_tasks_due_yesterday()
    for task in tasks_due_yesterday:
        rotator.udpate_task_due_date_to_today(task)


if __name__ == "__main__":
    main()
