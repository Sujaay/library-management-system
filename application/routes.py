from flask import render_template, request, redirect, url_for, session, request, flash, jsonify
from application import app, db
from application.models import *
from flask_login import login_required, current_user, login_user, logout_user, LoginManager
from datetime import datetime, date, timedelta
from sqlalchemy import func


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

        if role == 'user':
            # Create a new user instance and add it to the database
            user = User(name=name, email=email, phone=phone, password=password, address=address, gender=gender, role=role)
            user.date_registered = datetime.now()  # Set the registration date
            db.session.add(user)
        elif role == 'librarian':
            # Create a new librarian instance and add it to the database
            librarian = Librarian(name=name, email=email, password=password)
            db.session.add(librarian)
        else:
            flash('Invalid role selected. Please try again.', 'danger')
            return redirect(url_for('register'))

        db.session.commit()
        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('login'))



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
                user.last_login = datetime.now()  # Set the last_login attribute
                db.session.commit()  # Commit changes to the database
                login_user(user)
                flash('Login successful!', 'success')
                return redirect(url_for('user_dashboard'))
            else:
                flash('Invalid email or password. Please try again.', 'danger')
                return redirect(url_for('login'))

        elif role == 'librarian':
            librarian = Librarian.query.filter_by(email=email).first()
            if librarian and librarian.check_password(password):
                session['librarian_id'] = librarian.id
                librarian.last_login = datetime.now()  # Set the last_login attribute
                db.session.commit()  # Commit changes to the database
                login_user(librarian)
                flash('Login successful!', 'success')
                return redirect(url_for('librarian_dashboard'))
            else:
                flash('Invalid email or password. Please try again.', 'danger')
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


# LIBRARIAN ROUTES

@app.route('/librarian/dashboard')
@login_required
def librarian_dashboard():
    sections = Section.query.all()  # Assuming you have a way to fetch all sections
    current_date = datetime.utcnow()  # Example for current date
    return render_template('librarian/librarian_dashboard.html', sections=sections, current_date=current_date)

@app.route('/edit_section/<int:section_id>', methods=['GET', 'POST'])
def edit_section(section_id):
    # Assume logic for editing a section here
    if request.method == 'POST':
        # Handle form submission to update section details
        # Update the section in the database
        flash('Section updated successfully!', 'success')
        return redirect(url_for('librarian_dashboard'))
    else:
        # Render the edit section form
        return render_template('librarian/section/edit_section.html', section_id=section_id)

# Route for deleting a section
@app.route('/librarian/sections/<int:section_id>/delete', methods=['POST'])
@login_required
def delete_section(section_id):
    section = Section.query.get_or_404(section_id)
    try:
        # Delete the books associated with the section
        Book.query.filter_by(section_id=section.id).delete()

        # Delete the section itself
        db.session.delete(section)
        db.session.commit()
        return jsonify({'message': 'Section deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/librarian/sections/add', methods=['GET', 'POST'])
@login_required
def add_section():
    if request.method == 'GET':
        return render_template('librarian/section/add_section.html')
    elif request.method == 'POST':
        section_name = request.form.get('section_name')
        if section_name:
            new_section = Section(name=section_name)
            db.session.add(new_section)
            db.session.commit()
            return redirect(url_for('librarian_dashboard'))
        else:
            return render_template('librarian/section/add_section.html', error='Section name is required')

@app.route('/librarian/sections/<int:section_id>/books')
@login_required
def list_books_by_section(section_id):
    section = Section.query.get_or_404(section_id)
    books = Book.query.filter_by(section_id=section.id).all()
    return render_template('librarian/section/books.html', section=section, books=books)


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
         
@app.route('/librarian/statistics')
@login_required
def librarian_statistics():
    # Query to get the count of new books added each day for the last week
    books_data = db.session.query(func.date(Book.date_added), func.count(Book.id)).\
        filter(Book.date_added >= (datetime.now() - timedelta(days=7))).\
        group_by(func.date(Book.date_added)).all()
    
    # Extracting labels and data for books chart
    books_labels = [str(entry[0]) for entry in books_data]
    books_count = [entry[1] for entry in books_data]
    
    # Query to get the count of new sections added each day for the last week
    sections_data = db.session.query(func.date(Section.date_added), func.count(Section.id)).\
        filter(Section.date_added >= (datetime.now() - timedelta(days=7))).\
        group_by(func.date(Section.date_added)).all()
    
    # Extracting labels and data for sections chart
    sections_labels = [str(entry[0]) for entry in sections_data]
    sections_count = [entry[1] for entry in sections_data]
    
    # Query to get the count of new users registered today
    new_users_count = User.query.filter(func.date(User.date_registered) == date.today()).count()
    
    # Query to get the count of users logged in today
    users_logged_in_today = User.query.filter(func.date(User.last_login) == date.today()).count()
    
    return render_template('librarian/library_statistics.html', 
                           books_labels=books_labels, 
                           books_data=books_count, 
                           sections_labels=sections_labels, 
                           sections_data=sections_count, 
                           new_users_count=new_users_count, 
                           users_logged_in_today=users_logged_in_today)

from application.models import Section

@app.route('/add_book', methods=['GET'])
@login_required
def add_book_page():
    return render_template('librarian/book/add.html')