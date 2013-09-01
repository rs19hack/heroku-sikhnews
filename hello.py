import os
from flask import Flask
#import urllib3

currentpage = 'Placeholder....'

app = Flask(__name__)

@app.route('/')

def hello():
	return currentpage