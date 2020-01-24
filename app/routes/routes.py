from flask import jsonify
from flask_jwt_extended import jwt_required

from app import app

from ..controllers import contact, message, user, session


# users
@app.route("/users", methods=["POST"])
def create_user():
    return user.store()


@app.route("/users/<id>", methods=["PUT"])
@jwt_required
def update_user(id):
    return user.update(id)


# sessions
@app.route("/sessions", methods=["POST"])
def create_session():
    return session.store()


# contacts
@app.route("/contacts/<id>", methods=["GET"])
def list_contacts(id):
    return contact.index(id)


@app.route("/contacts/<id>", methods=["POST"])
def create_contact(id):
    return contact.store(id)


@app.route("/contacts/<id>", methods=["DELETE"])
def delete_user(id):
    return contact.destroy(id)


# messages
@app.route("/messages/<id>", methods=["GET"])
def list_messages(id):
    return message.index(id)


@app.route("/messages/<id>", methods=["POST"])
def create_message(id):
    return message.store(id)
