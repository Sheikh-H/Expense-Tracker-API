import os
import secrets
import sqlite3
from dotenv import load_dotenv

load_dotenv()


def make_env():
    if not os.path.exists(".env"):
        key = secrets.token_hex(16)
        with open(".env", "w") as f:
            f.write(f"SECRET_KEY={key}")


def get_db():
    connection = sqlite3.connect("instance/expense.db")
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON;")
    return connection


def make_database():
    connection = get_db()
    connection.execute("""
        create table if not exists users (
            id integer primary key autoincrement,
            name text not null, 
            email text unique not null, 
            hash text not null
        );
        """)
    connection.commit()
    connection.execute("""
        create table if not exists expenses (
            id integer primary key autoincrement, 
            user_id integer not null,
            title text not null, 
            category text not null,
            amount real not null,
            date text not null, 
            foreign key (user_id) references users(id) on delete cascade
        );
        """)
    connection.commit()
    connection.close()
