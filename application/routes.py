from flask import render_template, request, redirect, url_for, session, request, flash, jsonify, send_from_directory
from application import app, db
from application.models import *
from flask_login import login_required, current_user, login_user, logout_user, LoginManager
from datetime import datetime, date, timedelta
from sqlalchemy import func
import os
from werkzeug.utils import secure_filename
import secrets  # For generating random filenames


def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

    # Define the upload folder
    UPLOAD_FOLDER = 'assets'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


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


# USER DASHBOARD ROUTES

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

# Route for adding a new section
@app.route('/librarian/add_section', methods=['GET', 'POST'])
@login_required
def add_section():
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

    # Define the upload folder
    UPLOAD_FOLDER = 'assets'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    if request.method == 'POST':
        section_name = request.form.get('section_name')
        section_description = request.form.get('section_description')
        # Handle file upload
        if 'section_image' in request.files:
            file = request.files['section_image']
            if file and allowed_file(file.filename):
                import uuid  # Import for generating unique ID

                # Generate unique filename with section name
                extension = os.path.splitext(file.filename)[1]
                unique_id = str(uuid.uuid4())[:8]  # Generate 8 character unique ID
                filename = f"{section_name}_{unique_id}{extension}"
                filename = secure_filename(filename)

                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                # Update section_image with saved filename
                section_image = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        section = Section(name=section_name, description=section_description,  image=section_image)
        db.session.add(section)
        db.session.commit()
        flash('Section added successfully!', 'success')
        return redirect(url_for('librarian_dashboard'))

    return render_template('librarian/section/add_section.html')

# Route for editing a section
@app.route('/edit_section/<int:section_id>', methods=['GET', 'POST'])
def edit_section(section_id):
    section = Section.query.get_or_404(section_id)
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

    # Define the upload folder
    UPLOAD_FOLDER = 'assets'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    if request.method == 'POST':
        section_name = request.form.get('section_name')
        section_description = request.form.get('section_description')  # Get description from form

        # Update only modified attributes
        if section_name:
            section.name = section_name
        if section_description:
            section.description = section_description

        # Handle file upload (optional, modify if needed)
        if 'section_image' in request.files:
            file = request.files['section_image']
            if file and allowed_file(file.filename):
                import uuid

                # Generate unique filename with extension
                extension = os.path.splitext(file.filename)[1]
                unique_id = str(uuid.uuid4())[:8]  # Generate 8 character unique ID
                filename = f"{section_name}_{unique_id}{extension}"
                filename = secure_filename(filename)

                # Delete existing image (if present)
                old_image_path = section.image  

                if old_image_path:  # Check if image exists
                    try:
                        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    except FileNotFoundError:
                        pass  # Ignore if file not found

                # Save uploaded file
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                # Update section image with saved filename (if upload successful)
                section.image = url_for('uploaded_file', filename=filename)

        db.session.commit()
        flash('Section updated successfully!', 'success')
        return redirect(url_for('librarian_dashboard'))

    return render_template('librarian/section/edit_section.html', section=section)


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


# Route for displaying books in a section
@app.route('/librarian/sections/<int:section_id>/books', methods=['GET'])
def display_section_books(section_id):
    section = Section.query.get_or_404(section_id)
    books = section.books
    return render_template('librarian/section/display_section_books.html', section=section, books=books)


# Existing route for rendering the add book form
@app.route('/add_book/<int:section_id>', methods=['GET', 'POST'])
def add_book(section_id):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

    # Define the upload folder
    UPLOAD_FOLDER = 'assets'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    
    if request.method == 'POST':
        # Get form data
        title = request.form['title']
        author = request.form['author']
        isbn = request.form['isbn']

        # Handle file uploads (improved logic with unique filenames)
        book_image = request.files['book_image']
        pdf_file = request.files['pdf_file']

        if book_image and allowed_file(book_image.filename):
            import uuid

            # Generate unique filename with extension
            extension = os.path.splitext(book_image.filename)[1]
            unique_id = str(uuid.uuid4())[:8]  # Generate 8 character unique ID
            filename = f"book_image_{unique_id}{extension}"
            filename = secure_filename(filename)

            # Configure book image path (assuming UPLOAD_FOLDER is set)
            book_image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'books', 'images', filename)
            book_image.save(book_image_path)
        else:
            book_image_path = None  # Set to None if image upload fails

        if pdf_file and allowed_file(pdf_file.filename):
            # Generate unique filename with extension
            extension = os.path.splitext(pdf_file.filename)[1]
            unique_id = str(uuid.uuid4())[:8]  # Generate 8 character unique ID
            filename = f"book_pdf_{unique_id}{extension}"
            filename = secure_filename(filename)

            # Configure PDF path (assuming UPLOAD_FOLDER is set)
            pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], 'books', 'pdfs', filename)
            pdf_file.save(pdf_path)
        else:
            pdf_path = None  # Set to None if PDF upload fails

        book = Book(title=title, author=author, isbn=isbn, section_id=section_id, image=book_image_path, pdf_link=pdf_path)
        db.session.add(book)
        db.session.commit()

        flash('Book added successfully!', 'success')
        return redirect(url_for('display_section_books', section_id=section_id))

    else:
        return render_template('librarian/book/add_book.html', section_id=section_id)

# Route to delete a book
@app.route('/delete_book/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return 'Book deleted successfully'


@app.route('/librarian/statistics')
@login_required
def librarian_statistics():
    books_data = db.session.query(func.date(Book.date_added), func.count(Book.id)).\
        filter(Book.date_added >= (datetime.now() - timedelta(days=7))).\
        group_by(func.date(Book.date_added)).all()
    
    books_labels = [str(entry[0]) for entry in books_data]
    books_count = [entry[1] for entry in books_data]
    
    sections_data = db.session.query(func.date(Section.date_added), func.count(Section.id)).\
        filter(Section.date_added >= (datetime.now() - timedelta(days=7))).\
        group_by(func.date(Section.date_added)).all()
    
    sections_labels = [str(entry[0]) for entry in sections_data]
    sections_count = [entry[1] for entry in sections_data]
    
    new_users_count = User.query.filter(func.date(User.date_registered) == date.today()).count()
    users_logged_in_today = User.query.filter(func.date(User.last_login) == date.today()).count()  
    return render_template('librarian/library_statistics.html', 
                           books_labels=books_labels, 
                           books_data=books_count, 
                           sections_labels=sections_labels, 
                           sections_data=sections_count, 
                           new_users_count=new_users_count, 
                           users_logged_in_today=users_logged_in_today)
