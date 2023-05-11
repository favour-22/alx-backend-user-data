#!/usr/bin/env python3
"""API routes for auth"""
from auth import Auth
from flask import Flask,request,abort,redirect,jsonify

app=Flask(__name__)
AUTH =Auth()


@app.route('/',methods=['GET'])
def index() ->str:
    """BASE ROUTE"""
    text = {"message": "Bienvenue"}
    return jsonify(text)





if __name__ == "__main":
    app.run(host="0.0.0.0",port="5000")
