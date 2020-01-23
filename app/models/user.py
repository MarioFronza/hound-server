import datetime
from app import db, ma

user_contact = db.Table(
    "user_contact",
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
    db.Column("contact_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
    db.Column("created_at", db.DateTime, default=datetime.datetime.now()),
)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    contacts = db.relationship(
        "User",
        secondary=user_contact,
        primaryjoin=id == user_contact.c.user_id,
        secondaryjoin=id == user_contact.c.contact_id,
    )
    messages = db.relationship("Message", backref="users", lazy=True)
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
            "name",
            "email",
            "created_at",
        )


user_schema = UserSchema()
users_schema = UserSchema(many=True)
