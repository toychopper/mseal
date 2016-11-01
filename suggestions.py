from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/suggestions')
def suggestions():
    list = [
        {
          "title": "Bald Girl playing violin",
          "description": "One time only, never to see again",
          "link": "/events/1"
        },
        {
          "title": "Dumb Fish Lost At Sea",
          "description": "fun for the whole family",
          "link": "/events/2"
        },
        {
          "title": "Celebrity Chef cooking his own hair",
          "description": "A fine cousine masterclass",
          "link": "/events/3"
    }

    ]
    return jsonify(results = list)
