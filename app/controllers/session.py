import datetime

from flask import jsonify, request
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

from app import app

from ..models.user import User, user_schema


def store():
    email = request.json["email"]
    password = request.json["password"]

    user = find_user_by_email(email)
    if not user:
        return jsonify({"message": "User does not exists"}), 401
    print(user.password)
    print(password)
    if not check_password_hash(user.password, password):
        return jsonify({"message": "Invalid password"}), 401

    expires = datetime.timedelta(days=7)
    access_token = create_access_token(identity=user.id, expires_delta=expires)
    result = user_schema.dump(user)
    return jsonify(access_token=access_token, user=result), 200


def find_user_by_email(email):
    try:
        return User.query.filter(User.email == email).one()
    except:
        return None
