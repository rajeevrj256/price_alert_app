from flask import Flask
from flask_jwt_extended import JWTManager
from utils.db import db
from utils.blueprints import register_blueprints
from flask_cors import CORS
#from utils.websocket_client import start_websocket_client

#from utils.mail import send_email
import config

app = Flask(__name__)
app.config.from_object(config)
CORS(app)

jwt = JWTManager(app)

# Register blueprints
register_blueprints(app)

if __name__ == "__main__":
    #start_websocket_client()
    #send_email("body")
    app.run(debug=True, host='0.0.0.0')
