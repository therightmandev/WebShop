from flask import Flask, render_template, request, redirect

app = Flask(__name__)

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
    book_img = request.args.get('image')
    print('new book:\n' + book_name + '\n' + book_description)
    #add book to the database
    return redirect('/')

if __name__=='__main__':
    app.run()
