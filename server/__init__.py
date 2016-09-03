from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from .config import EMAIL, EMAIL_PASSWORD

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from .server import app
