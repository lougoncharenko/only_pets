from sqlalchemy_utils import URLType
from only_pets.extensions import db
from only_pets.utils import FormEnum

##########################################
#           Models                      #
##########################################

class User(db.Model):
    """User model."""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    def __str__(self):
        return f'{self.email}'

    def __repr__(self):
        return f'{self.email}'
    pass

class Account(db.Model):
    """Account model."""
    pass

class Post(db.Model):
    """Post model."""
    pass

class Comment(db.Model):
    """Comment model."""
    pass
