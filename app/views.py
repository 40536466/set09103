from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from sqlalchemy import or_
from .models import Comic
from . import db

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
  comics = Comic.query.all()


  # If user clicks 'Delete' button ...
  if request.method == 'POST':
    removeID = str(request.args.get('removeID'))
    current_user.collection = current_user.collection.replace(removeID, '')
    db.session.commit()


  return render_template('collection.html',
    user=current_user,
    comics=comics)





#COMIC DETAILS PAGE
@views.route('/comic-details', methods=['GET', 'POST'])
def comicDetails():

  # If no id passed in URL, redirect to comics page
  if request.args.get('id') == None:
    return redirect(url_for('views.comics'))
  
  # If id exists, get comic from DB
  else:
    comic = Comic.query.filter_by(id=request.args.get('id')).first()


  # Get all available categories from comics in the database
  query = Comic.query.with_entities(Comic.category).distinct().all()
  availableCategories = [item[0] for item in query]


  # Get other comics by same author
  featuredComics = Comic.query.filter_by(author=comic.author).all()


  # If user clicks 'Add to Collection' button ...
  if request.method == 'POST':
    current_user.collection += str(comic.id)
    db.session.commit()


  return render_template('comic_details.html',
    user=current_user,
    comic=comic,
    featuredComics=featuredComics,
    availableCategories=availableCategories)





# COMICS PAGE
@views.route('/comics', methods=['GET', 'POST'])
def comics():
  # Default variables
  searchTerm = ''
  category = ''
  comics = Comic.query.all()

  # Get all available categories from comics in the database
  query = Comic.query.with_entities(Comic.category).distinct().all()
  availableCategories = [item[0] for item in query]
  
  # If a search is submitted ...
  if request.method == 'POST':
    searchTerm = request.form.get('searchTerm')

  # If an author's name has been clicked ...
  if request.args.get('author') != None:
    searchTerm = request.args.get('author').replace('_', ' ')

  # If searchTerm has been set, get related comics from DB
  if searchTerm != '':
    search = "%{}%".format(searchTerm)
    comics = Comic.query.filter(
      or_(
        Comic.title.like(search),
        Comic.author.like(search)
      )
    ).all()


  # If a category has been clicked, get related comics from DB
  if request.args.get('category') != None:
    category = request.args.get('category').replace('_', ' ')
    comics = Comic.query.filter_by(category=category).all()


  return render_template('comics.html',
    user=current_user,
    searchTerm=searchTerm,
    category=category,
    availableCategories=availableCategories,
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
