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
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Account(UserMixin, db.Model):
    """Account model."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    biography = db.Column(db.String(250), nullable=False)
    photo_url = db.Column(URLType)
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_by = db.relationship('User')


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    caption = db.Column(db.Text, nullable=False)
    photo_url = db.Column(URLType)
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_by = db.relationship('User')
    all_comments = db.relationship('Comment', secondary="post_comments", back_populates="on_posts")



class Comment(db.Model):
    """Comment model."""
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(250), nullable=False)
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_by = db.relationship('User')
    on_posts = db.relationship('Posts', secondary="post_comments", back_populates="all_comments")
    def __str__(self):
        return f'{self.text}'

    def __repr__(self):
        return f'{self.text}'

# Not sure if i did this correctly--- check with Braus
post_comments_table = db.Table('post_comments',
db.Column('posts_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True),
db.Column('comment_id', db.Integer, db.ForeignKey('comment.id'), primary_key=True)
)