from flask import jsonify, request, g
from flask_jwt_extended import jwt_required

from app import app, socketio, connectedUsers

from ..controllers import contact, message, session, user


# users
@app.route("/users", methods=["POST"])
def create_user():
    return user.store()


@app.route("/users", methods=["PUT"])
@jwt_required
def update_user():
    return user.update()


# sessions
@app.route("/sessions", methods=["POST"])
def create_session():
    return session.store()


# contacts
@app.route("/contacts", methods=["GET"])
@jwt_required
def list_contacts():
    return contact.index()


@app.route("/contacts", methods=["POST"])
@jwt_required
def create_contact():
    return contact.store()


@app.route("/contacts/<id>", methods=["DELETE"])
@jwt_required
def delete_user(id):
    return contact.destroy(id)


# messages
@app.route("/messages", methods=["GET"])
@jwt_required
def list_messages():
    return message.index()


@app.route("/messages", methods=["POST"])
@jwt_required
def create_message():
    return message.store()


@socketio.on("connect")
def connect():
    id = request.args.get("id")
    socket = request.sid
    connectedUsers[id] = socket

