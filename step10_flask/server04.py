import random
from urllib.parse import urlencode
import requests
import pandas as pd
from urllib.request import urlopen, Request
import xml.etree.ElementTree as ET
from flask import Flask

app = Flask(__name__)

# 태그 사용 가능
@app.route('/')
def hello_world():
    # 접속할때마다 random으로 숫자가 나온다
    return '<h2>random: ' + str(random.random()) + '</h2>'

@app.route('/create')
def create():
    return '<h2> Create </h2>'

@app.route('/read/<id>')
def read(id):
    return '<h2> Read %s </h2>' %id

# 디버깅 실행 형식
app.run(debug=True)