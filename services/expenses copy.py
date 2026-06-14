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


def all_expenses(user_id, limit, offset, _on, _to, _from, category):
    if _to and _from:
        try:
            expenses = fetch_all(
                """
            select id, title, category, amount, date from expenses 
            where user_id = ? 
            and date >= ? 
            and date <= ?
            limit ? 
            offset ?;
            """,
                (
                    user_id,
                    _from,
                    _to,
                    limit,
                    offset,
                ),
            )
            total = fetch_one(
                """
                select count(*) from expenses 
                where user_id = ?;
                """,
                (user_id,),
            )
            return expenses, total["count(*)"]
        except Exception as e:
            print(e)
            return None
    if category:
        try:
            expenses = fetch_all(
                """
            select id, title, category, amount, date from expenses 
            where user_id = ? 
            and category = ?
            limit ? 
            offset ?;
            """,
                (
                    user_id,
                    category,
                    limit,
                    offset,
                ),
            )
            total = fetch_one(
                """
                select count(*) from expenses 
                where user_id = ?;
                """,
                (user_id,),
            )
            return expenses, total["count(*)"]
        except Exception as e:
            print(e)
            return None
    if _on:
        try:
            expenses = fetch_all(
                """
            select id, title, category, amount, date from expenses 
            where user_id = ? 
            and date = ?
            limit ? 
            offset ?;
            """,
                (
                    user_id,
                    _on,
                    limit,
                    offset,
                ),
            )
            total = fetch_one(
                """
                select count(*) from expenses 
                where user_id = ?;
                """,
                (user_id,),
            )
            return expenses, total["count(*)"]
        except Exception as e:
            print(e)
            return None
    
    if not _on and not _to and not _from and not category:
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
                """
                select count(*) from expenses 
                where user_id = ?;
                """,
                (user_id,),
            )
            return expenses, total["count(*)"]
        except Exception as e:
            print(e)
            return None


def delete_expense(_id, user_id):
    try:
        delete_one(
            """
            delete from expenses 
            where id = ? 
            and user_id = ?;
            """,
            (
                _id,
                user_id,
            ),
        )
        return True
    except Exception as e:
        print(e)
        return None


def update_expense(_id, user_id, data):
    for key, value in data.items():
        try:
            if key == "title":
                update = execute(
                    """
                    update expenses set title = ? 
                    where id = ? and user_id = ?;
                    """,
                    (
                        data["title"],
                        _id,
                        user_id,
                    ),
                )
            if key == "amount":
                update = execute(
                    """
                    update expenses set amount = ? 
                    where id = ? and user_id = ?;
                    """,
                    (
                        data["amount"],
                        _id,
                        user_id,
                    ),
                )
            if key == "category":
                update = execute(
                    """
                    update expenses set category = ? 
                    where id = ? and user_id = ?;
                    """,
                    (
                        str(data["category"]).upper(),
                        _id,
                        user_id,
                    ),
                )
            if key == "date":
                update = execute(
                    """
                    update expenses set date = ? 
                    where id = ? 
                    and user_id = ?;
                    """,
                    (
                        data["date"],
                        _id,
                        user_id,
                    ),
                )
        except Exception as e:
            print(e)
            return None
    expense = fetch_one(
        """
                select id, title, category, amount, date from expenses 
                where id = ? and user_id = ?;
                """,
        (
            _id,
            user_id,
        ),
    )
    return expense
