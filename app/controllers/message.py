from app import db
from flask import request, jsonify
from ..models.message import Message, messages_schema, message_schema
from ..models.user import User


def index(id):
    user = find_user_by_id(id)

    if not user:
        return jsonify({"message": "User does not exists"}), 400

    result = messages_schema.dump(user.messages)

    return jsonify(result)


def store(id):
    user_id = request.json["user_id"]
    send = request.json["send"]
    content = request.json["content"]

    user = find_user_by_id(id)
    contact = find_user_by_id(user_id)

    if not user:
        return jsonify({"message": "User does not exists"}), 400

    if not contact:
        return jsonify({"message": "Contact does not exists"}), 400

    message = Message(user_id, send, content)
    received_message = Message(id, False, content)

    try:
        db.session.add(message)
        db.session.add(received_message)
        db.session.commit()
        result = message_schema.dump(message)
        return jsonify(result), 201
    except:
        return jsonify({"message": "Unable to create message"}), 500


def find_user_by_id(id):
    try:
        return User.query.get(id)
    except:
        return None
