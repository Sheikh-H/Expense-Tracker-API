from services.auth import *
from services.db import *


def user_register(data):
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    hash = hash_password(password)
    try:
        execute(
            """
                insert into users 
                (name, email, hash)
                values (?, ?, ?)
                ;""",
            (
                name,
                email,
                hash,
            ),
        )
        user_id = fetch_one(
            """
                            select id from users 
                            where email = ?
                            ;""",
            (email,),
        )
        return int(user_id)
    except:
        return None
