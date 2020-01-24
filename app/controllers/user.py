from flask import jsonify, request
from werkzeug.security import generate_password_hash

from app import db

from ..models.user import User, user_schema, users_schema


def store():
    name = request.json["name"]
    email = request.json["email"]
    password = request.json["password"]

    user = find_user_by_email(email)
    if user:
        return jsonify({"message": "User already exists"}), 400

    password_hash = generate_password_hash(password)
    user = User(name, email, password_hash)

    try:
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify(result), 201
    except:
        return jsonify({"message": "Unable to create"}), 500


def update(id):
    name = request.json["name"]
    email = request.json["email"]
    password = request.json["password"]

    user = find_user_by_id(id)
    if not user:
        return jsonify({"message": "User does not exists"}), 400

    password_hash = generate_password_hash(password)

    try:
        user.name = name
        user.email = email
        user.password = password_hash
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify(result), 200
    except:
        return jsonify({"message": "Unable to update"}), 500


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
