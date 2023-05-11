#!/usr/bin/env python3
"""API Routes """
from auth import Auth
from flask import Flask, jsonify, request, abort, redirect


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def index() -> str:
    """ Base route for authentication service API """
    txt = {"message": "Bienvenue"}
    return jsonify(txt)

d@app.route('/users', methods=['POST'])
def register_user() -> str:
    """USERS REGISTERS"""
    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError:
        abort(400)

    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    text = {"email": email, "message": "user created"}
    return jsonify(text)


if __name__ == "__main":
    app.run(host="0.0.0.0",port="5000")
