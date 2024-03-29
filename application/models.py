import bcrypt
from application.database import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(15), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(255), nullable=True)
    role = db.Column(db.String(20), nullable=False, default="customer")

    def __init__(self, name, email, phone, password, address=None, role='customer'):
        self.name = name
        self.email = email
        self.phone = phone
        self.set_password(password)
        self.address = address
        self.role = role
    
    def set_password(self, password):
        # Hash the password using bcrypt
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self, password):
        # Check if the provided password matches the stored hash
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

    def __repr__(self):
        return f'<User {self.name}>'
