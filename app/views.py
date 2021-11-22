from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)


# HOMEPAGE
@views.route('/')
def home():
  return render_template('home.html')


# COLLECTION PAGE
@views.route('/collection', methods=['GET', 'POST'])
def myCollection():
  return render_template('collection.html')


#COMIC DETAILS PAGE
@views.route('/comic-details', methods=['GET', 'POST'])
def comicDetails():
  return render_template('comic_details.html')


# COMICS PAGE
@views.route('/comics')
def comics():
  return render_template('comics.html')


# CONTACT PAGE - doesn't actually do anything with form data
@views.route('/contact', methods=['GET', 'POST'])
def contact():
  if request.method == 'POST':
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    success = True
    return render_template('contact.html', success=success)

  return render_template('contact.html')
