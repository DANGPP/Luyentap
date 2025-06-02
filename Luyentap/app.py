from flask import Flask
from config import Config
from extension import db
from routes.UserRoutes.user_route import user_bp
from routes.AuthRoutes.auth_route import auth_bp
from routes.EventRoutes.event_route import event_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(user_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(event_bp)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
