from flask import jsonify
from flask_jwt_extended import jwt_required

from app import app

from ..controllers import contact, message, user, session


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
def list_contacts():
    return contact.index()


@app.route("/contacts", methods=["POST"])
def create_contact():
    return contact.store()


@app.route("/contacts/<id>", methods=["DELETE"])
def delete_user(id):
    return contact.destroy(id)


# messages
@app.route("/messages", methods=["GET"])
def list_messages():
    return message.index()


@app.route("/messages", methods=["POST"])
def create_message():
    return message.store()
