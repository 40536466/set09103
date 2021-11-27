from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from .models import Comic

views = Blueprint('views', __name__)





# HOMEPAGE
@views.route('/')
def home():
  featuredComics = Comic.query.filter_by(featured='yes').all()

  return render_template('home.html',
    user=current_user,
    featuredComics=featuredComics)





# COLLECTION PAGE
@views.route('/collection', methods=['GET', 'POST'])
@login_required
def myCollection():

  return render_template('collection.html',
    user=current_user)





#COMIC DETAILS PAGE
@views.route('/comic-details', methods=['GET', 'POST'])
def comicDetails():

  return render_template('comic_details.html',
    user=current_user)





# COMICS PAGE
@views.route('/comics', methods=['GET', 'POST'])
def comics():
  # Default variables
  searchTerm = ''
  category = ''
  comics = Comic.query.all()



  # if method = post
  # searchTerm = value from search bar

  # if get author's name exists
  # searchTerm = author's name -> convert underscores to spaces

  # if get category exists
  # category = category -> convert underscores to spaces


  # If search term != '', fetch only relevant comics
    # set comics = query.filter(title like searchterm or author like searchterm)

  # If category != '', fetch only comics from that category
    # set comics = query.filter(category = category)
  

  # Sample code for comics query
  # comics = Comic.query.filter(
    # or_(
      # title.like('%' + searchTerm + '%'),
      # author.like('%' + searchTerm + '%')
    # )
  # )

  

  return render_template('comics.html',
    user=current_user,
    comics=comics)





# CONTACT PAGE - doesn't actually do anything with form data yet
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
