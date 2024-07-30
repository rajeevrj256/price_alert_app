import websocket
import json
import time
from threading import Thread
from utils.db import db
from utils.mail import send_email

alerts_collection = db['alerts']

def check_alert(prev, curr, symbol):
    try:
        alerts = alerts_collection.find({'symbol': symbol, 'status': 'created'})
        for alert in alerts:
            alertprice=float(alert['alert_price'])
            if prev < alertprice <= curr or prev > alertprice >= curr:
                alerts_collection.update_one({'_id': alert['_id']}, {'$set': {'status': 'triggered'}})
                send_email('rjrajeev5918@gmail.com', 'alert',f"Alert triggered for symbol {alert['symbol']} at price {alert['alert_price']}" )
                print(f"Alert triggered for symbol {alert['symbol']} at price {alert['alert_price']}")
                
    except Exception as e:
        print('Error:', e)


class BinanceWebSocketClient:
    def __init__(self, alert_callback):
        self.isopen=False
        #TODO:handlelock
        self.alert_callback = alert_callback
        self.url = f'wss://stream.binance.com:9443/ws/trade'
        self.symbols=[]
        
        self.prev={}
    
       
    def init(self):    
        self.ws = websocket.WebSocketApp(
            self.url,
            on_message=self.on_message,
            on_close=self.on_close,
            on_open=self.on_open
            
        )
         
    def on_message(self, ws, message):
        data = json.loads(message)
        if "p" in data:
            price = float(data['p'])
            sym=data['s']
            if sym not in self.prev:
                self.prev[sym]=price
            self.alert_callback(self.prev[sym],price,sym)
            self.prev[sym]=price
            
            
        
        

    def on_close(self, ws, close_status_code, close_msg):
        print("### closed ###")
    
    
    def on_open(self,ws):
        self.isopen=True
        
        print("open")
        #self.subscribe(ws,'btcusdt')
        
    def subscribe(self,symbol):
        if self.isopen==False:
            return False
        if symbol in self.symbols:
            return True
        print("Sending subscribe",symbol)
        self.ws.send(json.dumps({"method": "SUBSCRIBE","params":[f"{symbol.lower()}@trade"],"id": 1}))
        self.symbols.append(symbol)
        return True
    
    
    def run(self):
        self.init()
        self.ws.run_forever()  

def start_websocket_client():
    client = BinanceWebSocketClient(check_alert)
    
    
    ws_thread = Thread(target=client.run)
    ws_thread.daemon=True
    ws_thread.start()
    return client
    #while not client.subscribe('btcusdt'):
        #pass
    #while True:
        #pass


if __name__ == "__main__":
    
    start_websocket_client()
    #app.run(debug=True)