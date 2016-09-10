from flask import Flask, render_template, request, redirect
from .utils import is_username_available, is_email_available, send_verification_email, hash_password, verify_password
from . import app, db
from .models import Book, User

@app.route('/')
def index():
    return render_template('index.html', name = 'Shopper')

@app.route('/submit')
def submit():
    return render_template('submit.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

#API
@app.route('/api/submit', methods=['POST'])
def api_submit():
    book_title = request.form['name']
    book_description = request.form['description']
    #book_img = request.args.get('image')
    print('new book:', book_title)
    book = Book(book_title, book_description)
    db.session.add(book)
    db.session.commit()
    return redirect('/')

@app.route('/api/signup', methods=['POST'])
def api_signup():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    if username is not None and email is not None and password is not None:
        pass
    else:
        return "Please fill all the fields"
    username_available = is_username_available(username)
    email_available = is_email_available(email)
    print('new user:', username)
    if username_available and email_available:
        hashed_password = hash_password(password)
        send_verification_email(email)
        db.session.add(User(username, hashed_password, email))
        db.session.commit()
        return "User registered successfully"
    elif not username_available:
        return "Username not available: " + username
    elif not email_available:
        return "Email already registered: " + email
    elif not email_validated:
        return "That doesn't seem to be a real email address"

@app.route('/api/login', methods=['POST'])
def api_login():
    username = request.form['username']
    password = request.form['password']
    print('logging in:', username)
    user = User.query.filter_by(username=username).first()
    if user:
        is_password_correct = verify_password(password, user.password)
        if is_password_correct:
            return "Logged in!"
        else:
            return "wrong password"
    else:
        return "User not found"
    #TODO:set cookie


#~TEMPORARY!~~~~#
@app.route('/admin/all_books')
def api_all_books():
    return render_template('admin/all_books.html', books=Book.query.all())

if __name__=='__main__':
    app.run()
