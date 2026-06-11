from services.config import *

def execute(query, params=()):
    connection = get_db()
    connection.execute(query, params)
    connection.commit()
    connection.close()

def fetch_one(query, params=()):
    connection = get_db()
    cursor = connection.cursor()
    cursor.execute(query, params)
    row = cursor.fetchone()
    connection.close()
    return row

def fetch_all(query, params=()):
    connection = get_db()
    cursor = connection.cursor()
    cursor.execute(query, params)
    rows = cursor.fetchall()
    connection.close()
    return rows

