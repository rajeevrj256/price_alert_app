from flask import Blueprint, jsonify
import requests

get_symbols_blueprint = Blueprint('get_symbols', __name__)


symbols_list = []

@get_symbols_blueprint.route('/symbols', methods=['GET'])
def get_symbols():
    
    response = requests.get('https://api.binance.com/api/v3/exchangeInfo')
    data = response.json()
    symbols_list = [symbol['symbol'] for symbol in data['symbols']]
    return jsonify(symbols_list), 200
