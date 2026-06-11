from datetime import datetime

def add_expense(data):
    title = data.get("title")
    amount = float(data.get("amount"))