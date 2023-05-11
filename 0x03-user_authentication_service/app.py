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

@app.route('/users')
"""def users():
     user endpoint 
    if request.method == 'POST':
        email = request.form('email')
        password = request.form('passord')

    try:
        AUTH.register(email=email, password=password)
         return jsonify({'email': email, 'message': 'user created'})
    except ValueError:
 return jsonify({'message': 'email already registered'}), 400 """

def users():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        try:
            AUTH.register(email=email, password=password)
            return jsonify({'email': email, 'message': 'user created'})
        except ValueError:
            return jsonify({'message': 'email already registered'}), 400



if __name__ == "__main":
    app.run(host="0.0.0.0",port="5000")
