import json

from flask import Flask
from flask import request, make_response, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def test_request():
    response = {'name': 'atsuo'}
    return make_response(jsonify(response))

if __name__ == '__main__':
    app.run()
