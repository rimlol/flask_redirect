from flask import Flask, redirect,  url_for, abort, request
from urllib.parse import urlparse
from logic import parse_and_redirect, geekschool_parse_and_redirect
from ann_logic import find_spec

app = Flask(__name__)


@app.route('/')
def index():

    return redirect(parse_and_redirect(request.url))

@app.route('/ann_o/')
def ann_o():

    return redirect(find_spec(request.url))

@app.route('/geek_school/')
def geek_school():

    return redirect(geekschool_parse_and_redirect(request.url))


if __name__ == '__main__':
    app.run()
