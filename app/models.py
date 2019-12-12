from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db
from flask_login import UserMixin
from app import login

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Posts', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return '<User {}>'.format(self.username)

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key = True)        
    body = db.Column(db.String(1000))
    timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 

    def __repr__(self):
        return f"<Posts {self.body}>"

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True, unique = True)
    name = db.Column(db.String(50), index = True)
    email = db.Column(db.String(100),index = True, unique = True)
    message = db.Column(db.String(500))

    def __repr__(self):
        return f"<Contact {Contact.email}>"