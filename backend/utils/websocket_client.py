import websocket
import json
from threading import Thread
from utils.db import db

alerts_collection = db['alerts']

def check_alert(price):
    alerts = alerts_collection.find({'alert_price': {'$gte': price}, 'status': 'created'})
    for alert in alerts:
        alerts_collection.update_one({'_id': alert['_id']}, {'$set': {'status': 'triggered'}})
        print(f"Alert triggered for symbol {alert['symbol']} at price {price}")

class BinanceWebSocketClient:
    def __init__(self, symbol, interval, alert_callback):
        self.symbol = symbol
        self.interval = interval
        self.alert_callback = alert_callback
        self.socket = f'wss://stream.binance.com:9443/ws/{self.symbol}@kline_{self.interval}'

    def on_message(self, ws, message):
        data = json.loads(message)
        price = float(data['k']['c'])
        self.alert_callback(price)

    def on_close(self, ws, close_status_code, close_msg):
        print("### closed ###")

    def run(self):
        ws = websocket.WebSocketApp(
            self.socket,
            on_message=self.on_message,
            on_close=self.on_close
        )
        ws.run_forever()

def start_websocket_client():
    client = BinanceWebSocketClient('btcusdt', '1m', check_alert)
    ws_thread = Thread(target=client.run)
    ws_thread.start()
