from flask import Flask, request
from flask_cors import CORS

from flask_runner import Runner, MyWorker

app = Flask(__name__)
CORS(app)
runner = Runner()


@app.route("/")
def run_robots():
    state_city = request.args.get('state_city', '')
    MyWorker('param_value')
    try:
        data = runner.run_robots(state_city)
    except:
        data = []

    return data


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
