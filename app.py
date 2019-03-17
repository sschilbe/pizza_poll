from flask import Flask, render_template, request, send_from_directory, jsonify
import json
from pizzapi import *
import sys
import logging

# Initialize Flask Application
app = Flask(__name__)
gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/pizza_poll', methods=['POST'] )
def pizza_poll():
    app.logger.info("%s\n", request.form )
    text = request.form["text"]
    app.logger.info("%s\n", text )

    customer = Customer( text.split("\"")[1] )
    address = Address( text.split("\"")[3] )
    store = address.closest_store()
    menu = store.get_menu()
    menu.search(Name='Coke')

    return jsonify( {   "response_type": "in_channel",
                        "text": "test" } )