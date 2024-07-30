from flask import Blueprint, jsonify
from utils.db import db

get_alerts_blueprint = Blueprint('get_alerts', __name__)

# Define the alerts collection
alerts_collection = db['alerts']

@get_alerts_blueprint.route('/api/alerts', methods=['GET'])
def get_alerts():
    try:
        # Fetch alerts from the MongoDB collection
        alerts = alerts_collection.find()
        alerts_list = [{**alert, '_id': str(alert['_id'])} for alert in alerts]
        return jsonify(alerts_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
