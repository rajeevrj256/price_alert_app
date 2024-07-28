from flask import Blueprint, request, jsonify, render_template
from flask_jwt_extended import jwt_required, get_jwt_identity
from utils.db import db
from bson.objectid import ObjectId
from utils.websocket_client import start_websocket_client

create_alert_blueprint = Blueprint('create_alert', __name__)

alerts_collection = db['alerts']

client=start_websocket_client()


@create_alert_blueprint.route('/create', methods=['POST'])
#@jwt_required()
def create_alert():
    print("here")
    #current_user = get_jwt_identity()
    data = request.json
    symbol = data.get('symbol')
    alert_price = data.get('alert_price')
    

    if not symbol or not alert_price :
        return jsonify({'error': 'Missing required fields'}), 400

    alert = {
        #'user_id': current_user,
        'symbol': symbol,
        'alert_price': alert_price,
        'status': 'created'
    }

    result = alerts_collection.insert_one(alert)
    client.subscribe(symbol)
    return jsonify({'_id': str(result.inserted_id)}), 201

