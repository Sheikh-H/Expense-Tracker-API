from services.config import *

def execute(query, params=()):
    connection = get_db()
    cursor = connection.cursor()
    cursor.execute(query, params)
    connection.commit()
    _id = cursor.lastrowid
    connection.close()
    return _id

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

def delete_one(query, params=()):
    connection = get_db()
    cursor = connection.cursor()
    cursor.execute(query, params)
    connection.close()