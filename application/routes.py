from application import app
from application.models import User
from flask import render_template, request, redirect, url_for
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
            print("Login Sucessful and logged in user", user)
            return redirect(url_for('index'))
        else:
            print("Wrong password or email")
            return render_template('login.html')