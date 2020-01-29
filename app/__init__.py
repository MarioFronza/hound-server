from flask import Flask
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, emit


app = Flask(__name__)

app.config.from_object("config")

jwt = JWTManager(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)

socketio = SocketIO(app)

connectedUsers = {}


from .controllers import contact, message, user, session
from .models import message, user
from .routes import routes
