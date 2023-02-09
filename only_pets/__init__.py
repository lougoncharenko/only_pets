from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from only_pets.config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = os.urandom(24)

db = SQLAlchemy(app)

from only_pets.main.routes import main

app.register_blueprint(main)

with app.app_context():
    db.create_all()
