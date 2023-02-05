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


class Post(db.Model):
    """Post model."""
    pass

class Comment(db.Model):
    """Comment model."""
    pass
