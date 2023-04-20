#!/usr/bin/python3
"""Simple http methods handling"""

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Home Page</h1>'

@app.route('/login', methods=['GET', 'POST', 'PUT', 'DELETE', 'UPDATE'])
def login():
    return f'HTTP request via {request.method} method'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
