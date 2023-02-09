"""Create database models to represent tables."""
from only_pets import db
from sqlalchemy.orm import backref
from flask_login import UserMixin
from sqlalchemy_utils import URLType
from datetime import datetime


##########################################
#           Models                      #
##########################################

class User(UserMixin, db.Model):
    """User model."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)
    # users_account = db.relationship('Account', secondary='user_account', 
    # back_populates='users')

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
