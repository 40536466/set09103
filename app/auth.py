from flask import Blueprint, render_template, request, redirect, url_for, session
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)


# LOGIN/REGISTER PAGE
@auth.route('/login-register', methods=['GET', 'POST'])
def loginRegister():

  # If a form has been submitted ...
  if request.method == 'POST':


    # LOGIN
    #------------------------------------------------------
    # If data comes from login form ...
    if request.args.get('section') == 'login':

      # Get form data
      username = request.form.get('username')
      password = request.form.get('password')

      # Confirm the username exists
      user = User.query.filter_by(username=username).first()
      if user:

        # If password matches hash, log the user in
        if check_password_hash(user.password, password):
          session['currentUser'] = username
          return redirect(url_for('views.home'))

        # If password does not match hash, return error
        else:
          return render_template('login_register.html',
            section='login',
            error='user_details_not_found')

      # If username does not exist, return error
      else:
        return render_template('login_register.html',
          section='login',
          error='user_details_not_found')



    # REGISTER
    #------------------------------------------------------
    # If data comes from registeration form ...
    elif request.args.get('section') == 'register':

      # Get form data
      username = request.form.get('username')
      password = request.form.get('password')
      confirmPassword = request.form.get('confirm-password')

      # If username already exists, return error
      user = User.query.filter_by(username=username).first()
      if user:
        return render_template('login_register.html',
          section='register',
          error='usernameError')

      # If passwords do not match, return error
      if password != confirmPassword:
        return render_template('login_register.html',
          section='register',
          error='passwordError')

      # If all is good, register a new user
      new_user = User(username=username, password=generate_password_hash(password, method='sha256'))
      db.session.add(new_user)
      db.session.commit()
      session['currentUser'] = username
      return redirect(url_for('views.home'))



  # By default: render page template with args
  return render_template('login_register.html',
    section=request.args.get('section'),
    error=request.args.get('error'))





# CREATE LOGOUT CODE!!!!!!!!