from . import db
from flask_login import UserMixin

# Users schema
class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True)
  password = db.Column(db.String(20))
  collection = db.Column(db.String(5000))

# Comics schema
class Comic(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(60))
  author = db.Column(db.String(40))
  category = db.Column(db.String(20))
  summary = db.Column(db.String(1000))
  additionalInfo = db.Column(db.String(1000))
  coverImage = db.Column(db.String(60))
  featured = db.Column(db.String(5))
  