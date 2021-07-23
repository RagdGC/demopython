from flask import Flask
from recursos import api

app = Flask(__name__)
api.init_app(app)

from models import db

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()
