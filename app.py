from flask import Flask, jsonify, make_response
import re

app = Flask(__name__)


@app.route("/")
def home():
    return "Home Page"


# @app.route('/interfaces')
# def interfaces():
#     return 'interfaces reached'


@app.route('/interfaces')
def interfaces():
    d={}
    res = make_response(jsonify(d), 200)
    return res


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

