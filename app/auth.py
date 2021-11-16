from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/login-register')
def loginRegister():
  return render_template('login_register.html')
