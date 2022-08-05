import logging
from flask import Flask, jsonify

app = Flask(__name__)

@app.post('/api/user')
def register():
    return jsonify({
        "message": "success"
    }), 200


@app.after_request
def add_header_response(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Access-Control-Allow-Origin, Api-Credentiel-Key')
    print(response.headers)
    return response
    

