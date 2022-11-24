#models for Message, User and Notifications
from datetime import datetime 
from app import db

class Message(db.Model): 
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    password = db.Column (db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Post (db.Model):
    id = db.Column (db.Integer, primary_key = True)
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)