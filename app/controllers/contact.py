from flask import jsonify, request

from app import db

from ..models.user import User, user_schema, users_schema


def index(id):
    user = find_user_by_id(id)

    if not user:
        return jsonify({"message": "User does not exists"}), 400

    result = users_schema.dump(user.contacts)

    return jsonify(result)


def store(id):
    email = request.json["email"]

    user = find_user_by_id(id)
    contact = find_user_by_email(email)

    if not user:
        return jsonify({"message": "User does not exists"}), 400

    if not contact:
        return jsonify({"message": "Contact does not exists"}), 400

    try:
        user.contacts.append(contact)
        contact.contacts.append(user)
        db.session.commit()
        result = user_schema.dump(contact)
        return jsonify(result), 201
    except:
        return jsonify({"message": "Unable to add contact"}), 500


def destroy(id):
    email = request.json["email"]

    user = find_user_by_id(id)
    contact = find_user_by_email(email)

    if not user:
        return jsonify({"message": "User does not exists"}), 400

    if not contact:
        return jsonify({"message": "Contact does not exists"}), 400

    try:
        user.contacts.remove(contact)
        db.session.commit()
        return jsonify({}), 204
    except:
        return jsonify({"message": "Unable to remove contact"}), 500


def find_user_by_email(email):
    try:
        return User.query.filter(User.email == email).one()
    except:
        return None


def find_user_by_id(id):
    try:
        return User.query.get(id)
    except:
        return None
