from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
  return render_template('home.html')

@views.route('/collection')
def myCollection():
  return render_template('collection.html')

@views.route('/comic-details')
def comicDetails():
  return render_template('comic_details.html')

@views.route('/comics')
def comics():
  return render_template('comics.html')

@views.route('/contact')
def contact():
  return render_template('contact.html')
