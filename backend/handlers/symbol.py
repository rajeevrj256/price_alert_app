from flask import Blueprint, jsonify
import requests
import logging


get_symbols_blueprint = Blueprint('get_symbols', __name__)


symbols_list = []

@get_symbols_blueprint.route('/symbols', methods=['GET'])
def get_symbols():
    
    response = requests.get('https://api.binance.com/api/v3/exchangeInfo')
    data = response.json()
    logging.info(f"API Response: {data}")

    if 'symbols' in data:
        symbols_list = [symbol['symbol'] for symbol in data['symbols']]
        return jsonify(symbols_list), 200
    else:
        logging.error("The 'symbols' key is missing from the response.")
        return jsonify({"error": "API response does not contain 'symbols'"}), 500
