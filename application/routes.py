from flask import render_template, request, redirect, url_for, session, flash, jsonify, send_from_directory
from application import app, db
from application.models import *
from flask_login import login_required, current_user, login_user, logout_user, LoginManager
from datetime import datetime, date, timedelta
from sqlalchemy import func
import os
from werkzeug.utils import secure_filename
import secrets
import uuid


# Update the allowed file extensions
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# Define the upload folder
UPLOAD_FOLDER = 'assets'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}
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

        # Check if the email already exists in the database
        existing_user = User.query.filter_by(email=email).first()
        print("Existing user:", existing_user)  # Debugging statement
        if existing_user:
            flash('This email is already registered. Please use a different email.', 'danger')
            return redirect(url_for('register'))

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
                print('Login successful!', 'success')
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


# Core - General User functionalities

@app.route('/request_book/<int:book_id>', methods=['POST'])
@login_required
def request_book(book_id):
    user_id = current_user.id  # Assuming you have a current user object

    # Create a new request entry in the database
    new_request = Request(user_id=user_id, book_id=book_id)
    db.session.add(new_request)
    db.session.commit()

    # Notify the admin about the request (You need to implement notification logic)
    return jsonify({'message': 'Request sent successfully'}), 200

# User dashboard route
@app.route('/user_dashboard')
@login_required
def user_dashboard():
    return render_template('user/user_dashboard.html')

# View sections and books route
@app.route('/view_sections')
@login_required
def view_sections():
    # Fetch all sections from the database
    sections = Section.query.all()
    
    # Render the view_sections template with the sections data
    return render_template('user/view_sections.html', sections=sections)

@app.route('/my_books')
@login_required
def my_books():
    # Get the current user (assuming user authentication is implemented)
    user = current_user  # Assign current_user to a local variable
    # Get the books borrowed or requested by the current user
    user_books = user.books  # Assuming there's a relationship between User and Book models
    
    return render_template('user_books.html', user=user, books=user_books)

@app.route('/view_books/<int:section_id>')
@login_required
def view_books(section_id):
    # Fetch the section based on the provided section_id
    section = Section.query.get(section_id)

    # If the section is not found, redirect to the view_sections page
    if not section:
        return redirect(url_for('view_sections'))

    # Fetch all books associated with the section
    books = section.books

    # Render the view_books template with the section and books data
    return render_template('user/view_books.html', section=section, books=books)
# Request and return books route
@app.route('/request_return_books')
@login_required
def request_return_books():
    # Logic to fetch available and borrowed books
    available_books = Book.query.filter_by(borrowed=False).all()
    borrowed_books = Book.query.filter_by(borrowed=True).all()
    return render_template('user/request_return_books.html', available_books=available_books, borrowed_books=borrowed_books)

# Give feedback route
@app.route('/give_feedback')
@login_required
def give_feedback():
    # Logic to fetch a book for feedback
    book = Book.query.first()  # Example: Fetch the first book for feedback
    return render_template('user/give_feedback.html', book=book)

# Download e-book route
@app.route('/download_ebook/<int:book_id>')
def download_ebook(book_id):
    book = Book.query.get_or_404(book_id)
    # Logic to check if user has access to download the e-book
    if user_has_access_to_download_book():  # You need to implement this logic
        # Logic to initiate download of e-book
        return redirect(book.pdf_link)  # Redirect user to download link
    else:
        flash("You do not have access to download this e-book.", "warning")
        return redirect(url_for('user_dashboard'))

# Helper function to check if user has access to download book
def user_has_access_to_download_book():
    # Add your logic here to check if the user has access to download the e-book
    return True  # Example: Always return True for demonstration purposes

# Add more routes and logic as needed

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
                section.image = url_for('static', filename=filename)

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



# Function to check if file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/add_book/<int:section_id>', methods=['GET', 'POST'])
def add_book(section_id):
    if request.method == 'POST':
        # Get form data
        title = request.form['title']
        author = request.form['author']
        isbn = request.form['isbn']
        price = request.form['price']

        # Handle file uploads (improved logic with unique filenames)
        book_image = request.files['book_image']
        pdf_file = request.files['pdf_file']

        if book_image and allowed_file(book_image.filename):
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

        book = Book(title=title, author=author, isbn=isbn, price=price, section_id=section_id, image=book_image_path, pdf_link=pdf_path)
        db.session.add(book)
        db.session.commit()

        flash('Book added successfully!', 'success')
        return redirect(url_for('display_section_books', section_id=section_id))

    else:
        return render_template('librarian/book/add_book.html', section_id=section_id)

# Route to edit a book

@app.route('/edit_book/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    book = Book.query.get_or_404(book_id)
    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        book.price = request.form['price']
        book.section_id = request.form['section_id']

        # Handle file uploads
        if 'pdf_file' in request.files:
            pdf_file = request.files['pdf_file']
            if pdf_file.filename != '':
                if pdf_file and allowed_file(pdf_file.filename):
                    filename = secure_filename(pdf_file.filename)
                    pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], 'books', 'pdfs', filename)
                    pdf_file.save(pdf_path)
                    book.pdf_link = pdf_path

        if 'image_file' in request.files:
            image_file = request.files['image_file']
            if image_file.filename != '':
                if image_file and allowed_file(image_file.filename):
                    filename = secure_filename(image_file.filename)
                    image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'books', 'images', filename)
                    image_file.save(image_path)
                    book.image = image_path

        db.session.commit()
        flash('Book updated successfully!', 'success')
        return redirect(url_for('display_section_books', section_id=book.section_id))
    return render_template('librarian/book/edit_book.html', book=book, sections=Section.query.all())


# Route to delete a book
@app.route('/delete_book/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return 'Book deleted successfully'


@app.route('/librarian/book_requests')
def book_requests():
    requests = Request.query.all()
    return render_template('librarian/book_requests.html', requests=requests)

@app.route('/librarian/view_requested_book/<int:book_id>')
def view_requested_book(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('librarian/view_requested_book.html', book=book)
@app.route('/accept_request/<int:request_id>', methods=['POST'])
def accept_request(request_id):
    request = Request.query.get(request_id)
    if request and request.status == 'requested':
        request.status = 'accepted'
        db.session.commit()
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'error'})

@app.route('/reject_request/<int:request_id>', methods=['POST'])
def reject_request(request_id):
    request = Request.query.get(request_id)
    if request and request.status == 'requested':
        request.status = 'rejected'
        db.session.commit()
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'error'})

# Route to view requested book details
@app.route('/view_request/<int:request_id>')
def view_request(request_id):
    request = Request.query.get_or_404(request_id)
    return render_template('request_details.html', request=request)



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
