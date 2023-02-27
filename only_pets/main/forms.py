from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, SelectField, SubmitField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired, Length, ValidationError
from only_pets.models import *


class UserForm(FlaskForm):
    """Form for adding/updating a post."""
    username = TextAreaField("Username",
    validators=[
    DataRequired(), 
        Length(min=3, max=250, message="Your title needs to be betweeen 3 and 250 chars")
    ])
    password = PasswordField("Password",
    validators=[
    DataRequired(), 
        Length(min=3, max=250, message="Your caption needs to be betweeen 3 and 250 chars")
    ])
    submit = SubmitField('Submit')

class PostForm(FlaskForm):
    """Form for adding/updating a post."""
    title = TextAreaField("Title",
    validators=[
    DataRequired(), 
        Length(min=3, max=250, message="Your title needs to be betweeen 3 and 250 chars")
    ])
    caption = TextAreaField("Caption",
    validators=[
    DataRequired(), 
        Length(min=3, max=250, message="Your caption needs to be betweeen 3 and 250 chars")
    ])
    photo_url = StringField('Photo Url',
    validators=[
    DataRequired() 
    ])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    """Form for adding/updating a comment."""
    text = TextAreaField("Comment",
    validators=[
    DataRequired(), 
        Length(min=3, max=250, message="Your comment needs to be betweeen 3 and 250 chars")
    ])
    submit = SubmitField('Submit')


class StoryForm(FlaskForm):
    """Form for adding/updating a post."""
    photo_url = StringField('Photo Url',
    validators=[
    DataRequired() 
    ])
    submit = SubmitField('Submit')