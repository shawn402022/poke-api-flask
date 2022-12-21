from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(200))
    date_created = db.Column(db.DateTime,default=datetime.utcnow)
    character = db.Column(db.String(50))



class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(500))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    owner_id = db.Column(db.Integer,db.ForeignKey('user.id'))