"""Create database models to represent tables."""
from only_pets.extensions import db
from sqlalchemy.orm import backref
from flask_login import UserMixin
from sqlalchemy_utils import URLType

##########################################
#           Models                       #
##########################################

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'<User: {self.username}>'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(250), nullable=False)
    caption = db.Column(db.Text, nullable=False)
    photo_url = db.Column(URLType)
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_by = db.relationship('User')
    all_comments = db.relationship(
        'Comment', secondary="post_comments", back_populates="on_posts")


class Comment(db.Model):
    """Comment model."""
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(250), nullable=False)
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_by = db.relationship('User')
    on_posts = db.relationship(
        'Post', secondary="post_comments", back_populates="all_comments")

    def __str__(self):
        return f'{self.text}'

    def __repr__(self):
        return f'{self.text}'

# Not sure if i did this correctly--- check with Braus
post_comments_table = db.Table('post_comments',
db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True),
db.Column('comment_id', db.Integer, db.ForeignKey('comment.id'), primary_key=True)
)

class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    photo_url = db.Column(URLType)
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_by = db.relationship('User')
   