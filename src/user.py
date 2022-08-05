from flask import Blueprint, jsonify, request
user_bp = Blueprint("Users", __name__, url_prefix="api/v1/users")

@user_bp.post('/')
def register():
    
    return jsonify({
        "message": "success"
    }), 200