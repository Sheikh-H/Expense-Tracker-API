import re
from datetime import datetime
from flask import jsonify
from http import HTTPStatus


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

def validate_date2(datestring):
    try:
        date = datetime.strptime(datestring, "%d-%m-%Y")
        date = date.strftime("%d-%m-%Y")
        return date
    except ValueError:
        return jsonify(error="Please enter correct date format (DD-MM-YYYY)"), HTTPStatus.BAD_REQUEST