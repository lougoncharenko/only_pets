"""Create database models to represent tables."""
from only_pets import db
from sqlalchemy.orm import backref
from flask_login import UserMixin
from sqlalchemy_utils import URLType
from datetime import datetime


##########################################
#           Models                      #
##########################################

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    posts = db.relationship('Posts', backref='author', lazy=True)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    # users_account = db.relationship('Account', secondary='user_account', 
    # back_populates='users')

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

class Account(UserMixin, db.Model):
    """Account model."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    biography = db.Column(db.String(250), nullable=False)
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_by = db.relationship('User')
#     users= db.relationship('User', secondary='user_account', 
#     back_populates='users_account')

# user_account = db.Table('user_account',
# db.column('user_id', db.Integer, db.ForeignKey('user_id')),
# db.column('account_id', db.Integer, db.ForeignKey('account_id'))
# )

# class Post(db.Model):
#     """Post model."""
#     id = db.Column(db.Integer, primary_key=True)
#     photo_url = db.Column(URLType)
#     caption = db.Column(db.String(250), nullable=False)
#     created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     created_by = db.relationship('User')
#     def __str__(self):
#         return f'{self.caption}'

#     def __repr__(self):
#         return f'{self.caption}'


# class Comment(db.Model):
#     """Comment model."""
#     id = db.Column(db.Integer, primary_key=True)
#     text = db.Column(db.String(250), nullable=False)
#     created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     created_by = db.relationship('User')
#     def __str__(self):
#         return f'{self.text}'

#     def __repr__(self):
#         return f'{self.text}'
