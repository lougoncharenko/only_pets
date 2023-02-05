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


# class GroceryStoreForm(FlaskForm):
#     """Form for adding/updating a GroceryStore."""
#     title = StringField('Grocery Store Name', 
#     validators=[
#         DataRequired(), 
#         Length(min=3, max=80, message="Your title needs to be betweeen 3 and 80 chars")
#     ])
#     address = StringField('Address', 
#     validators=[
#         DataRequired(), 
#         Length(min=3, max=80, message="Your address needs to be betweeen 3 and 80 chars")
#     ])
#     submit = SubmitField('Submit')

# class GroceryItemForm(FlaskForm):
#     """Form for adding/updating a GroceryItem."""
#     name = StringField('Grocery Item', 
#     validators=[
#         DataRequired(), 
#         Length(min=3, max=80, message="Your Grocery item needs to be betweeen 3 and 80 chars")
#     ])
#     price = FloatField ("Price    ",
#     validators=[
#         DataRequired()]
#     )
#     category = SelectField('Category',
#     )
#     photo_url = StringField('Photo',
#      validators=[
#         DataRequired() 
#      ]
#     )
#     submit = SubmitField('Submit')
