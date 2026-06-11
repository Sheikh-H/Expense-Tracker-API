from flask import Flask, sessions, requests, jsonify
import os

app = Flask(__name__)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port, host="0.0.0.0")