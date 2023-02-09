from sqlalchemy_utils import URLType
from only_pets.extensions import db
from only_pets.utils import FormEnum

##########################################
#           Models                      #
##########################################

class User(db.Model):
    """User model."""
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), nullable=False)
    biography = db.Column(db.String(80), nullable=False)
    def __str__(self):
        return f'{self.email}'

    def __repr__(self):
        return f'{self.email}'

class Account(db.Model):
    """Account model."""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    posts = db.relationship('Post', back_populates='account')
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_by = db.relationship('User')

class Post(db.Model):
    """Post model."""
    id = db.Column(db.Integer, primary_key=True)
    photo_url = db.Column(URLType)
    caption = db.Column(db.String(250), nullable=False)
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_by = db.relationship('User')
    def __str__(self):
        return f'{self.caption}'

    def __repr__(self):
        return f'{self.caption}'


class Comment(db.Model):
    """Comment model."""
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(250), nullable=False)
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_by = db.relationship('User')
    def __str__(self):
        return f'{self.text}'

    def __repr__(self):
        return f'{self.text}'
