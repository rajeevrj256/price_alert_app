from flask import Blueprint, request, jsonify, render_template,redirect, url_for,make_response
from flask_jwt_extended import create_access_token,jwt_required
from flask_bcrypt import Bcrypt
from bson import ObjectId
from utils.db import db

login_blueprint = Blueprint('login', __name__)
bcrypt = Bcrypt()

users_collection = db['users']

# Serve the login page
@login_blueprint.route('/', methods=['GET'])
def login_page():
    return render_template('login.html')

@login_blueprint.route('/alerts', methods=['GET'])
#@jwt_required()
def create_alert_form():
    return render_template('index.html')

# Handle login requests
@login_blueprint.route('/', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Missing required fields'}), 400

    user = users_collection.find_one({'username': username})
    if user and bcrypt.check_password_hash(user['password'], password):
        access_token = create_access_token(identity=str(user['_id']))
        
        
        return jsonify({'token':f"Bearer {access_token}", 'redirect_url': url_for("login.create_alert_form")})
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

