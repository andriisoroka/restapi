from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
db = SQLAlchemy(app)
CORS(app)
app.config.from_object('config')
api = Api(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(250))

u = User()
print(u.query.all())

from app import views
from app import router