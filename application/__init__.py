from flask import Flask
from application.database import db
from application.models import *

app = Flask(__name__, template_folder="../templates", static_folder='../static')
app.config['SECRET_KEY'] = 'aush33rf4r2gflashfaoi'  # Fix typo: 'secert_key' should be 'SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'

db.init_app(app)

# No need to use 'with app.app_context()' for 'db.create_all()' here, as it's not necessary during app creation

# Ensure you have imported all models so that db.create_all() can create tables for them

# For example:
from application.models import User  # Import your User model

with app.app_context():
    db.create_all()
