from flask import Flask
from flask import render_template
from datetime import time
from flask import jsonify
from flask import request
from flask import Response
from datetime import datetime
import json
import requests
from one.apiData import *

app = Flask(__name__)


@app.route("/")
def chart():
    return render_template('index.html')

@app.route("/onLoad")
def onLoad():
    currency = "EURUSD=X"
    tf = "1h"
    df = yfinance(currency, tf)
    df = df.to_dict(orient="records")
    return jsonify(result = df)


@app.route("/onClick", methods=['GET', 'POST'])
def onClick():
    currency = request.args.get('currency')
    tf = request.args.get('tf')
    print(currency)
    print(tf)
    df = getData(currency, tf)
    df = df.to_dict(orient="records")
    return jsonify(result = df)

if __name__ == "__main__":
    app.run(debug=True)

