from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
  return render_template('home.html')

@views.route('/collection', methods=['GET', 'POST'])
def myCollection():
  return render_template('collection.html')

@views.route('/comic-details', methods=['GET', 'POST'])
def comicDetails():
  return render_template('comic_details.html')

@views.route('/comics')
def comics():
  return render_template('comics.html')

@views.route('/contact', methods=['GET', 'POST'])
def contact():
  return render_template('contact.html')
