from flask import Flask, render_template, request, redirect
from .models import Book
from . import app, db

@app.route('/')
def index():
    return render_template('index.html', name = 'Shopper')

@app.route('/submit')
def submit():
    return render_template('submit.html')

#API
@app.route('/api/submit')
def api_submit():
    book_name = request.args.get('name')
    book_description = request.args.get('description')
    #book_img = request.args.get('image')
    print('new book:\n' + book_name + '\n' + book_description)
    book = Book(book_name, book_description)
    db.session.add(book)
    db.session.commit()
    return redirect('/')


#~TEMPORARY!~~~~#
@app.route('/api/all_books')
def api_all_books():
    res = ""
    for b in Book.query.all():
        res += b.title
    return res

if __name__=='__main__':
    app.run()
