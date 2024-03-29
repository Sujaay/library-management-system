from flask import render_template, request, redirect, url_for, session
from application import app, db
from application.models import User
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
    return render_template('index.html')

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
        role = 'customer'
        user = User(name=name, email=email, phone=phone, password=password, address=address, role=role)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            session['user_id'] = user.id  # Store user ID in session upon successful login
            login_user(user)  # Login the user
            print("Login Successful and logged in user", user)
            return redirect(url_for('user_dashboard'))
        else:
            print("Wrong password or email")
            return render_template('login.html')

        
@app.route('/logout')
@login_required
def logout():
    logout_user()  # Log out the user
    session.clear()  # Clear the session
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

# New routes for My Books, Account Settings, and Browse Sections

@app.route('/my_books')
@login_required
def my_books():
    # Add logic here to fetch user's books
    return render_template('my_books.html')

@app.route('/account_settings')
@login_required
def account_settings():
    # Add logic here to fetch user's account settings
    return render_template('account_settings.html')

@app.route('/browse_sections')
@login_required
def browse_sections():
    # Add logic here to browse different sections of the library
    return render_template('browse_sections.html')