"""Simple use case of make response header

>>> from flask import Flask, make_response
>>> app = Flask(__name__)
>>> @app.route('/')
... def index():
...     resp = make_response("Make custom response", 404)
...     resp.headers['X-my-header'] = "Awesome Header"
...     return resp
...
>>> with app.test_request_context():
...     obj = index()
...     print(obj.headers)
...
Content-Type: text/html; charset=utf-8
Content-Length: 20
X-my-header: Awesome Header
