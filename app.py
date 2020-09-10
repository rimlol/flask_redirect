from flask import Flask, redirect,  url_for, abort, request
from urllib.parse import urlparse
from logic import parse_and_redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
  
    return redirect(parse_and_redirect(request.url))

if __name__ == '__main__':
    app.run()
