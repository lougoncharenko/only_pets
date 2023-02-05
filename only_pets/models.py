from sqlalchemy_utils import URLType
from only_pets.extensions import db
from only_pets.utils import FormEnum

##########################################
#           Models                      #
##########################################

class User(db.Model):
    """User model."""
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