from datetime import datetime, timedelta


def get_today():
    """Returns the date from local timezone."""
    return datetime.today().date()


def get_yesterday():
    """Returns the date from local timezone."""
    return datetime.today().date() - timedelta(days=1)


if __name__ == "__main__":
    print(get_yesterday())
    print(get_today())
