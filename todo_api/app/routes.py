from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__)

@api_bp.route('/todos', methods=['GET'])
def get_todos():
    return jsonify({'message': 'Welcome to the Todo API!'})
