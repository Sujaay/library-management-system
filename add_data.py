from application import db, app
from application.models import User, Librarian, Book, Author, Section, Request, Feedback
from faker import Faker
import random
from datetime import datetime, timedelta
import bcrypt

# Initialize Faker
fake = Faker()

# Generate users
def generate_users(num_users=30):
    for _ in range(num_users):
        user = User(
            name=fake.name(),
            email=fake.email(),
            phone=fake.phone_number(),
            password='user',
            address=fake.address(),
            gender=random.choice(['Male', 'Female', 'Other']),
        )
        db.session.add(user)
    db.session.commit()

# Generate librarians
def generate_librarians(num_librarians=1):
    for _ in range(num_librarians):
        librarian = Librarian(
            name=fake.name(),
            email="admin@gmail.com",
            password='admin'
        )
        db.session.add(librarian)
    db.session.commit()

# Generate authors
def generate_authors(num_authors=50):
    for _ in range(num_authors):
        author = Author(
            name=fake.name()
        )
        db.session.add(author)
    db.session.commit()

# Generate sections
def generate_sections():
    section_names = ['Real Story', 'Reference', 'Periodicals', "Children's Literature", 'Special Collections', 'Sci-Fi', 'History']
    for name in section_names:
        section = Section(
            name=name,
            description=fake.paragraph(),
            image=fake.image_url(),
            date_added=fake.date_time_between(start_date='-1y', end_date='now')
        )
        db.session.add(section)
    db.session.commit()

# Generate books
def generate_books(num_books=200):
    sections = Section.query.all()
    authors = Author.query.all()
    for _ in range(num_books):
        section = random.choice(sections)
        author = random.choice(authors)
        book = Book(
            title=fake.sentence(),
            author=author.name,
            isbn=fake.isbn13(),
            section_id=section.id,
            date_added=fake.date_time_between(start_date=section.date_added, end_date='now'),
            image=fake.image_url(),
            pdf_link=fake.uri(),
            price=random.uniform(0, 50)
        )
        db.session.add(book)
    db.session.commit()

# Generate requests
def generate_requests(num_requests=50):
    users = User.query.all()
    books = Book.query.all()
    for _ in range(num_requests):
        user = random.choice(users)
        book = random.choice(books)
        if not Request.query.filter_by(user_id=user.id, book_id=book.id).first():
            request = Request(
                user_id=user.id,
                book_id=book.id,
                request_date=fake.date_time_between(start_date='-1y', end_date='now'),
                return_date=fake.date_time_between(start_date='now', end_date='+1y'),
                status=random.choice(['requested', 'approved']),
                requested_duration=random.randint(1, 14)  # Random duration in days
            )
            db.session.add(request)
    db.session.commit()

# Generate feedbacks
def generate_feedbacks(num_feedbacks=200):
    users = User.query.all()
    books = Book.query.all()
    for _ in range(num_feedbacks):
        user = random.choice(users)
        book = random.choice(books)
        if not Feedback.query.filter_by(user_id=user.id, book_id=book.id).first():
            feedback = Feedback(
                user_id=user.id,
                book_id=book.id,
                rating=random.randint(1, 5),
                date_added=fake.date_time_between(start_date='-1y', end_date='now')
            )
            db.session.add(feedback)
    db.session.commit()

# Main function to generate data
def generate_data():
    generate_users()
    generate_librarians()
    generate_authors()
    generate_sections()
    generate_books()
    generate_requests()
    generate_feedbacks()

    print("Data generated successfully!")

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        generate_data()
    print('Random data generation completed.')
