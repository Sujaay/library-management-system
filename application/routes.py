from application import app
from application.models import User
from flask import render_template, request, redirect, url_for, session
from application.database import db

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
        user = User(name, email, phone, password, address, role)
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
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            session['user_id'] = user.id  # Store user ID in session upon successful login
            print("Login Successful and logged in user", user)
            return redirect(url_for('user_dashboard'))
        else:
            print("Wrong password or email")
            return render_template('login.html')
        
@app.route('/user_dashboard')
def user_dashboard():
    # Ensure user_id is in session before fetching user details
    if 'user_id' in session:
        user_id = session['user_id']
        user = User.query.get(user_id)
        if user:
            name = user.name
            email = user.email
            phone = user.phone
            address = user.address
            return render_template('user_dashboard.html', name=name, email=email, phone=phone, address=address)
    # If user_id is not in session or user does not exist, redirect to login page
    return redirect(url_for('login'))

@app.route('/user_profile', methods=['GET', 'POST'])
def user_profile():
    # Ensure user_id is in session before fetching user details
    if 'user_id' in session:
        user_id = session['user_id']
        user = User.query.get(user_id)
        if user:
            name = user.name
            email = user.email
            phone = user.phone
            address = user.address
            return render_template('user_profile.html', name=name, email=email, phone=phone, address=address)
    # If user_id is not in session or user does not exist, redirect to login page
    return redirect(url_for('login'))