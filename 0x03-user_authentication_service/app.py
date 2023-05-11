#!/usr/bin/env python3
"""API Routes """
from auth import Auth
from flask import (Flask,
                   jsonify,
                   request,
                   abort,
                   redirect)

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def index() -> str:
    """ Base route for authentication service API """
    txt = {"message": "Bienvenue"}
    return jsonify(txt)





if __name__ == "__main":
    app.run(host="0.0.0.0",port="5000")
