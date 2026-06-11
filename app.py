from flask import Flask, request, jsonify
import os
from http import HTTPStatus
from services.config import *
from services.auth import *
from services.users import *
from services.validator import *
from services.db import *
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

make_env()
make_database()


key = os.environ.get("SECRET_KEY")


@app.route("/register", methods=["POST"])
def register():
    allowed_fields = {"name", "password", "email"}
    data = request.json
    fields_in_data = set(data.keys())
    extra = fields_in_data - allowed_fields
    missing = allowed_fields - fields_in_data
    if extra:
        return jsonify(error="Extra fields in request"), HTTPStatus.BAD_REQUEST
    if missing:
        return jsonify(error="Missing fields in request"), HTTPStatus.BAD_REQUEST

    valid_email = validate_email(data)
    if not valid_email:
        return jsonify(error="Invalid email format"), HTTPStatus.BAD_REQUEST

    user_id = user_register(data)
    if not user_id:
        return jsonify(error="Unable to register user"), HTTPStatus.BAD_REQUEST

    token = create_token(user_id)

    return jsonify(success=f"{token}"), HTTPStatus.CREATED


@app.route("/login", methods=["POST"])
def login():
    allowed_fields = {"email", "password"}
    data = request.json
    fields_in_data = set(data.keys())
    extra = fields_in_data - allowed_fields
    missing = allowed_fields - fields_in_data
    if extra:
        return jsonify(error="Extra fields in request"), HTTPStatus.BAD_REQUEST
    if missing:
        return jsonify(error="Missing fields in request"), HTTPStatus.BAD_REQUEST

    valid_email = validate_email(data)
    if not valid_email:
        return jsonify(error="Please enter valid email"), HTTPStatus.BAD_REQUEST

    user = find_user(data)
    if not user:
        return jsonify(error="Unable to find email"), HTTPStatus.BAD_REQUEST

    token = user_login(data)
    if not token:
        return jsonify(error="Password incorrect"), HTTPStatus.BAD_REQUEST

    return jsonify(success=f"{token}"), HTTPStatus.OK


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port, host="0.0.0.0")
