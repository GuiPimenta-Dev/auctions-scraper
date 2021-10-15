import json
from urllib.parse import urlencode

from flask import Flask, request
from flask_cors import CORS
import requests
import urllib


from flask_runner import Runner

app = Flask(__name__)
CORS(app)
runner = Runner()

@app.route('/home')
def home():
    return 'Home'

@app.route("/")
def run_robots():
    state_city = request.args.get('state_city', '')
    params = {
        'spider_name':'zukerman',
        'start_requests': True,
        'crawl_args' : '%7B%E2%80%9Ccity%E2%80%9D%3A%20state_city%7D%20'
    }
    response = requests.get('http://localhost:9080/crawl.json', params)
    return json.loads(response.text)
    # try:
    #     data = runner.run_robots(state_city)
    # except:
    #     data = []

    # return data


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
