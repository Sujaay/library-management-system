from faker import Faker
from application import app, db
from application.models import User, Librarian, Section, Book
import random
import datetime

# Initialize Faker for generating fake data
faker = Faker()

def generate_users(num_users=10):
    for _ in range(num_users):
        user = User(
            name=faker.name(),
            email=faker.email(),
            phone=faker.phone_number(),
            password='password123',  # Set a default password for now
            address=faker.address(),
            gender=random.choice(['Male', 'Female', 'Other'])
        )
        db.session.add(user)
    db.session.commit()

def generate_librarians(num_librarians=5):
    for _ in range(num_librarians):
        librarian = Librarian(
            name=faker.name(),
            email=faker.email(),
            password='password123'  # Set a default password for now
        )
        db.session.add(librarian)
    db.session.commit()

def generate_sections(num_sections=5):
    for _ in range(num_sections):
        section = Section(
            name=faker.word()
        )
        db.session.add(section)
    db.session.commit()

def generate_books(num_books=20):
    sections = Section.query.all()
    authors = ['Author 1', 'Author 2', 'Author 3']  # Add more authors as needed
    for _ in range(num_books):
        book = Book(
            title=faker.sentence(),
            author=random.choice(authors),
            isbn=faker.isbn13(),
            section=random.choice(sections)
        )
        db.session.add(book)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        # Call the data generation functions
        generate_users()
        generate_librarians()
        generate_sections()
        generate_books()

    print('Random data generation completed.')
