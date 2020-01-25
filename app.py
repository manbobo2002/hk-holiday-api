from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np

import requests
import lxml.html as lh
import pandas as pd

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)



@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route("/post_submit", methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        url = 'https://www.gov.hk/en/about/abouthk/holiday/'+request.json['yearinput']    +'.htm'
        html = requests.get(url).content
        df_list = pd.read_html(html)
        df = df_list[0]
        df = df.drop(df.columns[[0]],axis=0)
        print(df)
        # Indication of expected JSON string format 
        return df.to_json(orient ='index')
    return render_template('index.html')


if __name__ == '__main__':
    # app.run(port=5002, debug=True)

    # Serve the app with gevent
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    http_server.serve_forever()
