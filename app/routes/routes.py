from app import app
from flask import jsonify

# users
@app.route("/users", methods=["POST"])
def create_user():
    return jsonify({"message": "Create User"})


@app.route("/users", methods=["PUT"])
def update_user():
    return jsonify({"message": "Update User"})


# sessions
@app.route("/sessions", methods=["POST"])
def create_session():
    return jsonify({"message": "Create Session"})


# contacts
@app.route("/contacts", methods=["GET"])
def list_contacts():
    return jsonify({"message": "List Contacts"})


@app.route("/contacts", methods=["POST"])
def create_contact():
    return jsonify({"message": "Create Contact"})


@app.route("/contacts", methods=["DELETE"])
def delete_user():
    return jsonify({"message": "Delete Contact"})


# messages
@app.route("/messages", methods=["GET"])
def list_messages():
    return jsonify({"message": "List Messages"})


@app.route("/messages", methods=["POST"])
def create_message():
    return jsonify({"message": "Create Message"})
