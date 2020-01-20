from app import app
from flask import jsonify
from ..controllers import user, contact

# users
@app.route("/users", methods=["POST"])
def create_user():
    return user.store()


@app.route("/users/<id>", methods=["PUT"])
def update_user(id):
    return user.update(id)


# sessions
@app.route("/sessions", methods=["POST"])
def create_session():
    return jsonify({"message": "Create Session"})


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
    return jsonify({"message": "List Messages"})


@app.route("/messages/<id>", methods=["POST"])
def create_message(id):
    return jsonify({"message": "Create Message"})
