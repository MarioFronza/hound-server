import datetime

from app import db, ma


class Message(db.Model):
    __tablename__ = "messages"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    content = db.Column(db.Text, nullable=False)
    send = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, user_id, send, content):
        self.user_id = user_id
        self.send = send
        self.content = content


class MessageSchema(ma.Schema):
    class Meta:
        fields = ("id", "user_id", "send", "content")


message_schema = MessageSchema()
messages_schema = MessageSchema(many=True)
