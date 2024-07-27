from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from utils.db import db
from bson.objectid import ObjectId

delete_alert_blueprint = Blueprint('delete_alert', __name__)

alerts_collection = db['alerts']

@delete_alert_blueprint.route('/alerts/delete/<alert_id>/', methods=['DELETE'])
@jwt_required()
def delete_alert(alert_id):
    current_user = get_jwt_identity()
    result = alerts_collection.delete_one({'_id': ObjectId(alert_id), 'user_id': current_user})

    if result.deleted_count == 0:
        return jsonify({'error': 'Alert not found'}), 404

    return jsonify({'message': 'Alert deleted successfully'}), 200
