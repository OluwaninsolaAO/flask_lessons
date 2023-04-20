#!/usr/bin/python3
"""Simple url building using `url_for`"""

from flask import Flask, url_for, escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world!'

@app.route('/users/<username>')
def users(username):
    with app.test_request_context():
        return f"{url_for('users', username=username, id=89)}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
