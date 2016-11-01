from flask import Flask, request, json, jsonify
app = Flask(__name__)

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/events', methods = ['PUT'])
def add_event():

    if request.headers['Content-Type'] == 'application/json':
	with open("sample.json", "w") as sample:
	   sample.write(json.dumps(request.json))
        return "JSON format recognised! Message: " + json.dumps(request.json)
    else:
        return "415 Unsupported Media Type ;)"

@app.route('/events', methods = ['GET'])
def suggestions():
        with open("sample.json", "r") as el:
           data = json.load(el)
        return jsonify(data)
