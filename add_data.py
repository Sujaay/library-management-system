from faker import Faker
from application import app, db
from application.models import User, Librarian, Author, Section, Book
import random
from faker.providers import file as file_provider



# Initialize Faker for generating fake data
faker = Faker()
faker.add_provider(file_provider)

def generate_users(num_users=10):
    for _ in range(num_users):
        user = User(
            name=faker.name(),
            email=faker.email(),
            phone=faker.phone_number(),
            password='user',  # Set a default password for now
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
            password='admin'  # Set a default password for now
        )
        db.session.add(librarian)
    db.session.commit()

def generate_authors(num_authors=10):
    for _ in range(num_authors):
        author = Author(
            name=faker.name()
        )
        db.session.add(author)
    db.session.commit()

def generate_sections(num_sections=5):
    for _ in range(num_sections):
        section = Section(
            name=faker.word(),
            image=faker.image_url()
        )
        db.session.add(section)
    db.session.commit()

def generate_books(num_books=20):
    authors = Author.query.all()
    sections = Section.query.all()
    for _ in range(num_books):
        section_id = random.choice(sections).id  # Get the ID of a random section
        book = Book(
            title=faker.sentence(),
            author=random.choice(authors).name,
            isbn=faker.isbn13(),
            section_id=section_id,  # Pass the section ID instead of the section object
            date_added=faker.date_time_this_year(),
            image=faker.image_url(),
            pdf_link=faker.file_path(extension='pdf')
        )
        db.session.add(book)
    db.session.commit()




if __name__ == '__main__':
    with app.app_context():
        # Call the data generation functions
        generate_users()
        generate_librarians()
        generate_authors()
        generate_sections()
        generate_books()

    print('Random data generation completed.')
