#!/usr/bin/python3
"""Creates a simple routing with flash"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is index page'

@app.route('/hello')
def hello():
    return 'Hello there, we meet again!'


if __name__ == '__main__':
    app.run()
