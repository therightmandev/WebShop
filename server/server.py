from flask import Flask, render_template, request, redirect
from .utils import is_username_available, is_email_available, send_verification_email
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
    #TODO: hash password
    print('new user:', username)
    if username_available and email_available:
        send_verification_email(email)
        db.session.add(User(username, password, email))
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
    #check user info
    #set cookie and stuff if correct
    #return a message if incorrect or w/e
    return "WIP"


#~TEMPORARY!~~~~#
@app.route('/admin/all_books')
def api_all_books():
    return render_template('admin/all_books.html', books=Book.query.all())

if __name__=='__main__':
    app.run()
