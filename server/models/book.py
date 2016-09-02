from .. import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True)
    description = db.Column(db.String, unique=True)

    def __init__(self, title, description):
        self.title = title 
        self.description = description

    def __repr__(self):
        return '<Book %r>' % self.title
