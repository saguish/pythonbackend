from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({"message": "Bem-vindo à API Flask com JWT e PostgreSQL!"})

@main.route('/private', methods=['GET'])
@jwt_required()
def private():
    current_user_id = get_jwt_identity()
    return jsonify({"message": f"Acesso autorizado! Seu ID: {current_user_id}"}), 200
