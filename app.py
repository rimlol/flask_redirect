from flask import Flask, redirect,  url_for, abort, request
from urllib.parse import urlparse
from logic import parse_and_redirect

app = Flask(__name__)


@app.route('/')
def index():
  
    return redirect(parse_and_redirect(request.url))

@app.route('/ann_o/')
def ann_o():
  
    return redirect(parse_and_redirect(request.url))


if __name__ == '__main__':
    app.run()
