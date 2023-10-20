from datetime import datetime


def get_today():
    """Returns the date from local timezone."""
    return datetime.today().date()
