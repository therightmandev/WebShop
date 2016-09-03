from flask import Flask, render_template, request, redirect
from .models import Book, User
from . import app, db

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
    book_name = request.args.get('name')
    book_description = request.args.get('description')
    #book_img = request.args.get('image')
    book = Book(book_name, book_description)
    db.session.add(book)
    db.session.commit()
    return redirect('/')

@app.route('/api/signup', methods=['POST'])
def api_signup():
    username = request.args.get('username')
    password = request.args.get('password')
    email = request.args.get('email')
    #check if email and username are available
    print('new user:', username)
    db.session.add(User(username, password, email))
    db.session.commit()
    return "WIP"

@app.route('/api/login', methods=['POST'])
def api_login():
    username = request.args.get('username')
    password = request.args.get('password')
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
