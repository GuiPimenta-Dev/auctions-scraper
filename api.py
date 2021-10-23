import json
from urllib.parse import urlencode

from flask import Flask, request
from flask_cors import CORS
import requests
import urllib


from auctions.flask_runner import Runner

app = Flask(__name__)
CORS(app)
runner = Runner()

@app.route('/home')
def home():
    return 'Home'

@app.route("/")
def run_robots():
    state_city = request.args.get('state_city', '')
    try:
        data = runner.run_robots(state_city)
    except Exception as e:
        data = str(e)

    return data


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
