from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from utils.db import db
from flask_paginate import Pagination, get_page_parameter

get_alerts_blueprint = Blueprint('get_alerts', __name__)

alerts_collection = db['alerts']

@get_alerts_blueprint.route('/alerts', methods=['GET'])
@jwt_required()
def get_alerts():
    current_user = get_jwt_identity()
    status_filter = request.args.get('status')
    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 10

    query = {'user_id': current_user}
    if status_filter:
        query['status'] = status_filter

    total = alerts_collection.count_documents(query)
    alerts = alerts_collection.find(query).skip((page - 1) * per_page).limit(per_page)
    alerts = [{**alert, '_id': str(alert['_id'])} for alert in alerts]

    pagination = Pagination(page=page, total=total, per_page=per_page, css_framework='bootstrap4')

    return jsonify({
        'alerts': alerts,
        'pagination': {
            'page': page,
            'total_pages': total // per_page + (1 if total % per_page > 0 else 0),
            'total_alerts': total
        }
    }), 200
