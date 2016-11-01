import json
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/suggestions')
def suggestions():
	with open('sample.json') as data_file:
    		data = json.load(data_file)
        return jsonify(data)
