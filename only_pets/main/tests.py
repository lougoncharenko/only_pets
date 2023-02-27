
import os
import unittest
import app

from datetime import date
from only_pets.extensions import app, db, bcrypt
from only_pets.models import Post, User

"""
Run these tests with the command:
python -m unittest books_app.main.tests
"""

#################################################
# Setup
#################################################


def login(client, username, password):
    return client.post('/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)

def logout(client):
    return client.get('/logout', follow_redirects=True)

def create_post():
    new_post = Post(
        title= "My cute new kitten",
        caption = "I got a new kitten name Maui for my birthday! Stay tuned for the adventures",
        photo_url = "https://images.unsplash.com/photo-1560114928-40f1f1eb26a0?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8Y3V0ZSUyMGFuaW1hbHxlbnwwfHwwfHw%3D&w=1000&q=80"
    )
    db.session.add(new_post)
    db.session.commit()

def create_user():
    # Creates a user with username 'me1' and password of 'password'
    password_hash = bcrypt.generate_password_hash('password').decode('utf-8')
    user = User(username='me1', password=password_hash)
    db.session.add(user)
    db.session.commit()

#################################################
# Tests
#################################################

class MainTests(unittest.TestCase):
 
    def setUp(self):
        """Executed prior to each test."""
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    def test_homepage_logged_in(self):
        """Test that the posts show up on the homepage."""
        # Set up
        create_post()
        create_user()
        login(self.app, 'me1', 'password')

        # Make a GET request
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        # Check that page contains all of the things we expect
        response_text = response.get_data(as_text=True)
        self.assertIn('To Kill a Mockingbird', response_text)
        self.assertIn('The Bell Jar', response_text)
        self.assertIn('me1', response_text)
        self.assertIn('Create Post', response_text)
        self.assertIn('Create Story', response_text)

        # Check that the page doesn't contain things we don't expect
        # (these should be shown only to logged out users)
        self.assertNotIn('Log In', response_text)
        self.assertNotIn('Sign Up', response_text)

    def test_create_post(self):
        """Test creating a book."""
        # Set up
        create_post()
        create_user()
        login(self.app, 'me1', 'password')

         # Make POST request with data
        post_data = {
            'title': 'The perfect bunny',
            'caption': 'Rascal has been adapting well to his new enviroment',
            'photo_url': "https://www1.pictures.mabelandmoxie.com/mp/dk6E8H4sWN_l.jpg"
        }
        self.app.post('/create_post', data=post_data)