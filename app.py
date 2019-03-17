from flask import Flask, render_template, request, send_from_directory
from pizzapi import *
import os
import json

# Initialize Flask Application
app = Flask(__name__)

@app.route('')
def hello_world():
    return "Hello World!"