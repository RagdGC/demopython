from flask import Flask
# from werkzeug.contrib.fixers import ProxyFix
from recursos import api

app = Flask(__name__)

# app.wsgi_app = ProxyFix(app.wsgi_app)
api.init_app(app)

from models import db

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()
