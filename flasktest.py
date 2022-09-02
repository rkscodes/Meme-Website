#!/opt/homebrew/opt/python/libexec/bin/python

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Drink more coffee"


app.run(host="0.0.0.0", port=80)
