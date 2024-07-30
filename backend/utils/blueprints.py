from flask import Flask
from handlers import login,signup,create_alert ,get_alerts,symbol,delete_alert

def register_blueprints(app: Flask):
    
    app.register_blueprint(login.login_blueprint, url_prefix='/')
    app.register_blueprint(signup.signup_blueprint, url_prefix='/')
    app.register_blueprint(create_alert.create_alert_blueprint, url_prefix='/alerts')
    app.register_blueprint(delete_alert.delete_alert_blueprint, url_prefix='/alerts')
    app.register_blueprint(get_alerts.get_alerts_blueprint, url_prefix='/')
    app.register_blueprint(symbol.get_symbols_blueprint, url_prefix='/')
