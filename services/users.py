from services.auth import *
from services.db import *
from services.auth import *


def user_register(data):
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    hash = hash_password(password)
    try:
        user = fetch_one(
            """
            select * from users 
            where email = ?
            ;""",
            (email,),
        )
        if user:
            return None
        user_id = execute(
            """
                insert into users (name, email, hash)
                values (?, ?, ?)
                ;""",
            (
                name,
                email,
                hash,
            ),
        )

        return user_id
    except Exception as e:
        print(e)
        return None


def find_user(data):
    email = data.get("email").strip()
    try:
        user = fetch_one(
            """
            select * from users 
            where email = ?;
            """,
            (email,),
        )
        return user
    except Exception as e:
        print(e)
        return None


def user_login(data):
    password = data.get("password").strip()
    existing = find_user(data)
    try:
        verifier(existing["hash"], password)
        token = create_token(existing["id"])
        return token
    except Exception as e:
        print(e)
        return None
