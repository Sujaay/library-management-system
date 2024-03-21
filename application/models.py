from application.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(10), nullable=False, unique=True)
    phone = db.Column(db.String(10), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(100), nullable=True)
    role = db.Column(db.String(10), nullable=False, default="customer")

    def __init__(self, name, email, phone, password, address, role):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        self.address = address
        self.role = role
    
    def __repr__(self):
        return '<User %r>' % self.name
    