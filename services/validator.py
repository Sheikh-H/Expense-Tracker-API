import re

def validate_email(data):
    email = data.get("email")
    pattern = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
    return bool(re.match(pattern, email))