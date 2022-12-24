from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(200))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    pokemon = db.relationship('Pokemon', backref='user')

    def hash_my_password(self, password):
        self.password =  generate_password_hash(password)

    def check_my_password(self,password):
        return check_password_hash(self.password, password)



class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(500))
    type = db.Column(db.String(100))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    owner_id = db.Column(db.Integer,db.ForeignKey('user.id'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# def hash_passwords():
    # users =User.query.filter(User.id < 13).all()
    # for user in users:
    #     user.hash_my_password(user.password)
    #     db.session.add(user)

    # db.session.commit()
