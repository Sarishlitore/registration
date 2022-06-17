from datetime import datetime

from sweater import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), nullable=False, unique=True)
    psw = db.Column(db.String(128), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    profile = db.relationship('Profiles', backref='users', uselist=False)

    def __repr__(self):
        return f'<User {self.id}>'


class Profiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<Profile {self.id}>'
