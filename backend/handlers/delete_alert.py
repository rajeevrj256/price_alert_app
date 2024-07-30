from flask import Blueprint, jsonify
from utils.db import db
from bson import ObjectId
delete_alert_blueprint = Blueprint('delete_alert', __name__)

# Define the alerts collection
alerts_collection = db['alerts']
@delete_alert_blueprint.route('/alerts/<alter_id>', methods=['DELETE'])
def delete_alert(alert_id):
    try:
        # Convert alert_id to ObjectId if necessary
        alert_id = alert_id
    except Exception as e:
        return jsonify({'error': 'Invalid alert ID'}), 400

    result = alerts_collection.delete_one({'_id': alert_id})

    if result.deleted_count == 0:
        return jsonify({'error': 'Alert not found'}), 404

    return jsonify({'message': 'Alert deleted successfully'}), 200
