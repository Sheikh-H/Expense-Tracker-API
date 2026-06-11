from flask import Flask, sessions, request, jsonify
import os
from services.config import *
from dotenv import load_dotenv

app = Flask(__name__)

make_env()

load_dotenv()




if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port, host="0.0.0.0")