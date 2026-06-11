import re
from datetime import datetime


def validate_email(data):
    email = data.get("email")
    pattern = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
    return bool(re.match(pattern, email))


def validate_date(data):
    date = data.get("date")
    try:
        date = datetime.strptime(date, "%d-%m-%Y")
        date = date.strftime("%d-%m-%Y")
        return date
    except ValueError:
        return None
