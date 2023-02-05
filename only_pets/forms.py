from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, SelectField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length
from only_pets.models import *

class UserForm(FlaskForm):
    """Form for adding/updating a User."""
    pass

class AccountForm(FlaskForm):
    """Form for adding/updating an account."""
    pass

class PostForm(FlaskForm):
    """Form for adding/updating a post."""
    pass

class CommentForm(FlaskForm):
    """Form for adding/updating a comment."""
    pass

