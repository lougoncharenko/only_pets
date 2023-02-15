from wsgiref.validate import validator
from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from pyparsing import Regex
from wtforms import DateField, StringField, FileField, SubmitField, PasswordField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length
from only_pets.models import *

class UserForm(FlaskForm):
    """Form for adding/updating a User."""
    name = StringField('Name', 
    validators=[
        DataRequired(), 
        Length(min=3, max=80, message="Your name needs to be betweeen 3 and 80 chars")
    ])
    email = StringField('Email', 
    validators=[
        DataRequired(), 
        Length(min=3, max=80, message="Your email needs to be betweeen 3 and 80 chars")
    ])
    username = StringField('Username', 
    validators=[
        DataRequired(), 
        Length(min=3, max=80, message="Your username needs to be betweeen 3 and 80 chars")
    ])
    password = PasswordField('Password', 
    validators=[
        DataRequired(), 
        Length(min=3, max=60, message="Your password needs to be betweeen 3 and 80 chars")
    ])
    submit = SubmitField('Submit')

class AccountForm(FlaskForm):
    """Form for adding/updating an account."""
    username =  StringField('Username', 
    validators=[
        DataRequired(), 
        Length(min=3, max=80, message="Your username needs to be betweeen 3 and 80 chars")
    ])
    biography = TextAreaField("Biography",
    validators=[
    DataRequired(), 
        Length(min=3, max=250, message="Your username needs to be betweeen 3 and 250 chars")
    ])
    photo_url = StringField('Photo',
    validators=[
    DataRequired() 
    ])
    submit = SubmitField('Submit')

class PostForm(FlaskForm):
    """Form for adding/updating a post."""
    date_posted = DateField("Date", format='%Y-%m-%d',
    validators= [
        DataRequired(), 
    ])
    caption = TextAreaField("Biography",
    validators=[
    DataRequired(), 
        Length(min=3, max=250, message="Your username needs to be betweeen 3 and 250 chars")
    ])
    photo_url = StringField('Photo',
    validators=[
    DataRequired() 
    ])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    """Form for adding/updating a comment."""
    comment = TextAreaField("Comment",
    validators=[
    DataRequired(), 
        Length(min=3, max=250, message="Your username needs to be betweeen 3 and 250 chars")
    ])
    submit = SubmitField('Submit')
   