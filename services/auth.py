import os
from argon2 import PasswordHasher
import jwt
from jwt import ExpiredSignatureError, InvalidTokenError
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from functools import wraps
from flask import request, jsonify, g
from http import HTTPStatus

load_dotenv()


hasher = PasswordHasher().hash
verifier = PasswordHasher().verify


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        header = request.headers.get("Authorization")
        key = os.environ.get("SECRET_KEY")

        if not header:
            return (
                jsonify(denied="Missing Token, Login/Register."),
                HTTPStatus.UNAUTHORIZED,
            )

        try:
            if header.startswith("Bearer "):
                header = header.split(" ")[1]
            payload = jwt.decode(header, key, algorithms=["HS256"])
            g.user_id = payload["user_id"]
        except ExpiredSignatureError:
            return jsonify(denied="Expired Token"), HTTPStatus.UNAUTHORIZED
        except InvalidTokenError:
            return jsonify(denied="Invalid Token"), HTTPStatus.UNAUTHORIZED
        return func(*args, **kwargs)

    return wrapper


def create_token(user_id):
    key = os.environ.get("SECRET_KEY")
    payload = {
        "user_id": int(user_id),
        "exp": datetime.now(timezone.utc) + timedelta(hours=1),
    }
    token = jwt.encode(payload, key, algorithm="HS256")
    return token


def decode_token(token):
    key = os.environ.get("SECRET_KEY")
    if token.startswith("Bearer "):
        token = token.split(" ")[1]
    payload = jwt.decode(token, key, algorithms=["HS256"])
    user_id = int(payload.get("user_id"))
    return user_id


def hash_password(password):
    password = hasher(password)
    return password


def check_password(stored, entered):
    valid = verifier(stored, entered)
    return valid
