from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)


# LOGIN/REGISTER PAGE
@auth.route('/login-register', methods=['GET', 'POST'])
def loginRegister():

  # If a form has been submitted ...
  if request.method == 'POST':

    # If data comes from login form ...
    if request.args.get('section') == 'login':
      # Log the user in
      username = request.form.get('username')
      password = request.form.get('password')
      #include error=user_name_not_found arg in url if username not found -> see html login form

    # If data comes from registeration form ...
    elif request.args.get('section') == 'register':
      # Register a new user
      username = request.form.get('username')
      password = request.form.get('password')
      confirmPassword = request.form.get('confirm-password')
      #include error=usernameError arg in url if username already exists -> see html login form
      #include error=passwordError arg in url if password does not match -> see html login form


  # By default: render the template with args
  return render_template('login_register.html',
    section=request.args.get('section'),
    error=request.args.get('error'))
