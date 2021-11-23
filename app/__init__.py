from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'afdgvbmdljadnsefnsdvdndhrtjhh'
  app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
  app.config["SQLAlCHEMY_TRACK_MODIFICATIONS"] = False  # Handling Warnings
  db.init_app(app)

  from .views import views
  from .auth import auth
  from .models import User, Comic

  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/')

  create_database(app)

  return app


def create_database(app):
  if not path.exists('app/' + DB_NAME):
    db.create_all(app=app)
    print('Created database!')