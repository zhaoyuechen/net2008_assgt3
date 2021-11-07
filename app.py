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
    # reade interfaces.txt
    with open("interfaces.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            if "Link" in line:
                # find interface name
                names = line.split(":")
                name = names[0].strip()
                # find ip address
                ipadds = re.compile(r'addr:(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
                ipadds = re.findall(ipadds, line)
                ipadd = ipadds[0]
                # add ComputerInterfaces to d
                d[name.split(" ")[0]] = ipadd
        d = {"ComputerInterfaces": d}
    res = make_response(jsonify(d), 200)
    return res


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

