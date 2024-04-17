from application.database import db
from flask_login import UserMixin
from sqlalchemy import ForeignKey, Column, Integer, String, Text, DateTime, Float, Table
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
import bcrypt

user_allocated_books_association = Table('user_allocated_books', db.Model.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('book_id', Integer, ForeignKey('book.id')),
    Column('allocation_date', DateTime, nullable=False, default=db.func.current_timestamp()),
    Column('return_date', DateTime, nullable=True),
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(15), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(255), nullable=True)
    gender = db.Column(db.String(10), nullable=True)
    role = db.Column(db.String(20), nullable=False, default="user")
    date_registered = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    last_login = db.Column(db.DateTime, nullable=True)

    requests = relationship('Request', back_populates='user')
    feedbacks = relationship('Feedback', back_populates='user')
    allocated_books = relationship('Book', secondary=user_allocated_books_association, back_populates='users')


    def __init__(self, name, email, phone, password, address=None, gender=None, role='user'):
        self.name = name
        self.email = email
        self.phone = phone
        self.set_password(password)
        self.address = address
        self.gender = gender
        self.role = role
    
    def set_password(self, password):
        # Hash the password using bcrypt
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self, password):
        # Check if the provided password matches the stored hash
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

    def update_address(self, new_address):
        # Update user's address
        self.address = new_address
        db.session.commit()

    def update_phone(self, new_phone):
        # Update user's phone number
        self.phone = new_phone
        db.session.commit()

    def update_password(self, new_password):
        # Update user's password
        self.set_password(new_password)
        db.session.commit()

    def __repr__(self):
        return f'<User {self.name}>'

class Librarian(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    date_registered = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    last_login = db.Column(db.DateTime, nullable=True)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.set_password(password)

    def set_password(self, password):
        # Hash the password using bcrypt
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        # Check if the provided password matches the stored hash
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

    def __repr__(self):
        return f'<Librarian {self.name}>'

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(20), nullable=False, unique=True)
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    image = db.Column(db.String(255), nullable=True)  # Image URL or file path
    pdf_link = db.Column(db.String(255), nullable=True)  # PDF link for the book
    price = db.Column(db.Float, nullable=True)  # Price of the e-book

    section = db.relationship('Section', back_populates='books')
    requests = db.relationship('Request', back_populates='book')
    users = db.relationship('User', secondary=user_allocated_books_association, backref='books', overlaps="allocated_books")  # Many-to-Many relationship with User model
    feedbacks = db.relationship('Feedback', back_populates='book')  # Relationship with Feedback model

    @property
    def rating(self):
        feedback_ratings = [feedback.rating for feedback in self.feedbacks]
        if feedback_ratings:
            return sum(feedback_ratings) / len(feedback_ratings)
        else:
            return None

    def __repr__(self):
        return f'<Book {self.title}>'

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f'<Author {self.name}>'

class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    image = db.Column(db.String(255), nullable=True)  # Image URL or file path
    date_added = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    books = relationship('Book', back_populates='section')
    
    def __repr__(self):
        return f'<Section {self.name}>'

    @property
    def book_count(self):
        # Calculate the number of books associated with the section
        return len(self.books)

class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    request_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    return_date = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(20), nullable=False, default='requested')  # Request status: requested, approved, returned
    requested_duration = db.Column(db.Integer, nullable=False)  # Duration in days for which the book is requested

    user = relationship('User', back_populates='requests')
    book = relationship('Book', back_populates='requests')

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # Rating of the book (1 to 5)
    date_added = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    user = relationship('User', back_populates='feedbacks')
    book = relationship('Book', back_populates='feedbacks')

    def __repr__(self):
        return f'<Feedback {self.id}>'
