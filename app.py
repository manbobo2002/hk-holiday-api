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


@app.route("/post_submit", methods=['POST'])
def submit():
    print("here")
    year = request.args.get('year-input')
    print (year)
    # url='https://www.gov.hk/en/about/abouthk/holiday/'.join(year)+'htm'
    return year


if __name__ == '__main__':
    # app.run(port=5002, debug=True)

    # Serve the app with gevent
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    http_server.serve_forever()
