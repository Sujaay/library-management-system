from flask import Flask
from application.database import db
from application.models import User
from flask_login import LoginManager


app = Flask(__name__, template_folder="../templates", static_folder='../static')
app.config['SECRET_KEY'] = 'aush33rf4r2gflashfaoi' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'

db.init_app(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)  # Register login_manager with the app

# Define the user loader function
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()
