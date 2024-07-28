from flask import Blueprint, request, jsonify, render_template
from utils.auth import bcrypt
from utils.db import db

signup_blueprint = Blueprint('signup', __name__)

users_collection = db['users']

@signup_blueprint.route('/signup', methods=['GET'])
def signup_page():
    return render_template('signup.html')

@signup_blueprint.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Missing required fields'}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    user = {
        'username': username,
        'password': hashed_password
    }

    users_collection.insert_one(user)
    return jsonify({'message': 'User registered successfully'}), 201
