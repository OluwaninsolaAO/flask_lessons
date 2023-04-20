#!/usr/bin/python3
"""Simple example of redirections and Error"""

from flask import Flask, abort, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        abort(404)
    return """Enter Username and Password\n
            <form action="/login" method="POST">
            <input type="text" placeholder="Username" name="username"><br>
            <input type="password" placeholder="Password" name="password"><br>
            <input type="submit" value="Submit">
            </form>"""

@app.errorhandler(404)
def page_not_found(error):
    return 'Well this is awkward!', 404


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
