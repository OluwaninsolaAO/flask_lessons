#!/usr/bin/python3
"""Simple variable rules for routing with flask"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Index!"

@app.route('/user/<username>')
def users(username):
    return f'Hello there {username}!'

smiley = [ '😎', '😋', '🤗', '🤓', '👻', '🐶', '🐱' ]

@app.route('/emojis/<int:num>')
def emojis(num):
    return f'Your choice of index [{num}] is {smiley[num]}'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
