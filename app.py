from flask import Flask, render_template, request, send_from_directory  
import json
from pizzapi import *

# Initialize Flask Application
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/pizza_poll', methods=['POST'] )
def pizza_poll():
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 