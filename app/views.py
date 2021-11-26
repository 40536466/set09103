from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


# HOMEPAGE
@views.route('/')
def home():
  return render_template('home.html', user=current_user)


# COLLECTION PAGE
@views.route('/collection', methods=['GET', 'POST'])
@login_required
def myCollection():
  return render_template('collection.html', user=current_user)


#COMIC DETAILS PAGE
@views.route('/comic-details', methods=['GET', 'POST'])
def comicDetails():
  return render_template('comic_details.html', user=current_user)


# COMICS PAGE
@views.route('/comics')
def comics():
  return render_template('comics.html', user=current_user)


# CONTACT PAGE - doesn't actually do anything with form data
@views.route('/contact', methods=['GET', 'POST'])
def contact():
  if request.method == 'POST':
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    success = True
    return render_template('contact.html',
      success=success,
      user=current_user)

  return render_template('contact.html', user=current_user)
