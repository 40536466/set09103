from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/login-register')
def loginRegister():
  return render_template('login_register.html')

@auth.route('/login-request', methods=['GET', 'POST'])
def loginRequest():
  return render_template('login_register.html')

@auth.route('/register-request', methods=['GET', 'POST'])
def registerRequest():
  return render_template('login_register.html')
