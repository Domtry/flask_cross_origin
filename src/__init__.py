import logging
from flask import Flask, jsonify
from src.user import user_bp

logging.basicConfig(
    filename='app.log', 
    filemode='+a', 
    format='[%(asctime)s]> %(name)s - %(levelname)s - %(message)s')

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(user_bp)
    
    @app.before_request
    def before():
        print("response.headers")
    
    @app.after_request
    def add_header_response(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Content-Type', 'application/json')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Access-Control-Allow-Origin, Api-Credentiel-Key')
        print(response.headers)
        return response
    
    return app