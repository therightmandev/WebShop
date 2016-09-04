from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .config import EMAIL, EMAIL_PASSWORD, DB_PATH

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DB_PATH
db = SQLAlchemy(app)

from .server import app
