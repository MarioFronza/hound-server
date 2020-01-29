from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity

from app import connectedUsers, db, socketio

from ..models.message import Message, message_schema, messages_schema
from ..models.user import User


def index():
    id = get_jwt_identity()
    user = find_user_by_id(id)

    if not user:
        return jsonify({"message": "User does not exists"}), 400

    result = messages_schema.dump(user.messages)

    return jsonify(result)


def store():
    id = get_jwt_identity()
    contact_id = request.json["contact_id"]
    send = request.json["send"]
    content = request.json["content"]

    user = find_user_by_id(id)
    contact = find_user_by_id(contact_id)

    if not user:
        return jsonify({"message": "User does not exists"}), 400

    if not contact:
        return jsonify({"message": "Contact does not exists"}), 400

    message = Message(contact_id, send, content)
    received_message = Message(id, False, content)

    try:
        db.session.add(message)
        db.session.add(received_message)
        db.session.commit()
        result = message_schema.dump(message)
        if str(contact.id) in connectedUsers:
            socketio.emit("message", result, room=connectedUsers[str(contact.id)])

        return jsonify(result), 201
    except:
        return jsonify({"message": "Unable to create message"}), 500


def find_user_by_id(id):
    try:
        return User.query.get(id)
    except:
        return None
