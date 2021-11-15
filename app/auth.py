from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/login_register')
def login_register():
  return render_template('login_register.html')
