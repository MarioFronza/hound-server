import datetime
from app import db, ma

contacts = db.Table(
    "contacts",
    db.Model.metadata,
    db.Column("user_id", db.Inteher, db.ForeignKey("user.id")),
    db.Column("contact_id", db.Inteher, db.ForeignKey("user.id")),
)


class User(db.Model):
    __tablename__ == "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    contacts = db.relationship("User", secondary=contacts)
    messages = db.relationship("Message", backref="user", fazy=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, username, name, email, password):
        self.username = username
        self.password = password
        self.name = name
        self.email = email


class UserSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "username",
            "name",
            "email",
            "password",
            "contacts",
            "created_at",
        )


user_schema = UserSchema()
users_schema = UserSchema(many=True)
