from datetime import datetime
from services.db import *


def add_expense(data):
    title = data.get("title")
    amount = float(data.get("amount"))
    category = str(data.get("category")).upper()
    date = data.get("date")
    user_id = int(data.get("user_id"))
    try:

        _id = execute(
            """
            insert into expenses (user_id, title, category, amount, date)
            values (?, ?, ?, ?, ?);
            """,
            (user_id, title, category, amount, date),
        )
        expense = {
            "id": int(_id),
            "title": title,
            "category": category,
            "amount": f"£{amount:.2f}",
            "date": date,
        }
        return expense
    except Exception as e:
        print(e)
        return None


def all_expenses(user_id, limit, offset):
    try:
        expenses = fetch_all(
            """
        select id, title, category, amount, date from expenses 
        where user_id = ? 
        limit ? 
        offset ?;
        """,
            (
                user_id,
                limit,
                offset,
            ),
        )
        total = fetch_one(
            """select count(*) from expenses where user_id = ?;""",
            (user_id,),
        )
        return expenses, total['count(*)']
    except Exception as e:
        print(e)
        return None
