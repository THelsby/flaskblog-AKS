from app import db
from app import login_manager
from flask_login import UserMixin
import datetime

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    posts = db.relationship('Posts', backref='author', lazy=True)

    def __repr__(self):
        return ''.join([
            'User ID:', self.id, '\r\n',
            'Name: ', self.first_name, ' ', self.last_name, '\r\n',
            'Email: ', self.email])

    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False, unique=True)
    content = db.Column(db.String(3000), nullable=False, unique=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow())

    def __repr__(self):
        return ''.join([
            'User ID:', str(self.user_id), '\r\n',
            'Title: ', str(self.title), '\r\n', 'Content: ',self.content])

