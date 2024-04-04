from flask import render_template, request, redirect, url_for, session, request, flash
from application import app, db
from application.models import *
from flask_login import login_required, current_user, login_user, logout_user, LoginManager

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('login.html')
  
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        address = request.form['address']
        gender = request.form.get('gender')
        role = request.form.get('role')
        user = User(name=name, email=email, phone=phone, password=password, address=address, gender=gender, role=role)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('login'))

from flask import request, redirect, url_for, render_template, flash

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']  # Get the selected role from the form

        if role == 'user':
            user = User.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session['user_id'] = user.id
                login_user(user)
                flash('Login successful!', 'success')
                return redirect(url_for('user_dashboard'))
            else:
                flash('Invalid email or password. Please try again.', 'danger')
                return redirect(url_for('login'))

        elif role == 'librarian':
            # You should implement your own authentication logic for librarians here
            if email == 'admin@gmail.com' and password == 'admin':
                print('Login successful!', 'success')
                return redirect(url_for('librarian_dashboard'))
            else:
                print('Invalid email or password. Please try again.', 'danger')
                return redirect(url_for('login'))

        else:
            flash('Invalid role selected. Please try again.', 'danger')
            return redirect(url_for('login'))

        
@app.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/user_dashboard')
@login_required
def user_dashboard():
    # Ensure user_id is in session before fetching user details
    if current_user.is_authenticated:  # Check if the user is authenticated
        name = current_user.name
        email = current_user.email
        phone = current_user.phone
        address = current_user.address
        return render_template('user_dashboard.html', name=name, email=email, phone=phone, address=address)
    else:
        return redirect(url_for('login'))  # Redirect to login if user is not authenticated


@app.route('/user_profile', methods=['GET', 'POST'])
@login_required
def user_profile():
    # Fetch user details from current_user
    user = current_user
    name = user.name
    email = user.email
    phone = user.phone
    address = user.address
    return render_template('user_profile.html', name=name, email=email, phone=phone, address=address)

@app.route('/user_my_books')
@login_required
def user_my_books():
    user_books = Book.query.filter_by(user_id=current_user.id).all()
    return render_template('user_my_books.html', user_books=user_books)

@app.route('/user_account_settings')
@login_required
def user_account_settings():
    # Add logic here to fetch user's account settings
    return render_template('user_account_settings.html')

@app.route('/update_account_settings', methods=['POST'])
@login_required
def update_account_settings():
    if request.method == 'POST':
        # Get form data
        new_address = request.form.get('new_address')
        new_phone = request.form.get('new_phone')
        new_password = request.form.get('new_password')

        # Update user information if data is provided
        if new_address:
            current_user.update_address(new_address)
        if new_phone:
            current_user.update_phone(new_phone)
        if new_password:
            current_user.update_password(new_password)

        # Redirect to user account settings page or wherever appropriate
        return redirect(url_for('user_account_settings'))

@app.route('/user_browse_sections')
@login_required
def user_browse_sections():
    # Add logic here to browse different sections of the library
    return render_template('user_browse_sections.html')


@app.route('/librarian/dashboard')
@login_required
def librarian_dashboard():
    # Add logic for librarian dashboard here
    return render_template('librarian/dashboard.html')

@app.route('/librarian/sections')
@login_required
def list_sections():
    sections = Section.query.all()
    return render_template('librarian/section/sections.html', sections=sections)

@app.route('/librarian/sections/add', methods=['GET', 'POST'])
@login_required
def add_section():
    if request.method == 'GET':
        return render_template('librarian/section/add_section.html')
    elif request.method == 'POST':
        section_name = request.form.get('section_name')
        if section_name:
            # Create a new Section object
            new_section = Section(name=section_name)
            # Add the new section to the database session
            db.session.add(new_section)
            # Commit the changes to the database
            db.session.commit()
            return redirect(url_for('librarian_dashboard'))
        else:
            # Handle case where section name is not provided
            return render_template('librarian/section/add_section.html', error='Section name is required')

@app.route('/librarian/sections/<int:section_id>/books')
@login_required
def list_books_by_section(section_id):
    section = Section.query.get_or_404(section_id)
    books = Book.query.filter_by(section_id=section.id).all()
    return render_template('librarian/section/books.html', section=section, books=books)

@app.route('/librarian/books/add', methods=['GET', 'POST'])
@login_required
def add_book():
    if request.method == 'GET':
        sections = Section.query.all()
        return render_template('librarian/book/add.html', sections=sections)
    else:
        title = request.form['title']
        author = request.form['author']
        isbn = request.form['isbn']
        section_id = request.form['section_id']
        new_book = Book(title=title, author=author, isbn=isbn, section_id=section_id)
        try:
            db.session.add(new_book)
            db.session.commit()
            flash('Book added successfully!', 'success')
            return redirect(url_for('librarian_dashboard'))
        except Exception as e:
            # Handle database errors gracefully (e.g., duplicate ISBN)
            flash(f'Error adding book: {e}', 'danger')
            return render_template('librarian/book/add.html', sections=Section.query.all())

@app.route('/librarian/books/<int:book_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_book(book_id):
    book = Book.query.get_or_404(book_id)
    sections = Section.query.all()
    if request.method == 'GET':
        return render_template('librarian/book/edit.html', book=book, sections=sections)
    else:
        title = request.form['title']
        author = request.form['author']
        isbn = request.form['isbn']
        section_id = request.form['section_id']
        book.title = title
        book.author = author
        book.isbn = isbn
        book.section_id = section_id
        try:
            db.session.commit()
            flash('Book edited successfully!', 'success')
            return redirect(url_for('list_books_by_section', section_id=book.section_id))
        except Exception as e:
            # Handle database errors gracefully
            flash(f'Error editing book: {e}', 'danger')
            return render_template('librarian/book/edit.html', book=book, sections=sections)

@app.route('/librarian/books/<int:book_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_book(book_id):
     book = Book.query.get_or_404(book_id)
     if request.method == 'GET':
         return render_template('librarian/book/delete.html', book=book)
     else:
         try:
             db.session.delete(book)
             db.session.commit()
             flash('Book deleted successfully!', 'success')
             return redirect(url_for('list_books_by_section', section_id=book.section_id))
         except Exception as e:
             # Handle database errors gracefully (e.g., foreign key constraints)
             flash(f'Error deleting book: {e}', 'danger')
             return redirect(url_for('list_books_by_section', section_id=book.section_id))