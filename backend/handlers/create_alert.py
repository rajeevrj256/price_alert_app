from flask import Blueprint, request, jsonify, render_template
from flask_jwt_extended import jwt_required, get_jwt_identity
from utils.db import db
from bson.objectid import ObjectId

create_alert_blueprint = Blueprint('create_alert', __name__)

alerts_collection = db['alerts']

@create_alert_blueprint.route('/alerts/create/', methods=['GET'])
@jwt_required()
def create_alert_form():
    return render_template('index.html')

@create_alert_blueprint.route('/alerts/create/', methods=['POST'])
@jwt_required()
def create_alert():
    current_user = get_jwt_identity()
    data = request.json
    symbol = data.get('symbol')
    alert_price = data.get('alert_price')
    timeframe = data.get('timeframe')

    if not symbol or not alert_price or not timeframe:
        return jsonify({'error': 'Missing required fields'}), 400

    alert = {
        'user_id': current_user,
        'symbol': symbol,
        'alert_price': alert_price,
        'timeframe': timeframe,
        'status': 'created'
    }

    result = alerts_collection.insert_one(alert)
    return jsonify({'_id': str(result.inserted_id)}), 201
